from django.urls import path
from . import views
from UnicoWebApp import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.home, name="home"),
    # Path Converters
    
    path('admin/', views.admin, name="admin"),
    path('create_content/', views.createContents, name="create-contents"),
    path('IN/', views.process_in, name="process-in"),
     path('5W/', views.process_5W, name="process-5W"),
    path('totem/', views.process_totem, name="process-totem"),
    path('theme/', views.process_theme, name="process-theme"),
    path('summary/', views.process_summary, name="process-summary"),    
    path('process_report/', views.process_report, name="process-report"),
    path('content_list/', views.content_list, name="content-list"),
    path('update_content/<content_id>', views.update_content_table, name='update-content'),
    path('delete_content/<content_id>', views.delete_content_table, name='delete-content'),
    path('banco-de-assunto/', views.banco_de_assunto, name='banco-de-assunto'),
    path('delete_conjunto/<content_id>', views.delete_conjunto_table, name='delete-conjunto'),
    path('add_conjunto/', views.add_conjunto_table, name='add-conjunto'),
    path('add_base/<conjunto_id>', views.add_base_table, name='add-base'),
    path('add_sub_base/<base_id>', views.add_sub_base_table, name='add-sub-base'),
    path('delete_base/<base_id>', views.delete_base_table, name='delete-base'),
    path('delete_sub_base/<sub_base_id>', views.delete_sub_base_table, name='delete-sub-base'),
    path('edit_conjunto/<conjunto_id>', views.edit_conjunto_table, name='edit-conjunto'),
    path('turma', views.turma_content, name='turma'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)