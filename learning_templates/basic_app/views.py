from django.shortcuts import render

# Create your views here.
def index(request):
     dict={"name":"sarang"}
     return render(request,"basic_app/index.html",dict)

def other(request):
    return render(request,"basic_app/other.html")

def relative(request):
    return render(request,"basic_app/relative_url_template.html")
