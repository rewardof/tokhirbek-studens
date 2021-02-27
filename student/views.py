from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentInputForm
from .models import Student


# def student_create_view(request):
#     if request.method == "GET":
#         form = StudentInputForm()
#         return render(request, 'student_create.html', {"form": form})
#     if request.method == 'POST':
#         form = StudentInputForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             form.save()
#             form = StudentInputForm()
#         context = {'form': form}
#         return render(request, 'student_create.html', context)

def student_create_view(request):
    if request.method == 'GET':
        form = StudentInputForm()
        context = {'form': form}
        return render(request, 'student_create.html', context)
    if request.method == 'POST':
        # print(request.POST[''])
        try:
            full_name = request.POST.get('full_name', 'Valiyev Ali')
            entry_date = request.POST.get('entry_date', '01.01.2021')
            email = request.POST.get('email', 'example@gmail.com')
            # faculty = request.POST.get('faculty')
            interests = request.POST.get('interests', 'My hobby is watching multic')
            password = request.POST.get('password', '0000')
            teacher = request.POST.get('teacher', 'Eshmamatova Dilfuza')
            data = Student.objects.create(full_name=full_name, entry_date=entry_date, email=email, interests=interests,
                                          password=password, teacher=teacher)
            print(data)
        except ValueError as ve:
            return HttpResponse('an error occured')
            print(ve)

        return render(request, 'student_create.html')
