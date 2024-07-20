from typing import List
from django.shortcuts import render
from .models import Notes #hna importina mel models.py class Notes
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
# Create your views here.

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/admin"
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes' 
    form_class = NotesForm 
    login_url = "/admin"
class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes' #redirect the user to a specific URL after a successful submission of a form, hadi tekhdem m3a tag form ki tdir par exmpl create wla update fl form tedik lel lien we7dakhor kima hna tedina lel ../smart/notes
    form_class = NotesForm 
    login_url = "/admin"

    def form_valid(self, form):  #form_valid method dakhla fl Django class-based view, form  is the validated form object ki tdekhel data ta3ek w tdir submit ki django ydir validation lhad data form hna yejme3ha 3ndeh data valid
        self.object = form.save(commit=False)  #This line saves the form data to an object without committing it to the database immediately(bla manzidoh lel database) This line saves the form data to an object without committing it to the database immediately.
        self.object.user = self.request.user  #hna tabe9na object lfoganiya m3a user ctd  you establish a relationship between the user and the saved data.
        self.object.save()  #This line saves the object to the database with the updated attributes.
        return HttpResponseRedirect(self.get_success_url())  #This line redirects the user to a specific URL after the form is successfully processed ctd tdik lel success_url = '/smart/notes'
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"
    def get_queryset(self) :
        return self.request.user.notes.all() #bhadi yweli luser yetel3oleh ghi notes taw3eh brk
        #now our end point is requiring user authentication, and then using the user of that request to just display the notes that were created by that user.
class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
    login_url = "/admin"
