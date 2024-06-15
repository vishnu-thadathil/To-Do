from django.urls import include, path

from task import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('create-task', views.create_task, name='create-task'),
    path('update-task/<int:task_id>', views.update_task, name='update-task'),
    path('ajax-delete-task', views.delete_task, name='ajax-delete-task'),
    path('send-email', views.send_email, name='send-email'),
]
