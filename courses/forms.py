from django import forms
from .models import AFFCourse, VisitorDetail


class CourseSelectForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=AFFCourse.objects.none(),
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        courses = kwargs.pop('courses', AFFCourse.objects.none())
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = courses


class VisitorDetailForm(forms.ModelForm):
    class Meta:
        model = VisitorDetail
        fields = ['email', 'phone_number', 'weight', 'height', 'full_name']
