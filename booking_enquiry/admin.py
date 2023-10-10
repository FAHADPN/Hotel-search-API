from django.contrib import admin
from .models import checkoutUserDetails

class CheckoutUserDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'destination', 'check_in_date', 'check_out_date', 'unique_id')

admin.site.register(checkoutUserDetails, CheckoutUserDetailsAdmin)
