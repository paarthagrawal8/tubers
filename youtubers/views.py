from django.shortcuts import render
from .models import Youtuber
from webpages.models import Slider
from django.shortcuts import get_object_or_404

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    slider = Slider.objects.all()
    city_search = Youtuber.objects.values_list('city' , flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type' , flat=True).distinct()
    category_search = Youtuber.objects.values_list('category' , flat=True).distinct()
   
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact = city)
            
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact = camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact = category)
    data = {
        'tubers' : tubers,
        'slider' : slider,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search,
    }
    return render(request , 'youtubers/youtubers.html' , data)

def youtubers_detail(request , id):
    tuber = get_object_or_404(Youtuber , pk = id)

    

    data={
        'tuber' : tuber,
    }
    return render(request , 'youtubers/youtuber_detail.html' , data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city' , flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type' , flat=True).distinct()
    category_search = Youtuber.objects.values_list('category' , flat=True).distinct()

    if 'Keyword' in request.GET:
        Keyword = request.GET['Keyword']
        if Keyword:
            tubers = tubers.filter(description__icontains = Keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact = city)
            
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact = camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact = category)
    

    data = {
        'tubers' : tubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search
    }
    return render(request , 'youtubers/search.html' , data)
