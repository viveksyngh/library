from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from views import *

urlpatterns = [ url(r'^books/$', 
                csrf_exempt(BookListView.as_view()), 
                name="book_list"),
                url(r'^book/(?P<book_id>[0-9]+)/$', 
                csrf_exempt(BookView.as_view()), 
                name="book"),
                url(r'^members/$', 
                csrf_exempt(MemberListView.as_view()), 
                name="member_list"),
                url(r'^member/(?P<member_id>[0-9]+)/$', 
                csrf_exempt(MemberView.as_view()), 
                name="member"),
                url(r'^issues/$', 
                csrf_exempt(IssueListView.as_view()), 
                name="issues"),
                url(r'^issue/(?P<book_id>[0-9]+)/member/(?P<member_id>[0-9]+)/$', 
                csrf_exempt(IssueView.as_view()), 
                name="issue"),
            ]