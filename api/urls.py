from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView, RegisterView

from api import views as api_views
from users import views as user_views

schema_view = get_schema_view(title='TinyTrader API', description='OpenAPI Schema')

# https://www.django-rest-framework.org/tutorial/quickstart/
router = routers.DefaultRouter()
router.register(r'ticker', api_views.TickerViewSet, 'ticker')
router.register(r'sector', api_views.SectorViewSet, 'sector')
router.register(r'industry', api_views.IndustryViewSet, 'industry')
router.register(r'size', api_views.SizeViewSet, 'size')
router.register(r'liquidity', api_views.LiquidityViewSet, 'liquidity')
router.register(r'metadata', api_views.MetadataViewSet, 'metadata')
router.register(r'metric', api_views.MetricViewSet, 'metric')
router.register(r'crypto', api_views.CryptoViewSet, 'crypto')
router.register(r'crypto/prices/historical', api_views.CryptoPricesHistoricalViewSet, 'crypto_prices_historical')
router.register('users', user_views.UsersViewSet, 'users')

app_name = 'api'
urlpatterns = [
  path('', include(router.urls)),
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # TODO: do we still need this??
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # TODO: do we need this??
  path('signup/email/<str:email>/', user_views.SignupEmailView.as_view(), name='signup_email'),
  path('user/detail/', user_views.UserDetailView.as_view(), name='user_detail'),

  path('login/', LoginView.as_view(), name='rest_login'),
  path('logout/', LogoutView.as_view(), name='rest_logout'),
  path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()), # needs to be defined before registration path
  path('signup/', RegisterView.as_view(), name='rest_register'),
  path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'), # only needed if email verification is mandatory
  path('token/refresh/', user_views.CustomTokenRefreshView.as_view(), name='token_refresh'),

  path('crypto/prices/live/<id>/', api_views.CryptoPricesLiveViewSet.as_view(), name='crypto_prices_live'),

  path('openapi/', schema_view, name='schema_view'),
  path('docs/', api_views.OpenApiView.as_view(), name='swagger_ui'),
]