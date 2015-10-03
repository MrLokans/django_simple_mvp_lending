from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email',]

    # validators
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "edu" not in email.split("@")[-1]:
            raise forms.ValidationError("Please use a valid colledge address.")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        return full_name