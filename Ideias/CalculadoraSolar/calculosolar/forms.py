from django import forms
from calculosolar.models import CalculoSolarPF, CalculoIrradianciaSolar,CalculoPotenciaGeracaoPF, QntPaineisPF,GeracaoPrevistaPF


class CalculoSolarPFForm(forms.ModelForm):
    class Meta:
        model = CalculoSolarPF
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


class CalculoPotenciaGeracaoPFForm(forms.ModelForm):
    class Meta:
        model = CalculoPotenciaGeracaoPF
        fields = '__all__'
        widgets = {
            'rendimento': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }


class QntPaineisPFForm(forms.ModelForm):
    class Meta:
        model = QntPaineisPF
        fields = '__all__'
        widgets = {
            'potpainel': forms.NumberInput(attrs={'min': 0}),
        }


class GeracaoPrevistaPFForm(forms.ModelForm):
    class Meta:
        model = GeracaoPrevistaPF
        fields = '__all__'
