from django.contrib import admin
from jobs.models import Jobs, Category

# Register your models here.
@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
