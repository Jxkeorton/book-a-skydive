from django import forms
from .models import AFFCourse, VisitorDetail
import re


class CourseSelectForm(forms.Form):
    """
    A form to select an AFFCourse from a
    dynamically provided list of courses.

    The queryset for the 'course' field is
    populated dynamically via the 'courses' argument
    passed during initialization.
    """
    course = forms.ModelChoiceField(
        queryset=AFFCourse.objects.none(),
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set the queryset
        for the 'course' field based on
        the 'courses' argument passed during initialization.
        """
        courses = kwargs.pop('courses', AFFCourse.objects.none())
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = courses


class VisitorDetailForm(forms.ModelForm):
    """
    A form for collecting visitor details,
    using the VisitorDetail model.

    Fields: email, phone_number, weight, height, and full_name.
    """
    MAX_WEIGHT = 100
    MAX_HEIGHT = 200
    
    class Meta:
        model = VisitorDetail
        fields = ['email', 'phone_number', 'weight', 'height', 'full_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d+$', phone_number):
            raise forms.ValidationError("Phone number must be numeric.")
        return phone_number
    
    def clean_weight(self):
        """
        Validates that the weight does not exceed the hardcoded maximum weight.
        """
        weight = self.cleaned_data.get('weight')
        if weight > self.MAX_WEIGHT:
            raise forms.ValidationError(f"Weight exceeds the maximum limit of {self.MAX_WEIGHT} kg.")
        return weight

    def clean_height(self):
        """
        Validates that the height does not exceed the hardcoded maximum height.
        """
        height = self.cleaned_data.get('height')
        if height > self.MAX_HEIGHT:
            raise forms.ValidationError(f"Height exceeds the maximum limit of {self.MAX_HEIGHT} cm.")
        return height
