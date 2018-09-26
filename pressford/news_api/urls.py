from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, CommentList, DetailsView, CommentReviewDetail


urlpatterns = {
    url(r'^news/$', CreateView.as_view(), name="create"),
    url(r'^news/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^news/(?P<pk>[0-9]+)/comments/$', CommentList.as_view(), name="comment"),
    url(r'^news/(?P<news_id>[0-9]+)/comments/(?P<comments_id>[0-9]+)/$',CommentReviewDetail.as_view())


}

urlpatterns = format_suffix_patterns(urlpatterns)
