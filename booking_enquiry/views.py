from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import KayakURLSerializer, checkoutDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import checkoutUserDetails




# def generate_kayak_url(destination, check_in_date, check_out_date, sort_option="distance_a"):
#     base_url = "https://www.kayak.co.in/hotels/"
#     # destination = quote(destination)  # URL-encode the destination

#     # Format the URL
#     kayak_url = f"{base_url}{destination}/{check_in_date}/{check_out_date}?sort={sort_option}"
    
#     return kayak_url

# @api_view(['POST'])
# def generate_kayak_url_view(request):
#     if request.method == 'POST':
#         serializer = KayakURLSerializer(data=request.data)
#         if serializer.is_valid():
#             destination = serializer.validated_data['destination']
#             check_in_date = serializer.validated_data['check_in_date']
#             check_out_date = serializer.validated_data['check_out_date']

#             # Modify the destination string if it contains spaces
#             if " " in destination:
#                 destination = destination.replace(" ", "%2C")

#             # Generate the Kayak URL
#             kayak_url = generate_kayak_url(destination, check_in_date, check_out_date)

#             response_data = {'url': kayak_url}
#             print(response_data)
#             return JsonResponse(response_data)
#         else:
#             return JsonResponse(serializer.errors, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@api_view(['POST'])
def checkout_user(request):
    if request.method == 'POST':
        serializer = KayakURLSerializer(data=request.data)
        if serializer.is_valid():
            destination = serializer.validated_data['destination']
            check_in_date = serializer.validated_data['check_in_date']
            check_out_date = serializer.validated_data['check_out_date']

            # Modify the destination string if it contains spaces
            if " " in destination:
                destination = destination.replace(" ", "%2C")

            # Generate the Kayak URL
            kayak_url = generate_kayak_url(destination, check_in_date, check_out_date)

            response_data = {'url': kayak_url}
            print(response_data)
            return JsonResponse(response_data)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    


# @api_view(['POST'])
# def checkout_user(request):
#     if request.method == 'POST':
#         serializer = checkoutDetails(data=request.data)
#         if serializer.is_valid():
#             destination = serializer.validated_data['destination']
#             check_in_date = serializer.validated_data['check_in_date']
#             check_out_date = serializer.validated_data['check_out_date']
#             print(destination)
#             print(check_in_date)
#             # print(type(check_out_date))
#     data = {'username':'Fahad','destination': destination, 'check_in_date': check_in_date, 'check_out_date': check_out_date}
#     # print(datetime.date(2023,10,1))
#     return render(request, 'index.html', data)

class CheckoutView(APIView):
    def post(self, request):
        serializer = checkoutDetails(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # Save the data to your model
            checkoutUserDetails.objects.create(**data)
            return render(request, 'checkout.html', data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)