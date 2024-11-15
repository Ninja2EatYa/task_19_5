from django.contrib import admin
from task1.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ('title', )
    list_per_page = 10
    fieldsets = (
        (None, {
            'fields': ('title', )
        }),
        ('Post text', {
            'classes': ('collapse', ),
            'fields': ('content', 'created_at')
        })
    )

    readonly_fields = ('created_at', )
