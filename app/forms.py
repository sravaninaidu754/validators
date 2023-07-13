
from django import forms
from django.core import validators
def validate_for_s(svalue):
    if svalue[0].lower()=='s':
        raise forms.ValidationError('sname should not be s length is less than 5')



def validate_for_length(name):
    if len(name)<=5:
        raise forms.ValidationError('length is less than 5')


class Studentform(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_s]) 
    sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()
    phone=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])


    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('email not matched')
    # def clean_url(self):
    #     u=self.cleaned_data['url']
    #     if u[-1]=='m': 
    #         raise forms.ValidationError('wewqewiuednmsnjsdh')


    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher'] 

        if len(bot)>0:
            raise forms.ValidationError('bot') 