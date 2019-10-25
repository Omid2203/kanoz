from django import forms
from .models import Student, Branch

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'family_name', 'cellphone', 'email', 'university', 'document', 'part', 'branch')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'part' in self.data:
            try:
                part_id = int(self.data.get('part'))
                self.fields['branch'].queryset = Branch.objects.filter(part_id=part_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Branch queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.part.branch_set.order_by('name')
