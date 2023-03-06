from django.shortcuts import render

def index(request):
    return render(request,
                  'index.html',
                  context = {}
                )
    # return HttpResponse(f"Hello, world. You're at the roadmap index.{request}")