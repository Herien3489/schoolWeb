from django.shortcuts import render, redirect
from .forms import LoginForm, LoginFormTeacher, UploadGradesForm
from .models import School, Teacher, Grades
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_student(request):
    return render(request, 'school/student/login-student.html')

def login_teacher(request):
    return render(request, 'school/teacher-portal/login-teacher.html')
    return render(request, 'school/student/grades.html')

def upload_grades(request):
    return render(request, 'school/teacher-portal/upload-grades.html')



def login_student(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                school = School.objects.get(email=email, password=password)
                request.session['email'] = school.email
                return redirect('grades')
            except School.DoesNotExist:
                messages.error(request, 'Usuario o contraseña incorrectos')
            # Aquí puedes agregar la lógica de autenticación
            return redirect('login_student')
    else:
        form = LoginForm()
    return render(request, 'school/student/login-student.html', {'form': form})

def login_teacher(request):
    if request.method == 'POST':
        form = LoginFormTeacher(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                teacher = Teacher.objects.get(email=email, password=password)
                request.session['email'] = teacher.email
                return redirect('upload_grades')
            except Teacher.DoesNotExist:
                messages.error(request, 'Usuario o contraseña incorrectos')
            # Aquí puedes agregar la lógica de autenticación
            return redirect('login_teacher')
    else:
        form = LoginForm()
    return render(request, 'school/teacher-portal/login-teacher.html', {'form': form})

def grades(request):
    email = request.session.get('email')
    if email:
        try:
            student = School.objects.get(email=email)  
            grades = student.grades_set.all()  
            return render(request, 'school/student/grades.html', {'grades': grades})
        except School.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')
            return redirect('login_student')
    else:
        messages.error(request, 'Usuario no autenticado')
        return redirect('login_student')
    



def upload_grades(request):
    email = request.session.get('email')
    if email:
        try:
            teacher = Teacher.objects.get(email=email)
        except Teacher.DoesNotExist:
            messages.error(request, 'Profesor no encontrado')
            return redirect('login_teacher')

        if request.method == 'POST':
            form = UploadGradesForm(request.POST, teacher=teacher)
            if form.is_valid():
                student = form.cleaned_data['student']
                subject = form.cleaned_data['subject']
                partial1 = form.cleaned_data['partial1']
                partial2 = form.cleaned_data['partial2']
                partial3 = form.cleaned_data['partial3']
                ordinary = form.cleaned_data['ordinary']

                # Verificar si ya existe un registro para el alumno, el profesor y la materia
                grades, created = Grades.objects.update_or_create(
                    student=student,
                    teacher=teacher,
                    subject=subject,
                    defaults={
                        'partial1': partial1,
                        'partial2': partial2,
                        'partial3': partial3,
                        'ordinary': ordinary,
                    }
                )

                if created:
                    messages.success(request, 'Calificaciones subidas exitosamente')
                else:
                    messages.success(request, 'Calificaciones actualizadas exitosamente')

                return redirect('upload_grades')
        else:
            form = UploadGradesForm(teacher=teacher)
        return render(request, 'school/teacher-portal/upload-grades.html', {'form': form})
    else:
        return redirect('login_teacher')



