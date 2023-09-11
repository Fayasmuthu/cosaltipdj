# from django import forms
# from django.forms import widgets
# from .models import ContactMessage

# class ContactForm(forms.ModelForm):
#     service = forms.ChoiceField(choices=[
#         ("", "Select service"),
#         ("1", "One"),
#         ("2", "Two"),
#         ("3", "Three"),
#     ], widget=forms.Select(attrs={"class": "single-input-field"}))

#     class Meta:
#         model = ContactMessage
#         exclude = ("timestamp",)
#         widgets = {
#             "full_name": widgets.TextInput(attrs={"class": "single-input-field", "placeholder": "Your Name"}),
#             "email": widgets.EmailInput(attrs={"class": "single-input-field", "placeholder": "Email address"}),
#             "phone_number": widgets.NumberInput(attrs={"class": "single-input-field", "placeholder": "Phone number"}),
#             "message": widgets.TextInput(attrs={"class": "single-input-field","placeholder": "Message"}),
#         }


from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     number = forms.CharField(max_length=20)
#     optionC = forms.ChoiceField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
#     message = forms.CharField(widget=forms.Textarea)


from django import forms
from .models import FormMessage 
from .models import Comment
# from .models import ContactMessage
from .models import EmailMessage



# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactMessage
#         fields = ['full_name', 'email', 'phone_number', 'services', 'message']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = FormMessage
        fields = ['name', 'email', 'number', 'optionC', 'message']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'comment']



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields=['email']

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact,Subscribe
from django.forms import widgets

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         exclude = ("timestamp",)
#         widgets = {
#             "full_name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Name"}),
#             "phone_number": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Phone"}),
#             "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
#              "message": widgets.Textarea(attrs={"class": "required form-control","placeholder": "Type Your Message",}),
#         }
class ContactForm(forms.ModelForm):
    # Add a new field for the service selection
    services = forms.ChoiceField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')],
                                 widget=forms.Select(attrs={"class": "required form-control"}))

    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "required form-control", "placeholder": "Your Name"}),
            "phone_number": forms.TextInput(attrs={"class": "required form-control", "placeholder": "Your Phone"}),
            "email": forms.EmailInput(attrs={"class": "required form-control", "placeholder": "Your Email Address"}),
            "message": forms.Textarea(attrs={"class": "required form-control", "placeholder": "Type Your Message"}),
        }

        # class SubscribeForm(forms.ModelForm):
        #     class Meta:
        #         model = Subscribe
        #         exclude = ("timestamp",)
        #         widgets = {
        #             "email": widgets.EmailInput(attrs={"class": "required form-control rounded-0  form-control-lg bubscribe-control px-5 py-3","placeholder": "Enter Your Email",}),
        #         }
from web.models import Subscribe  # Import the Subscribe model from your models.py

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        exclude = ("timestamp",)
        widgets = {
            "email": forms.EmailInput(attrs={"class": "required form-control rounded-0 form-control-lg subscribe-control px-5 py-3", "placeholder": "Enter Your Email"}),
        }