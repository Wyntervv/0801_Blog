from django.shortcuts import render,get_object_or_404,redirect
from .models import Board
import datetime

# Create your views here.
def index(request):
     board = Board.objects
     return render(request, 'index.html', {'boards':board})

def second(request):
    return render(request, 'second.html')

def third(request):
    ob = Board()
    ob.title = request.GET['title']
    ob.text = request.GET['text']
    ob.category = request.GET['category']
    ob.save()
    return redirect('/')

def read(request, board_id):
    read = get_object_or_404(Board, pk=board_id)
    return render(request, 'read.html', {'read':read})

def update(request, board_id):
    ob = get_object_or_404(Board, pk=board_id)
    return render(request, 'update.html', {'ob':ob})

def up(request,board_id):
    ob=get_object_or_404(Board, pk=board_id)
    ob.title = request.GET['title']
    ob.text = request.GET['text']
    ob.category = request.GET['category']
    ob.save()
    return redirect('/',board_id)

def delete(request,board_id):
    ol=get_object_or_404(Board, pk=board_id)
    ol.delete()
    return redirect('/')







    

