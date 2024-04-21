from django.urls import path
from animeList import views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('create_anime/', views.AnimeCreateView.as_view(), name='create-anime'),
    path('update_anime/', views.AnimeUpdateView.as_view(), name='update-anime'),
    path('seach_anime/', views.AnimeSearchView.as_view(), name='search-result'),
    path('details_anime/<int:pk>/', views.AnimeDetailView.as_view(), name='details-anime'),
    path('create_list', views.CreateUserAnimeView.as_view(), name='create-list'),
    path('update_list/<int:pk>/', views.UpdateUserAnimeView.as_view(), name='update-list'),

]