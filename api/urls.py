from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api import views as api_views
from users import views as user_views

# https://www.django-rest-framework.org/tutorial/quickstart/
router = routers.DefaultRouter()
router.register(r'ticker', api_views.TickerViewSet, 'ticker')
router.register(r'sector', api_views.SectorViewSet, 'sector')
router.register(r'industry', api_views.IndustryViewSet, 'industry')
router.register(r'size', api_views.SizeViewSet, 'size')
router.register(r'liquidity', api_views.LiquidityViewSet, 'liquidity')
router.register(r'metadata', api_views.MetadataViewSet, 'metadata')
router.register(r'metric', api_views.MetricViewSet, 'metric')
router.register('users', user_views.UsersViewSet, 'users')

app_name = 'api'
urlpatterns = [
  path('', include(router.urls)),
  path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  path('signup/email/<str:email>/', user_views.SignupEmailView.as_view(), name='signup-email'),
  path('user/detail/', user_views.UserDetailView.as_view(), name='user-detail'),
]