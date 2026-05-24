from django.shortcuts import render
from services.models import Service
from blog.models import Blog


def index (request):

    featured_services = Service.objects.filter(is_featured = True)
    latest_posts = Blog.objects.all()[:3]
    context = {
        'featured_services' : featured_services,
        'latest_posts':latest_posts,
    }

    return render(request,'core/index.html',context)

