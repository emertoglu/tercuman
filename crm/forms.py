from django import forms
from.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["account_name","account_type","account_area","account_phone","account_information"]