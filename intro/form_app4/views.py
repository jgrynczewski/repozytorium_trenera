from django.shortcuts import render

from form_app5.models import Task


# Create your views here.
def register(request):
    return render(
        request,
        'form_app4/register.html'
    )


def task_list(request):
    task = request.POST.get('task')
    if task:
        t = Task(text=task)
        t.save()

    tasks = Task.objects.all()

    return render(
        request,
        'form_app4/list.html',
        {'tasks': tasks}
    )
