from django.forms import ModelForm
from brand.models import Brand
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'brandForm'
        self.helper.add_input(Submit('submit', 'Salvar'))
