from django.shortcuts import render

TASKS = []

# Create your views here.
def register_task(request):
    # print(f"Metodą GET przyszło: {request.GET['task']}")
    # task = request.GET.get('task')
    task = request.POST.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'form_app/register.html',
        {"tasks": TASKS},
    )