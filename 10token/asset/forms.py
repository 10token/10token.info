from .models import Asset
from django import forms

class AssetSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search',
                    widget=forms.TextInput(attrs={'placeholder': 'Token name ... '})
                  )

    # token_id_exact = forms.IntegerField(
    #                 required = False,
    #                 label='token_id (token_id)!'
    #               )
