from django.urls import path, include
from rest_framework.routers import DefaultRouter
from breaks.views import dicts

router = DefaultRouter()
router.register(r'dicts/statuses', dicts.BreakStatusView, 'breaks-statuses')
router.register(r'replacements/statuses', dicts.ReplacementStatusView, 'replacements-statuses')

urlpatterns = [
    path('breaks/', include(router.urls)),
]