from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
  path('blog/', views.BlogListView.as_view(), name='blog'),
  path('blog-drafts/', views.BlogDraftListView.as_view(), name='drafts'),
  path('<slug:slug>/', views.BlogDetailView.as_view(), name='post'),
]