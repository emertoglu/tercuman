from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display =["account_name","account_type","account_area","account_created","account_phone"]

    class Meta:
        model = Account
