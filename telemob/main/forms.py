# -*- coding: utf-8 -*-

from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contacted_by', 'result')

    def clean_result(self):
        result = self.cleaned_data.get('result')
        contacted_by = self.cleaned_data.get('contacted_by')

        if contacted_by != 'tel' and result != None:
            raise forms.ValidationError(
                'Resultados só podem ser informados se o contato foi por Telefone =/'
            )

        return result