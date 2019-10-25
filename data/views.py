from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Student, Branch
from .forms import StudentForm

from django.core.files.storage import FileSystemStorage


class StudentLiView(ListView):
    model = Student
    context_object_name = 'student'

class StudentCreView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

class StudentUpView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

def load_branches(request):
    part_id = request.GET.get('part')
    branches = Branch.objects.filter(part_id=part_id).order_by('name')
    return render(request, 'data/branch_dropdown_list_options.html', {'branches': branches})

def index(request):
    return render(request, 'data/base.html')


def resume(request):
    if request.method == 'POST' and request.FILES["document"]:
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

    return render(request, 'data/registered.html')

def resume1(request):
    return render(request, 'data/resume.html')

