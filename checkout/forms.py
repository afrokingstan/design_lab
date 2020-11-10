from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('project_name', 'project_description',
                  'project_owner_full_name', 'project_owner_email',
                  'project_owner_phone_number', 'street_address1',
                  'street_address2', 'town_or_city', 'postcode',
                  'country', 'county',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'project_name': 'Project Name',
            'project_description': 'Project Description',
            'project_owner_full_name': 'Project Owner Full Name',
            'project_owner_email': 'Project Owner Email Address',
            'project_owner_phone_number': 'Project Owner Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['project_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
