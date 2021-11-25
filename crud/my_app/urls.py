from django.contrib import admin
from django.urls import path
from my_app import views

app_name = "my_app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index' ),
    path('student_form/', views.student_form, name='student_form' )
]