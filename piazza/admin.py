from django.contrib import admin
from .models import Messages, Reactions, Comments

# Register your models here.

admin.site.site_header = "Cloud Computing Coursework - Piazza Admin"

#admin.site.register(Messages)
@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('poster', 'title', 'postDate', 'expiryTime', 'category', 'active' )
    list_filter = ('poster', 'postDate', 'expiryTime', 'category', 'active')
    search_fields = ('title', 'body')
    date_hierarchy = 'postDate'

#admin.site.register(Reactions)
@admin.register(Reactions)
class ReactionsAdmin(admin.ModelAdmin):
    list_display = ('reactor','message', 'reactDate', 'reactType', Reactions.showPoster)
    list_filter = ('reactor', 'reactType', 'message')
    date_hierarchy = 'reactDate'

#admin.site.register(Reactions)
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('commentor', 'dateCommented','comment' ,Comments.showTitle)