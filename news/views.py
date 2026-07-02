from django.shortcuts import render
from .models import News
from django.db.models import Q

# Create your views here.

def home(request):
    news=News.objects.filter(status="Published").order_by("-created_at")
    context={
        "news":news,
    }
    
    return render(request,'newscategory/html/home.html',context)

def sports(request):

    news = News.objects.filter(
        category__name="Sports",
        status="Published"
    ).order_by("-created_at")
    context={
        "news":news,
    }

    return render(request, "newscategory/html/sport.html",context)

def politics(request):

    news = News.objects.filter(
        category__name="Politics",
        status="Published"
    ).order_by("-created_at")
    context={
        "news":news,
    }

    return render(request, "newscategory/html/politics.html",context)


def technology(request):

    news = News.objects.filter(
        category__name="Technology",
        status="Published"
    ).order_by("-created_at")
    context={
        "news":news,
    }
    return render(request, "newscategory/html/technology.html",context)


def business(request):

    news = News.objects.filter(
        category__name="Business",
        status="Published"
    ).order_by("-created_at")
    context={
        "news":news,
    }

    return render(request, "newscategory/html/business.html",context)

def entertainment(request):

    news = News.objects.filter(
        category__name="Entertainment",
        status="Published"
    ).order_by("-created_at")
    context={
        "news":news,
    }
    return render(request, "newscategory/html/entertainment.html",context)



def search(request):

    query = request.GET["q"]

    news = News.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )
    context={
        "news": news,
    }

    return render(
        request,
        "newscategory/html/home.html",
        context
        
    )

def error_404(request, exception):
    return render(request, "newscategory/html/pagenotfound.html", status=404)

# def category_news(request, category_name):

#     category = Category.objects.get(name=category_name)

#     news = News.objects.filter(
#         category=category,
#         status="Published"
#     ).order_by("-created_at")

#     context = {
#         "category": category,
#         "news": news,
#     }

#     return render(
#         request,
#         "newscategory/html/category.html",
#         context
#     )