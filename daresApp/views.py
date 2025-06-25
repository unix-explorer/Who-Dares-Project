from django.shortcuts import render
from .models import Votes
from .forms import VoteForm 
import os
# Create your views here.
def index(request):
    return render(request,'daresApp/index.html')

def maleView(request):
    pass

def maleView(request):
    pass