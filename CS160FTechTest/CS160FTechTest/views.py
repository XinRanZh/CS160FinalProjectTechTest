from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def testwrite(request):
    return render(request, 'testwrite.html')
def gallery(request):
    return render(request, 'gallery.html')