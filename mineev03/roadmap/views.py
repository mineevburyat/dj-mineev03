from django.shortcuts import render
from .models import RoadMapStudy
from django.http import HttpResponse


def index(request):
    roadmaps = RoadMapStudy.objects.all()
    num = roadmaps.count()
    return render(request,
                  'roadmap-index.html',
                  context = {
                      'roadmaps': roadmaps, 
                      'num': num})
    # return HttpResponse(f"Hello, world. You're at the roadmap index.{request}")