from django import forms
from django.db.models import F
from .models import AFFCourse, VisitorDetail

class DaySelectForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)

class CourseSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        date = kwargs.pop('date')
        super().__init__(*args, **kwargs)
        self.fields['course'] = forms.ModelChoiceField(
            queryset=AFFCourse.objects.filter(date=date, booked_slots__lt=F('max_slots')),
            empty_label="Select a Course"
        )

class VisitorDetailForm(forms.ModelForm):
    class Meta:
        model = VisitorDetail
        fields = ['email', 'phone_number', 'weight', 'height', 'full_name']
