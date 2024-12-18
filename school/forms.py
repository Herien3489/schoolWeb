from django import forms
from .models import School, Teacher, Grades

class LoginForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class LoginFormTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class UploadGradesForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ['student', 'teacher', 'subject', 'partial1', 'partial2', 'partial3', 'ordinary']

    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super(UploadGradesForm, self).__init__(*args, **kwargs)
        if teacher:
            self.fields['teacher'].queryset = Teacher.objects.filter(id=teacher.id)
            self.fields['subject'].initial = teacher.subject
            self.fields['subject'].widget.attrs['readonly'] = True