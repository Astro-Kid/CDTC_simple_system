from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'age', 'email', 'phone', 'location', 'hobby']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'age', 'email', 'phone', 'location', 'hobby']

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
