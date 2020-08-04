from django.contrib import admin
from .models import Post, Subscription, RelatedPost
# Register your models here.

admin.site.register(Post)
admin.site.register(Subscription)
admin.site.register(RelatedPost)
