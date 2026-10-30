from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <p>Hello World</p>
    <br>
    <p>My name is <h1>Arun<h1></p>
    """)