from django.shortcuts import render
from .models import MyIdea,TotalVisit
# Create your views here.
def home(request):
    i = TotalVisit.objects.all()
    if len(i)==0:i=0
    else :i=i.last().count
    TotalVisit(count=i+1).save()
    allidea = MyIdea.objects.all()
    if request.method=='POST':
        name = request.POST.get('instaid','unknown')
        idea = request.POST.get('idea','unknown')
        contri = MyIdea(name=name,idea=idea)
        contri.save()        
    return render(request,'home.html',{'allidea':allidea,'totalvisit':i})