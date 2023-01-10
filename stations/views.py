from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    
    # получите текущую страницу и передайте ее в контекст
    with open('data-398-2018-08-30.csv', newline='', encoding='Utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        list_reader = []
        for row in reader:
            list_reader.append({"Name": row['Name'], "Street": row['Street'], "District": row['District']})
    page_number = int(request.GET.get('page', 1))    
    paginator = Paginator(list_reader, 10)
    page = paginator.get_page(page_number)
    # bus_stations.get_
    # print(page)
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
