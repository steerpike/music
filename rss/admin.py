from django.contrib import admin

from rss.models import Feed


class FeedAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feed, FeedAdmin)
