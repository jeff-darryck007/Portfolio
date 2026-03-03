from .models import CompanySetting

def site_settings(request):
    return {
        'company': CompanySetting.objects.first()
    }
