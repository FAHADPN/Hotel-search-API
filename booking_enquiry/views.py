from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import KayakURLSerializer 




def generate_kayak_url(destination, check_in_date, check_out_date, sort_option="distance_a"):
    base_url = "https://www.kayak.co.in/hotels/"
    # destination = quote(destination)  # URL-encode the destination

    # Format the URL
    kayak_url = f"{base_url}{destination}/{check_in_date}/{check_out_date}?sort={sort_option}"
    
    return kayak_url

@api_view(['POST'])
def generate_kayak_url_view(request):
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
