from django.core.context_processors import csrf
from note.models import Note
from note.forms import NoteForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

# Create your views here.
def count_notes(request):
    amount = Note.objects.all().count()
    return {'amount' : amount}

def index(request):
    notes = Note.objects.all()
    return render_to_response("index.html", {'notes' : notes}, 
    context_instance=RequestContext(request, processors=[count_notes]))

#add request.FILES later
def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoteForm()
    return render_to_response('add.html', {'form' : form}, RequestContext(request, 
    processors=[count_notes]))
