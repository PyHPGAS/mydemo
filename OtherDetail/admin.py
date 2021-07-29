from django.contrib import admin
from OtherDetail.models import Religion, Mothertongue, Caste, SubCaste, Gotra, Education, Occupation
# Register your models here.
class ReligionAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("status",)

admin.site.register(Religion, ReligionAdmin)

class MothertongueAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("status",)

admin.site.register(Mothertongue, MothertongueAdmin)

class CasteAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",'state')
    list_filter = ("status",)

admin.site.register(Caste, CasteAdmin)

class SubCasteAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("status",)

admin.site.register(SubCaste, SubCasteAdmin)

class GotraAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("status",)

admin.site.register(Gotra, GotraAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",'state')
    list_filter = ("status",)

admin.site.register(Education, EducationAdmin)

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",'state')
    list_filter = ("status",)

admin.site.register(Occupation, OccupationAdmin)