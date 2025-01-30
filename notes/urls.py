from notes import views
from django.urls import path,include

urlpatterns = [

    path('',views.index,name='index'),
    path('add/',views.add_note,name='add_note'),
    path('edit/<int:note_id>',views.edit_note,name='edit_note'),
    path('delete/<int:note_id>',views.delete_note,name='delete_note'),
    path('notes/',views.view_note,name='view_note')

]