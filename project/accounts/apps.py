from django.apps import AppConfig


class AccountsConfig(AppConfig):
    def_auto_Fields='django.db.models.BigAutoField'
    name = 'accounts'
    
def ready(self):
     import accounts.signals