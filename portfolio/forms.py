from django import forms
from .widgets import CustomClearableFileInput
from .models import Portfolio


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Portfolio.objects.all()