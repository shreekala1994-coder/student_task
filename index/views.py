from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'index.html')


def calculator(request):
    if request.method=='POST':
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        result=n1+n2
        return render(request,'index.html',{'answer':result})

