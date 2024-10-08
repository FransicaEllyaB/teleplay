from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include,re_path

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-video-entry', create_video_entry, name='create_video_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-video/<uuid:id>', edit_video, name='edit_video'),
    path('delete/<uuid:id>', delete_video, name='delete_video'),
    path('create-video-entry-ajax', add_video_entry_ajax, name='add_video_entry_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]