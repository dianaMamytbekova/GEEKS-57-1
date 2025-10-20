from django.shortcuts import render, redirect
from . import models, forms


#CRUD - CREATE READ UPDATE DELETE

def createStudent(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = forms.StudentForm()        
    return render(request, template_name='student/create_student.html',
                  context={'form': form})    
        

#read        
def ReadStudent(request):
    if request.method == 'GET':
        student = models.Student.objects.all().order_by('-id')
    return render(request, template_name='students/student_list.html', context={'stud': student})
