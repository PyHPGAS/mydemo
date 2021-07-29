from django.shortcuts import render
from OtherDetail.models import Religion, Mothertongue, Caste, SubCaste, Gotra, Education, Occupation
from OtherDetail.serializers import ReligionSerializer, MothertongueSerializer, CasteSerializer, SubCasteSerializer, GotraSerializer, EducationSerializer, OccupationSerializer
from rest_framework import viewsets
# Create your views here.
class ReligionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = ReligionSerializer

    def get_queryset(self):

        try:
            return Religion.objects.all()
        except Exception as err:
            return {}

class MothertongueViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = MothertongueSerializer

    def get_queryset(self):

        try:
            return Mothertongue.objects.all()
        except Exception as err:
            return {}

class CasteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = CasteSerializer

    def get_queryset(self):

        try:
            return Caste.objects.all()
        except Exception as err:
            return {}

class SubCasteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = SubCasteSerializer

    def get_queryset(self):

        try:
            return SubCaste.objects.all()
        except Exception as err:
            return {}

class GotraViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = GotraSerializer

    def get_queryset(self):

        try:
            return Gotra.objects.all()
        except Exception as err:
            return {}

class EducationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = EducationSerializer

    def get_queryset(self):

        try:
            return Education.objects.all()
        except Exception as err:
            return {}

class OccupationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = OccupationSerializer

    def get_queryset(self):

        try:
            return Occupation.objects.all()
        except Exception as err:
            return {}
