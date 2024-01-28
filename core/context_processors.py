from website.models import Category


def categories(request):
    m_categories = Category.objects.all()
    return {
        'categories': m_categories,
    }
