from django.shortcuts import render

# Create your views here.


def classing(request):
    return render(request, 'second_task/class_template.html')



def functional(request):
    return render(request, 'second_task/func_template.html')
