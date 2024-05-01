from django.shortcuts import render
from .models import Company, Internship
from django.shortcuts import render, redirect
from .models import Internship
from .forms import InternshipForm
from .models import Company
def employer_page(request):
    companies = Company.objects.all()
    return render(request, 'employer_page.html', {'companies': companies})
'''def create_internship(request):
    companies = Company.objects.all()
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешного создания стажировки
    else:
        form = InternshipForm()
    return render(request, 'create_internship.html', {'form': form})
from django.shortcuts import render'''
def create_internship(request):
    companies = Company.objects.all()
    print(companies)  # Печать списка компаний для отладки
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InternshipForm()
    return render(request, 'create_internship.html', {'form': form, 'companies': companies})

def internship_search(request):
    if request.method == 'POST':
        education = request.POST.get('education')
        experience = request.POST.get('experience')
        direction = request.POST.get('direction')

        # Выполнение поиска в базе данных на основе данных из формы
        internships = Internship.objects.filter(
            education_required=education,
            experience_required=(experience == 'with_experience'),
            direction__icontains=direction
        )

        # Передача результатов поиска в контекст шаблона
        return render(request, 'search_results.html', {'internships': internships})
    else:
        # Возврат формы поиска, если запрос методом GET
        return render(request, 'internship_search.html')



def home(request):
    return render(request, 'home.html')
