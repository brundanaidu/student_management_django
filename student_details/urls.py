from django.urls import path
from student_details import views

urlpatterns=[
    path('',views.index,name='index'),
    path('create/', views.create, name ='create'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('view/<int:pk>',views.view,name='view'),
]