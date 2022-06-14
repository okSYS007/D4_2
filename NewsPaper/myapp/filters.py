from django_filters import FilterSet
from .models import Post
 
class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'creation_date':['gt'], 
            'post_title':['icontains'],
            'post_author__author_user__username':['contains']
        }