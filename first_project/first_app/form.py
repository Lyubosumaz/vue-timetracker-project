from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('NAME NEEDS TO START WITH Z')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea,)
    botcatcher = forms.ChoiceField(widget=forms.HiddenInput,
                                   required=False,
                                   validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcather = self.cleaned_data['botcatcher']
    #     if len(botcather) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return botcather

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH!')
