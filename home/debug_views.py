from django.http import JsonResponse
from django.conf import settings
import os

def health_check(request):
    """Endpoint simples para verificar se a aplicação está funcionando"""
    return JsonResponse({
        'status': 'OK',
        'debug': settings.DEBUG,
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'database_url_configured': bool(os.environ.get('DATABASE_URL')),
        'secret_key_configured': bool(os.environ.get('SECRET_KEY')),
    })
