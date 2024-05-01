from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),  # URL для главной страницы
    path('employer/', views.employer_page, name='employer_page'),
    path('create_internship/', views.create_internship, name='create_internship'),
    path('internship_search/', views.internship_search, name='internship_search'),
]
