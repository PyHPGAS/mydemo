from django.urls import path, include
from rest_framework.routers import DefaultRouter
from OtherDetail import views

router = DefaultRouter()
router.register(r'religions', views.ReligionViewSet, basename="api_religions")
router.register(r'mothertongues', views.MothertongueViewSet, basename="api_mothertongues")
router.register(r'castes', views.CasteViewSet, basename="api_castes")
router.register(r'subcastes', views.SubCasteViewSet, basename="api_subcastes")
router.register(r'gotras', views.GotraViewSet, basename="api_gotras")
router.register(r'educations', views.EducationViewSet, basename="api_educations")
router.register(r'occupations', views.OccupationViewSet, basename="api_occupations")

urlpatterns = [
    path('', include(router.urls)),
]
