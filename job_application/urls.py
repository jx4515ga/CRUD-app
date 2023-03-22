
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.job_form, name='job_insert'), #get and post req for insert operation 
    path('<int:id>/',views.job_form, name='job_update'),#get and post req for undate operation 
    path('list/',views.job_list, name='job_list'),#get and req to retreive and display all records
    path('delete/<int:id>/',views.job_delete, name='job_delete')
]
