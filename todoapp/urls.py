from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),   # ✅ ADD THIS
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('view/<int:id>/', views.view, name='view'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
