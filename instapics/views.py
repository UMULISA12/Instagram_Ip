import datetime as dt
from django.http  import HttpResponse,Http404
# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Image,Location
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    locations=Location.objects.all()

    return render(request,'welcome.html',{'images':images,'locations':locations})



def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
    #     message = f"{search_term}"

    #     return render(request, 'all-photos/search.html',{"message":message,"categories": searched_categories})

    # else:
    #     message = "You haven't searched for any term"
    #     return render(request, 'all-photos/search.html',{"message":message})      



def location(request,location_id):
    try:
        locations = Location.objects.all()
        location = Location.objects.get(id = location_id)
        images = Image.objects.filter(image_location = location.id)
    except:
        raise Http404()
    return render(request,'location.html',{'location':location,'images':images,'locations':locations})
