from django.shortcuts import render

# Create your views here.
def django(req):
    return render(req,('coures/dj.html'))

def python(req):
    return render(req,('coures/py.html'))