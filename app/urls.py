from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('forms', forms, name='forms'),
    # home panel
    path('add/home', ADD_HOME, name='add_home'),
    path('view/home', VIEW_HOME, name='view_home'),
    path('edit/home/<str:id>', EDIT_HOME, name='edit_home'),
    path('update/home/', UPDATE_HOME, name='update_home'),
    path('delete/home/<str:id>', DELETE_HOME, name='delete_home'),
    # statik panel
    path('add/statik', ADD_STATIK, name='add_statik'),
    path('view/statik', VIEW_STATIK, name='view_statik'),
    path('edit/statik/<str:id>', EDIT_STATIK, name='edit_statik'),
    path('update/statik', UPDATE_STATIK, name='update_statik'),
    path('delete/statik/<str:id>', DELETE_STATIK, name='delete_statik'),
    # PROBLEMS panels
    path('add/problems', ADD_PROBLEMS, name='add_problems'),
    path('add/problemss', ADD_PROBLEMSr, name='add_problemsr'),
    path('view/problems', VIEW_PROBLEMS, name='view_problems'),
    path('edit/problems/<str:id>', EDIT_PROBLEMS, name='edit_problems'),
    path('edit/problemsr/<str:id>', EDIT_PROBLEMSr, name='edit_problemsr'),
    path('update/problems', UPDATE_PROBLEMS, name='update_problems'),
    path('update/problemsr', UPDATE_PROBLEMSr, name='update_problemsr'),
    path('delete/problems/<str:id>', DELETE_PROBLEMS, name='delete_problems'),
    path('delete/problemsr/<str:id>', DELETE_PROBLEMSr, name='delete_problemsr'),
    # Social Networks panel
    path('add/social', ADD_SOCIAL, name='add_social'),
    path('view/social', VIEW_SOCIAL, name='view_social'),
    path('edit/social/<str:id>', EDIT_SOCIAL, name='edit_social'),
    path('update/social', UPDATE_SOCIAL, name='update_social'),
    path('delete/social/<str:id>', DELETE_SOCIAL, name='delete_social'),
    # Social Networks Link panel
    path('add/social/link', ADD_SOCIAL_LINK, name='add_social_link'),
    path('view/social/link', VIEW_SOCIAL_LINK, name='view_social_link'),
    path('edit/social/link/<str:id>', EDIT_SOCIAL_LINK, name='edit_social_link'),
    path('update/social', UPDATE_SOCIAL_LINK, name='update_social_link'),
    path('delete/social/<str:id>', DELETE_SOCIAL_LINK, name='delete_social_link'),

]
