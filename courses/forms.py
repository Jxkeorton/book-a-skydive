from django import forms
from .models import AFFCourse, VisitorDetail


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
    class Meta:
        model = VisitorDetail
        fields = ['email', 'phone_number', 'weight', 'height', 'full_name']
