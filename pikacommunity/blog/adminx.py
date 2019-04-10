import xadmin
from .models import BlogTag,Blog


class BlogTagAdmin(object):
    pass


class BlogAdmin(object):
    pass

xadmin.site.register(BlogTag,BlogTagAdmin)
xadmin.site.register(Blog,BlogAdmin)
