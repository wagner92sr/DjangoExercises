from django.shortcuts import render

# Create your views here.
def console_list(request):
    return render(request,'console.html')
