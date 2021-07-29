from rest_framework import serializers
from OtherDetail.models import Religion, Mothertongue, Caste, SubCaste, Gotra, Education, Occupation

class ReligionSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = Religion
        # fields = '__all__'
        fields = ['id', 'name']

class MothertongueSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = Mothertongue
        # fields = '__all__'
        fields = ['id', 'name']

class CasteSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = Caste
        # fields = '__all__'
        fields = ['id', 'name']


class SubCasteSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = SubCaste
        # fields = '__all__'
        fields = ['id', 'name']

class GotraSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = Gotra
        # fields = '__all__'
        fields = ['id', 'name']

class EducationSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Education
        # fields = '__all__'
        fields = ['id', 'name']


class OccupationSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Occupation
        # fields = '__all__'
        fields = ['id', 'name']