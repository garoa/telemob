# -*- coding: utf-8 -*-

from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('contacted_by', 'result', )

    def clean_result(self):
        #FIXME: os ranges e números abaixo dependem de RESULT_CHOICES em models.py
        contacted_by = self.cleaned_data.get('contacted_by')
        try:
            result = int(self.cleaned_data.get('result'))
        except TypeError:
            if contacted_by == 'telegram':
                result = 20
            else:
                raise forms.ValidationError(
                    'Por favor, informe o resultado do contato.'
                )

        if not contacted_by:
            raise forms.ValidationError(
                'Por favor, informe o meio de contato.'
            )


        #FIXME: os ranges e números abaixo dependem de RESULT_CHOICES em models.py
        if contacted_by == 'tel' and result not in range(10, 16):
            raise forms.ValidationError(
                'Este resultado só faz sentido se o contato foi por telefone.'
            )

        if contacted_by == 'fax' and result not in range(30, 34):
            raise forms.ValidationError(
                'Este resultado só faz sentido se o contato foi por fax.'
            )

        if contacted_by == 'email' and result not in range(40, 42):
            raise forms.ValidationError(
                'Este resultado só faz sentido se o contato foi por email.'
            )

        return result
