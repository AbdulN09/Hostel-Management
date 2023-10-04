from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('Admission/', views.Admission, name="Admission"),
    path('thanks/',views.thanks,name='thanks'),
    path('Display/', views.Display, name='Display'),
    path('about/', views.about, name='about'),
    path('images/', views.images, name='images'),
    path('services/', views.services, name='services'),
    path('view_student_detail/<str:student_id>/', views.view_student_detail, name='view_student_detail'),
    path('search/', views.search_student, name='search_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:Id>/',views.delete,name='delete'),
]



