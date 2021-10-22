from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from form_app5.models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()

    return render(request, 'form_app5/index.html', {
        "tasks": tasks
    })


@require_http_methods(["POST"])
def register(request):
    task = request.POST.get('task')
    if task:
        t = Task(text=task)
        t.save()

    tasks = Task.objects.all()

    return render(request, 'form_app5/register.html', {
        "tasks": tasks
    })

@require_http_methods(["GET", "POST"])
def update(request, task_id):
    # task = Task.objects.get(id=task_id)
    task = Task.objects.get(pk=task_id)

    # # Przy 4 dostaniemy wyjątek. Powinniśmy go obsłużyć.
    # p = Person.objects.get(pk=id)

    # zmieniam w settings DEBUG na False
    # ALLOWED_HOSTS = ["*"]

    # try:
    #     p = Person.objects.get(pk=id)
    # except ObjectDoesNotExist:
    #     raise Http404()

    # Albo na skróty
    # p = get_object_or_404(Person, id=id)

    if request.method == "GET":
        return render(request, "form_app5/update.html", {
            "task": task
        })

    elif request.method == "POST":
        task.text = request.POST.get('task')
        task.save()

        # Pokazać, że w pierwszym przypadku odświeżenie strony spowoduje próbę ponownego
        # wysłania danych, a w drugim i trzecim przypadku już nie.
        # Dlatego kiedy obsługujemy metodę POST lepiej jest używać redirect

        # tasks = Task.objects.all()
        # return render(request, 'form_app5/register.html', {"tasks": tasks})

        return redirect('form_app5:index')
        # return HttpResponseRedirect(reverse("form3:register"))


@require_http_methods(["POST"])
def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # task = Task.objects.get(pk=task_id)
    task.delete()

    return redirect('form_app5:list')
