from django.db import models
from phone_field import PhoneField
from ckeditor.fields import RichTextField

# Create your models here.

class Account(models.Model):
    name = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    account_name=models.CharField(max_length=25,verbose_name="Müşteri İsim Soyisim")
    account_type=models.CharField(max_length=25,verbose_name="Kategori")
    account_area=models.CharField(max_length=25,verbose_name="Bölge")
    account_phone = PhoneField(blank=True, verbose_name='Müşteri Number')
    account_information = RichTextField(verbose_name="Müşteri Notları")
    account_created = models.DateTimeField(auto_now=True,verbose_name="Kayıt Tarihi.")
    def __str__(self):
        return self.account_name


    


