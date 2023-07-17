from .import views
from django.urls import path

urlpatterns = [
    path('',views.f1,name="f1"),
    path('add_studdetails',views.add_studdetails,name='add_studdetails'),
    path('show_students',views.show_students,name='show_students'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('studname/<int:pk>',views.studname,name='studname'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('deletepage<int:pk>',views.deletepage,name='deletepage')
]
