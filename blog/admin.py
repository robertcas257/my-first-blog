from django.contrib import admin
# imported the Post model defined in models.py to 
from .models import Post

# to make visible on admin page, need to register the model 
admin.site.register(Post)