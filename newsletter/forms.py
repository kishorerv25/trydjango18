from django import forms
from .models import SignUp

<<<<<<< HEAD
class ContactForm(forms.Form):
    full_name = forms.CharField(required = False)
    email = forms.EmailField()
    message = forms.CharField()
    
=======

>>>>>>> 9fd0748a7995a1f445ae975cf4cfea51c8860cda
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if not domain == "gmail":
<<<<<<< HEAD
        	raise forms.ValidationError("Please make sure you use your gmail emil.")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .edu email address")
        return email

    def clean_full_name(self):
    	full_name = self.cleaned_data.get('full_name')
    	#form validtion
    	return full_name

=======
            raise forms.ValidationError(
                "Please make sure you use your gmail email.")
        if not extension == "edu":
            raise forms.ValidationError(
                "Please use a valid .edu email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # form validtion
        return full_name
>>>>>>> 9fd0748a7995a1f445ae975cf4cfea51c8860cda
