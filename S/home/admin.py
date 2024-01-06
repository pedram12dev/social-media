from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user' , 'slug' , 'created')
    list_filter = ('updated' , )
    search_fields = ('body' , )
    prepopulated_fields = {'slug' : ('body' , )}
    raw_id_fields = ('user' , )


