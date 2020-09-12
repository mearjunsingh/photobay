from .models import Category

def category(request):
    cats = Category.objects.all().order_by('category')
    return {'cat_menu' : cats}