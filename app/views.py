from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'index.html')
    
def katalog(request):

    return render(request, 'katalog.html')

def detailproduk(request):

    return render(request, 'portfolio-details.html')