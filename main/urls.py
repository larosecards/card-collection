from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, CategoryLink

urlpatterns = [
    path('', views.home, name='home'),  # Example route
    # Add other routes as needed
]

# Main view to render the card menu and categories
def card_menu_view(request):
    categories = Category.objects.prefetch_related('links').all()  # Fetch categories with related links
    return render(request, 'card_menu.html', {'categories': categories})

# View to fetch link content dynamically
def fetch_link_content(request, link_id):
    link = get_object_or_404(CategoryLink, id=link_id)  # Fetch the link by ID or return 404
    return JsonResponse({
        'title': link.name,  # Title of the link
        'content': link.content  # Content of the link
    })
