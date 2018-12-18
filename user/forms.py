from django import forms
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User


from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parolayı Doğrula", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =["first_name","last_name","username","email","password"]
        
    
    def clean(self):
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        
       

        if password != confirm:
            raise forms.ValidationError("Şifre Hatası")

       

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)



#non field eroros ile sadece tek clean il sorgulamada kullanılıyor.
#2 şekilde sorgulama yapıla bilir. örnek def clean_email ile.

#formlarda  username = forms.CharField(widget=form.input("class":"form-control"),max_length = 50,label = "Kullanıcı Adı") bu alana wigdet ekeleye biliyoruz örnek solda 

#clonlama init fonksiyonu ve usper init.
 #   def __init__(self,*args,**kwargs)
 #       super(RegisterForm,self).__init__(*args,**kwargs) init ile tek işlem formlara şekil vere bilitoruz.
 #       ^
#ama def ile sonuç alınmkaz ise .elle teker teker formlara widget gire ve attr girilcek ama genele de biz form cripsy ile yapıyoruz.










