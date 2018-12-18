from django.db import models
from ckeditor.fields import RichTextField



class Contact(models.Model):
    email= models.CharField(max_length=25,verbose_name="Lütfen Emailiniz Giriniz")
    full_name = models.CharField(max_length=25,verbose_name="Lütfen İsinizi Giriniz.")
    message =RichTextField(verbose_name="Lütfen Bizden İstediğniz Hizmeti Belirtin")
    def __str__(self):
        return self.email

