from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field


ACTIVITY = (
    ('', 'Choose...'),
    ('0.95','Sleeping'),
    ('1.0','Watching television'),
    ('1.3','Writing, desk work, typing'),
    ('2.0','Walking, household'),
    ('2.8','Walking, 2.0 mph '),
)

LEVEL = (
    ('', 'Choose...'),
    ('L', 'Light'),
    ('M', 'Moderate'),
    ('V', 'Vigorous')
)

GENDER = (
        ('', 'Choose...'),
        ('M', 'Male'),
        ('F', 'Female'),
        )

class BMRForm():
    firstname = forms.CharField()
    lastname = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER)
    age = forms.IntegerField()
    height = forms.DecimalField()
    weight = forms.IntegerField()

class METForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    activity = forms.ChoiceField(choices=ACTIVITY)
    level = forms.ChoiceField(choices=LEVEL)
    hours = forms.IntegerField()
    mins = forms.IntegerField()


class CrispyAddressForm(BMRForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('firstname', css_class='form-group col-md-6 mb-0'),
                Column('lastname', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('age', css_class='form-group col-md-6 mb-0'),
                Column('gender', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('height', css_class='form-group col-md-6 mb-0'),
                Column('weight', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Generate BMR Report')
        )

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'


class CustomFieldForm(METForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('firstname', css_class='form-group col-md-6 mb-0'),
                Column('lastname', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('activity', css_class='form-group col-md-6 mb-0'),
                Column('level', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('hours', css_class='form-group col-md-6 mb-0'),
                Column('mins', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Generate MET Report')
        )

