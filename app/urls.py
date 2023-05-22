from django.contrib import admin
from django.urls import path
from .views import landingview, loginview, login_action, logout_action, \
                   chore_type_listview, add_chore_type, confirm_delete_chore_type, delete_chore_type, edit_chore_type_get, edit_chore_type_post, \
                   chore_listview, add_chore, search_chores, confirm_delete_chore, delete_chore, edit_chore_get, edit_chore_post, chores_of_type, \
                   diary_listview, add_diary_entry, confirm_delete_diary_entry, delete_diary_entry, edit_diary_entry_get, edit_diary_entry_post

urlpatterns = [
    #Main page
    path('', landingview),


    #Login
    path('please_login/', loginview),
    path('login/', login_action),
    path('logout', logout_action),

    #ChoreTypes
    path('choretypes/', chore_type_listview),
    path('add-chore-type/', add_chore_type),
    path('confirm-delete-chore-type/<int:id>/', confirm_delete_chore_type),
    path('delete-chore-type/<int:id>/', delete_chore_type),
    path('edit-chore-type-get/<int:id>/', edit_chore_type_get),
    path('edit-chore-type-post/<int:id>/', edit_chore_type_post),

    #Chores
    path('chores/', chore_listview),
    path('add-chore/', add_chore),
    path('search-chores/', search_chores),
    path('confirm-delete-chore/<int:id>/', confirm_delete_chore),
    path('delete-chore/<int:id>/', delete_chore),
    path('edit-chore-get/<int:id>/', edit_chore_get),
    path('edit-chore-post/<int:id>/', edit_chore_post),
    path('category-chores/<int:id>/', chores_of_type),

    #History aka Chore Diary
    path('chore-diary/', diary_listview),
    path('add-to-diary/', add_diary_entry),
    path('confirm-delete-diary/<int:id>/', confirm_delete_diary_entry),
    path('delete-diary-entry/<int:id>/', delete_diary_entry),
    path('edit-diary-get/<int:id>/', edit_diary_entry_get),
    path('edit-diary-post/<int:id>/', edit_diary_entry_post)

]