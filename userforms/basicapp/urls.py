from django.shortcuts import render
from basicapp.view import auth,note
from django.conf.urls import url,include
# Create your views here.


app_name = 'basicapp'

urlpatterns=[
    url(r'^register/$',auth.register,name='register'),
    url(r'^user_login/$',auth.user_login,name='login'),
    url(r'^user_dashboard/$',note.User_Dashboard.as_view(),name='user_dashboard'),
    url(r'^create/$',note.NoteCreateView.as_view(),name='create'),
    url(r'^delete/(?P<pk>\d+)/$',note.NoteDeleteView.as_view(),name='delete'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$',note.userinformation,name='profile'),
    url(r'^update/(?P<pk>\d+)/$',note.update,name='update'),
    url(r'^remove/$',note.remove,name='remove'),
    
]
