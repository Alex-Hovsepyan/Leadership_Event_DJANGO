from django.contrib import admin
from .models import Header, HomeFirstPage, HighLights, About, Speakers, SpeakersContent, Schedules, SchedulesCategories, ScheldulesContent, Pricing
from .models import PricingContent, Venue, ContactGet, ContactPost, Footer
# Register your models here.

admin.site.register(Header)
admin.site.register(HomeFirstPage)
admin.site.register(HighLights)
admin.site.register(About)
admin.site.register(Speakers)
admin.site.register(SpeakersContent)
admin.site.register(Schedules)
admin.site.register(SchedulesCategories)

@admin.register(ScheldulesContent)
class ScheldulesContentModelAdmin(admin.ModelAdmin):

    list_display = ['title', 'category']
    list_display_links = ['title', 'category']
    search_fields = ['title', 'category']

admin.site.register(Pricing)
admin.site.register(PricingContent)
admin.site.register(Venue)
admin.site.register(ContactGet)

@admin.register(ContactPost)
class ContactPostModelAdmin(admin.ModelAdmin):

    list_display = ['user_name', 'user_email', 'date']
    list_display_links = ['user_name', 'user_email']
    search_fields = ['user_name', 'user_email']
    ordering = ['date']

admin.site.register(Footer)