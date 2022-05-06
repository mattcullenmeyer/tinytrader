from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

  def get_email_confirmation_url(self, request, emailconfirmation):
    base_url = 'https://app.tinytrader.io'
    # uncomment for testing
    # base_url = 'http://127.0.0.1:8080'
    url = f'{base_url}/confirm-email/{emailconfirmation.key}'
    return url
