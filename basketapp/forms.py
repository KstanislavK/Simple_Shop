from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='Количество')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

