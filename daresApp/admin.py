from django.contrib import admin
from .models import Votes
# Register your models here.

@admin.register(Votes)
class VotesAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Votes model.
    """
    list_display = ('image_id','image_file', 'category', 'votes')
    search_fields = ('category',)
    list_filter = ('category',)
    ordering = ('-votes',)
    

    def has_add_permission(self, request):
        return True   