from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Design


def home(request):
    designs = Design.objects.all().order_by('-id')
    paginator = Paginator(designs, 50)
    page = request.GET.get('page')
    try:
        displayed_designs = paginator.page(page)
    except:
        displayed_designs = paginator.page(1)

    pages = []
    for i in range(1, paginator.num_pages + 1, 1):
        pages.append(i)

    context = {
        'designs': displayed_designs,
    }
    return render(request, 'website/home.html', context)


def designs_page(request):
    designs = Design.objects.all().order_by('-id')
    paginator = Paginator(designs, 50)
    page = request.GET.get('page')
    try:
        displayed_designs = paginator.page(page)
    except:
        displayed_designs = paginator.page(1)

    pages = []
    for i in range(1, paginator.num_pages + 1, 1):
        pages.append(i)

    context = {
        'designs': displayed_designs,
        'pages': pages,
    }
    return render(request, 'website/designs/designs.html', context)


def design_details(request, id):
    design = get_object_or_404(Design, pk=id)
    design.likes += 1
    design.save()
    context = {
        'design': design,
    }
    return render(request, 'website/designs/details.html', context)
