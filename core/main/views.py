from django.shortcuts import render, redirect
from .models import Header, HomeFirstPage, HighLights, About, Speakers, SpeakersContent, Schedules, SchedulesCategories, ScheldulesContent, Pricing
from .models import PricingContent, Venue, ContactGet, ContactPost, Footer
from .forms import ContactModelForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            ContactPost.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactModelForm()

    header = Header.objects.all()[0]
    header_first_page = HomeFirstPage.objects.all()[0]
    highlights = HighLights.objects.all()
    about = About.objects.all()[0]
    speakers = Speakers.objects.all()[0]
    speakers_content = SpeakersContent.objects.all()
    schedules = Schedules.objects.all()[0]
    schedules_categories = SchedulesCategories.objects.all()
    schedules_content = ScheldulesContent.objects.all()
    pricing = Pricing.objects.all()[0]
    pricing_content = PricingContent.objects.all()
    venue = Venue.objects.all()[0]
    contact_get = ContactGet.objects.all()[0]
    footer = Footer.objects.all()[0]

    return render(request, 'index.html', context={
        'header':header,
        'header_first_page':header_first_page,
        'highlights':highlights,
        'about':about,
        'speakers':speakers,
        'speakers_content':speakers_content,
        'schedules':schedules,
        'schedules_categories':schedules_categories,
        'schedules_content':schedules_content,
        'pricing':pricing,
        'pricing_content':pricing_content,
        'venue':venue,
        'contact_get':contact_get,
        'footer':footer,
    })