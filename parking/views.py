from django.shortcuts import render

# Create your views here.
def index(r):
    a = "piyush"
    return render(r, 'parking/index.html',{"a":a})

