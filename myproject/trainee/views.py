from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Trainee
# Create your views here.
def inserttrainee(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        trainee = Trainee.objects.create(
            first_name=first_name, last_name=last_name,
            email=email, password=password
        )
        context['user_data'] = trainee
        return render(request, 'trainee/trainee_info.html', context=context)
    return render(request, 'trainee/trainee.html')
def deletetrainee(request,id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect(trainee_list)
def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/show_trainee.html', {'trainees': trainees})
def xorActivity(request,id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.Activity = not trainee.Activity
    trainee.save()
    return redirect('trainee_list')