# -*- coding: utf-8 -*-

from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contacted_by', 'result')

    def clean_result(self):
        result = int(self.cleaned_data.get('result'))
        contacted_by = self.cleaned_data.get('contacted_by')

        if contacted_by == 'tel' and result not in range(6):
            raise forms.ValidationError(
                'Este resultado só pode ser usado se o contato foi por Telefone =/'
            )

        if contacted_by == 'fax' and result not in range(6, 10):
            raise forms.ValidationError(
                'Este resultado só pode ser usado se o contato foi por Fax =/'
            )

        if contacted_by not in ('tel', 'fax') and result is not None:
            raise forms.ValidationError(
                'Não é preciso informar resultado se a forma de contato não for Fax ou Telefone =/'
            )

        return result