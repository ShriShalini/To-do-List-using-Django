from django.shortcuts import render
from basicapp.forms import CreateForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (DeleteView,ListView,CreateView)
from basicapp.model import note_model
from django.urls import reverse_lazy
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import json
import pdb
from django.forms.models import model_to_dict

User = get_user_model()

def index(request):
    return render(request,'basicapp/index.html')

@login_required
def remove(request):
    return HttpResponseRedirect(reverse('basicapp:user_dashboard'))


class User_Dashboard(ListView):
    fields = ("title","content",)
    model = note_model.Note
    template_name='basicapp/dashboard.html'
    context_object_name = 'note_list'
    def get_queryset(self):
        user =  self.request.user
        notelist  = note_model.Note.objects.all().filter(user=user)
        return notelist


class NoteCreateView(CreateView):
    context_object_name = 'note_create'
    model = note_model.Note
    form_class = CreateForm
    template_name='basicapp/dashboard.html'
    #pdb.set_trace()
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    

class NoteDeleteView(DeleteView):
    model = note_model.Note
    template_name = 'basicapp/dashboard.html'
    context_object_name = 'note_edit'
    success_url = reverse_lazy("basicapp:user_dashboard")

@login_required
def update(request,pk):
    title = request.POST.get('title')
    note = get_object_or_404(note_model.Note,pk=int(pk))
    note.title = title
    note.save()
    return JsonResponse("success",safe=False)

@login_required
def userinformation(request,username):
    user = get_object_or_404(User,username=username)   
    return JsonResponse(model_to_dict(user))