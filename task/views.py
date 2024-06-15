from django.http import JsonResponse
from django.shortcuts import redirect, render

from task.models import Task

from .forms import CreateTaskForm, SendEmailForm


def index(request):
    # TODO: Filter based on date and pagination
    task_list = Task.objects.all()

    return render(request, 'task/index.html', {'task_list': task_list})


def create_task(request):
    form = CreateTaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'task/create_task.html', {'form': form})


def update_task(request, task_id):
    task = Task.objects.get(task_id=task_id)
    form = CreateTaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'task/create_task.html', {'form': form})


def delete_task(request):
    task_id = request.POST.get('task_id')
    task = Task.objects.get(task_id=task_id)
    task.delete()

    return JsonResponse({'detail': 'Deleted successfully'}, safe=False)


def send_email(request):
    form = SendEmailForm()
    if request.method == 'POST':
        # TODO: Send email
        return redirect('index')

    return render(request, 'task/send_email.html', {'form': form})
