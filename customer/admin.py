from django.contrib import admin
from .models import (
    CustomUser,
    UserPayment,
    UserAddress,
    ProductReview,
)

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name']
    search_fields = ('email', 'username', 'cid')
    readonly_fields = ['image_tag']

@admin.register(UserAddress)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['addr1',]
    search_fields = ['city', 'country',]
    readonly_fields = ['addr1', 'addr2', 'city', 'country']

@admin.register(UserPayment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'provider']
    search_fields = ['provider']
    readonly_fields = ['account_number', 'provider']

@admin.register(ProductReview)
class AdminReview(admin.ModelAdmin):
    list_display = ['review_title', 'review_rating']
    readonly_fields = ['review_screenshots']
