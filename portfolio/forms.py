from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Portfolio.objects.all()