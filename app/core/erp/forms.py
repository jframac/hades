from django.forms import *

from .models import Category


class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = 'True'
             

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingeres un nombre',
                    'autocomplet': 'off'
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingeres una descripción',
                    'rows': 3,
                    'cols': 3,
                }
            )
        }
