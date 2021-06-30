from django.shortcuts import render
from .models import MyIdea
# Create your views here.
i=0
def home(request):
    global i
    i+=1
    allidea = MyIdea.objects.all()
    if request.method=='POST':
        name = request.POST.get('instaid','unknown')
        idea = request.POST.get('idea','unknown')
        contri = MyIdea(name=name,idea=idea)
        contri.save()        
    return render(request,'home.html',{'allidea':allidea,'totalvisit':i})