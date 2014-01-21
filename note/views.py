from django.shortcuts import render_to_response
from note.models import Note

# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render_to_response("index.html", {'notes' : notes})
