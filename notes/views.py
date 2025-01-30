from django.shortcuts import render,redirect,get_object_or_404
from .forms import NoteForm
from .models import Note

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add_note(request):
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect('view_note')
    
    else:
         form=NoteForm()
    return render(request,'add_note.html',{'form':form,'note':None})

def view_note(request):
    notes=Note.objects.all()
    context={'notes':notes}
    return render(request,'view_note.html',context)

def edit_note(request,note_id):
    note=get_object_or_404(Note,id=note_id)
    if request.method=='POST':
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('view_note')

    else:
        form=NoteForm(instance=note)
    return render(request,'add_note.html',{'form':form,'note':note})


def delete_note(request,note_id):
    note=get_object_or_404(Note,id=note_id)
    if request.method=='POST':
        note.delete()
        return redirect('view_note')
    return render(request, 'delete_confirm.html', {'note': note})
    
        
    

    
        



