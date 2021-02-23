from hotel.forms import HotelForm
from hotel.forms import HotelFormNew
from hotel.models import Hotel
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    submitbutton = request.POST.get("submit")
    if request.method == "POST":
        form = HotelFormNew(request.POST)

        if form.is_valid():
            if request.POST.get("rating") != "": 
                ratingFromHtml = request.POST.get("rating")
            else:
                ratingFromHtml = None

            if request.POST.get("city") != "": 
                cityFromHtml = request.POST.get("city")
            else:
                cityFromHtml = ""   

            if request.POST.get("price") != "": 
                priceFromHtml = request.POST.get("price")
            else:
                priceFromHtml = None 

            if priceFromHtml == None and ratingFromHtml == None and cityFromHtml == "": #Если все не заполнено
                object = Hotel.objects.all()
                return render(request, 'hotel/index.html', {'form': form, 'submitbutton': submitbutton, 'object': object })
            
            if ratingFromHtml == None and cityFromHtml == "": #Если рейтинг и город не заполнены
                object = Hotel.objects.filter(price = priceFromHtml)
                return render(request, 'hotel/index.html', {'form': form, 'submitbutton': submitbutton, 'object': object })

            if ratingFromHtml == None and priceFromHtml == None: #Если рейтинг и цена не заполнены
                object = Hotel.objects.filter(city = cityFromHtml)
                return render(request, 'hotel/index.html', {'form': form, 'submitbutton': submitbutton, 'object': object })

            if cityFromHtml == "" and priceFromHtml == None: #Если город и цена не заполнены
                object = Hotel.objects.filter(rating = ratingFromHtml)
                return render(request, 'hotel/index.html', {'form': form, 'submitbutton': submitbutton, 'object': object })

            if ratingFromHtml == None: #Если рейтинг не заполнен
                object = Hotel.objects.filter(city = cityFromHtml, price = priceFromHtml)
                return render(request, 'hotel/index.html', {'form': form, 'submitbutton': submitbutton, 'object': object })

            if cityFromHtml == "": #Если город не заполнен
                object = Hotel.objects.filter(rating = ratingFromHtml, price = priceFromHtml)
                return render(request, 'hotel/index.html', {'form': form, 'submitbutton': submitbutton, 'object': object })

            if priceFromHtml == None: #Если цена не заполнена
                object = Hotel.objects.filter(rating = ratingFromHtml, city = cityFromHtml)
                return render(request, 'hotel/index.html', {'form': form, 'submitbutton': submitbutton, 'object': object })

            #return render(request, 'hotel/index.html', {'form': form})
        else: 
            return HttpResponse("Invalid data")

    else:
        form = HotelFormNew()
        return render(request, 'hotel/index.html', {'form': form })

def about(request):
    return render(request, 'hotel/about.html')

def contacts(request):
    return render(request, 'hotel/contacts.html')