from django.shortcuts import render
from planes.models import CustomUser

# Create your views here.
def index(request):
    users_list = CustomUser.objects.all()
    context = {
        "users_list": users_list,
    }
    return render(request, 'administration/index.html', context)
