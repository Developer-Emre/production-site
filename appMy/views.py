from django.shortcuts import render
from.models import *


# Create your views here.

def index(request):
    welcome_text=Welcome.objects.all()
    company=Header.objects.all()
    detail_card=detailCard.objects.all()
    team=Team.objects.all()
    card=Card.objects.all()
    cardtwo=Cardtwo.objects.all()
    latesnews=latestNews.objects.all()
    
    context={
        "welcome_text":welcome_text,
        "company":company,
        "detail_card":detail_card,
        "team":team,
        "card":card,
        "cardtwo":cardtwo,
        "latesnews":latesnews,
    }
    
    return render(request,'index.html',context)