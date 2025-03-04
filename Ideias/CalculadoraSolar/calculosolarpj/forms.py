from django import forms
from calculosolarpj.models import CalculoSolarPJ,CalculoPotenciaGeracaoPJ, QntPaineisPJ,GeracaoPrevistaPJ
from calculosolar.models import  CalculoIrradianciaSolar

class CalculoSolarPJForm(forms.ModelForm):
    class Meta:
        model = CalculoSolarPJ
        fields = '__all__'
        widgets = {
            'cons_jan': forms.NumberInput(attrs={'min': 0}),
            'cons_fev': forms.NumberInput(attrs={'min': 0}),
            'cons_mar': forms.NumberInput(attrs={'min': 0}),
            'cons_abr': forms.NumberInput(attrs={'min': 0}),
            'cons_mai': forms.NumberInput(attrs={'min': 0}),
            'cons_jun': forms.NumberInput(attrs={'min': 0}),
            'cons_jul': forms.NumberInput(attrs={'min': 0}),
            'cons_ago': forms.NumberInput(attrs={'min': 0}),
            'cons_set': forms.NumberInput(attrs={'min': 0}),
            'cons_out': forms.NumberInput(attrs={'min': 0}),
            'cons_nov': forms.NumberInput(attrs={'min': 0}),
            'cons_dez': forms.NumberInput(attrs={'min': 0}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Aqui você pode adicionar validações específicas da interface, se necessário.
        return cleaned_data


class CalculoIrradianciaSolarForm(forms.ModelForm):
    class Meta:
        model = CalculoIrradianciaSolar
        fields = '__all__'
        widgets = {
            'irradi_jan': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_fev': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_mar': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_abr': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_mai': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_jun': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_jul': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_ago': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_set': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_out': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_nov': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
            'irradi_dez': forms.NumberInput(attrs={'min': 0, 'step': 'any'}),
        }


class CalculoPotenciaGeracaoPJForm(forms.ModelForm):
    class Meta:
        model = CalculoPotenciaGeracaoPJ
        fields = '__all__'
        widgets = {
            'rendimento': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }


class QntPaineisPJForm(forms.ModelForm):
    class Meta:
        model = QntPaineisPJ
        fields = '__all__'
        widgets = {
            'potpainel': forms.NumberInput(attrs={'min': 0}),
        }


class GeracaoPrevistaPJForm(forms.ModelForm):
    class Meta:
        model = GeracaoPrevistaPJ
        fields = '__all__'
