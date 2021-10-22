from django.shortcuts import render


# Create your views here.
def register(request):
    return render(
        request,
        'form_app3/register.html'
    )


def task_list(request):

        with open("tasks.txt", 'a+') as f:
            task = request.POST.get('task')
            if task:
                f.write(task+"\n")

        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()

    return render(
        request,
        'form_app3/list.html',
        {"tasks": tasks},
    )