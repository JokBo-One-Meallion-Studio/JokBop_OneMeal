from django.contrib import admin
from .models import Jok_Post
from .models import Bob_Post
from .models import Jok_comment
from .models import Bob_comment

admin.site.register(Jok_Post)
admin.site.register(Bob_Post)
admin.site.register(Bob_comment)
admin.site.register(Jok_comment)


# Register your models here.
