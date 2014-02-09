from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField
from poll.models import loantype_choices, State, Saletype, Person
import pdb


class ContactForm1(forms.ModelForm):
    confirm_email = forms.EmailField()
    
    class Meta:
        model=Person

    def clean_loan_amount(self):
        cd = self.cleaned_data
        loanamount = cd.get('loan_amount' or None)
        if loanamount <= 0:
            raise forms.ValidationError('The loan amount cannot be negative or zero')
        return loanamount

    def clean(self):
        pdb.set_trace()
        cd = self.cleaned_data
        email1 = cd.get('email' or None)
        email2 = cd.get('confirm_email' or None)
        if email1 != email2:
            raise forms.ValidationError("Emails does not match")
        return cd
        

class ContactForm(forms.Form):
    firstname = forms.CharField()
    #middlename = forms.CharField(required=False)
    lastname = forms.CharField()
    email = forms.EmailField()
    confirm_email = forms.EmailField()
    phone_number = USPhoneNumberField()
    saletype = forms.ModelChoiceField(queryset=Saletype.objects.all())
    loan_type = forms.TypedChoiceField(choices = ((('-----','-----'),)+loantype_choices))
    loan_amount = forms.IntegerField()
    credit_tier = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    state = forms.ModelChoiceField(queryset=State.objects.all())
    zipcode = forms.IntegerField()



    
    
    
   
