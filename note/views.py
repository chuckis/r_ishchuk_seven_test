from django.core.context_processors import csrf
from note.models import Note
from note.forms import NoteForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
#CBV 
from django.views.generic import ListView

# Create your views here.

class ListNoteView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = "index.html"
    paginate_by = 5

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
