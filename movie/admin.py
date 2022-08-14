from django.contrib import admin
from .models import Movie,Review
# Register your models here.

admin.site.register(Movie) # Registered the movie model to the admin 
admin.site.register(Review)