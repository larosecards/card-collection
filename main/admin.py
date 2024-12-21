from django.contrib import admin
from .models import Category, CategoryLink, Image

# Admin interface for the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display these fields in the admin list view
    search_fields = ('name',)  # Add search functionality for the name field


# Admin interface for the CategoryLink model
@admin.register(CategoryLink)
class CategoryLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # Display these fields in the admin list view
    search_fields = ('name', 'content')  # Add search functionality for the name and content fields
    list_filter = ('category',)  # Add a filter for the category field


# Admin interface for the Image model (if used)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'description')  # Display these fields in the admin list view
    search_fields = ('description',)  # Add search functionality for the description field
    list_filter = ('link',)  # Add a filter for the link field
