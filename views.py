from django.shortcuts import render

# Create your views here.
# Create your views here.
def index( request ) :
    context = {
        'title' : 'Productos'    
    }
    return render( request, 'products/index.html', context )