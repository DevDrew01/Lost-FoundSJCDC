from django import forms
from .models import ItemReport


class ItemReportForm(forms.ModelForm):
    class Meta:
        model = ItemReport
        fields = ['item_name', 'category', 'location', 'description', 'image']

        widgets = {
            'item_name': forms.TextInput(attrs={
                'placeholder': 'e.g. Blue Hydroflask',
                'class': 'form-input'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Provide details like brand, color, or specific markings...',
                'class': 'form-input'
            }),
            'location': forms.Select(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
        }