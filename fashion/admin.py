from django.contrib import admin
from .models import Image ,Profile , Review

# Register your models here.
class ReviewAdmin (admin.ModelAdmin):
    list_display = ('name' ,'post' ,'body')
    actions = ['allow_review']

    def allow_reviews(self , request , queryset):
        queryset.update(active = True)

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('image' ,)

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('image' ,)

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Review)