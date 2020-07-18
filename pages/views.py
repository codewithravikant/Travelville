from django.shortcuts import render, get_object_or_404
from pages.models import City
from django.views.generic import DeleteView


# create your views here.
def hello_pages(request):
    return render(request, 'home.html')


def get_city_info(request):
    cityname = request.GET.get('cityname')
    print("cityname " + str(cityname))
    result_set = City.objects.filter(name=cityname)

    context = {
        'object_list': result_set
    }

    return render(request, 'city_detail.html', context)
