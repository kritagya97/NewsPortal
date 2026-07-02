from django.contrib import admin
from .models import Category,News

# Register your models here.
admin.site.site_header = "News Portal Administration"
admin.site.site_title = "News Portal Admin"
admin.site.index_title = "Welcome to News Portal"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "category",
        "auto_category",
        "status",
        "author",
        "created_at",
        "image",
    ]

    list_filter = [
        "category",
        "status",
        "created_at"
    ]

    search_fields = [
        "title",
        "content"
    ]

    readonly_fields = [
        "auto_category",
        "created_at",
        "updated_at",
        "views"
    ]
