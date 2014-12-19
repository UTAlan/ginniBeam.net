from django.contrib.syndication.views import Feed
from blog.models import Post

class LatestBlogs(Feed):
    title = "ginnibeam.net"
    link = "http://www.ginnibeam.net"
    description = "ginnibeam.net Blog"

    def items(self):
        return Post.objects.filter(is_public=True).filter(groups__isnull=True).order_by('-created_date')[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content.replace('\n','<br />\n')
