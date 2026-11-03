from django.shortcuts import render
from.models import Destination
# Create your views here.
def index(request):
    Dest1 = Destination()
    Dest1.name='Bengaluru'
    Dest1.desc='The city is never sleep'
    Dest1.prise= 800

    Dest2= Destination()
    Dest2.name='Mubai'
    Dest2.desc='Financial hub of Bollywood'
    Dest2.prise= 1000

    Dest3= Destination()
    Dest3.name='Jaipur'
    Dest3.desc='Pink city with royal palaces'
    Dest3.prise= 600

    Dest4= Destination()
    Dest4.name='Varanasi'
    Dest4.desc='Ancient spiritual capital on Ganges'
    Dest4.prise= 900

    Dest5= Destination()
    Dest5.name='Udaipur'
    Dest5.desc='City of lakes and palaces'
    Dest5.prise= 500

    Dest6= Destination()
    Dest6.name='Kolkata'
    Dest6.desc='Cultural capital of India'
    Dest6.prise= 800

    Dests=[Dest1, Dest2, Dest3, Dest4, Dest5, Dest6]

    return render(request,"index.html",{'Dests':Dests})