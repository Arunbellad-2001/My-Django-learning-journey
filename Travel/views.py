from django.shortcuts import render
from.models import Destination
# Create your views here.
def index(request):
    Dest1 = Destination()
    Dest1.name='Bengaluru'
    Dest1.desc='The city is never sleep'
    Dest1.prise= 800
    return render(request,"index.html",{'Dest1':Dest1})
