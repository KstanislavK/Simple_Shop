from django import forms
from .models import OrderList


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderList
        fields = ('first_name', 'email', 'phone_number', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
