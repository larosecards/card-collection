from django.shortcuts import render
from .models import Category
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import CategoryLink

# Create your views here.
def home(request):
    return render(request, 'index.html')

def fetch_link_content(request, link_id):
    link = get_object_or_404(CategoryLink, id=link_id)
    return JsonResponse({
        'title': link.name,  # Title of the link
        'content': link.content  # Content of the link
    })
def card_menu_view(request):
    categories = Category.objects.prefetch_related('links').all()
    return render(request, 'card_menu.html', {'categories': categories})