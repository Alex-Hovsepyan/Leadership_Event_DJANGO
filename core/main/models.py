from django.db import models

# Create your models here.

class Header(models.Model):

    general_title = models.CharField('General Page Title', max_length=50)
    left_title = models.CharField('Left Title', max_length=40)
    right_title = models.CharField('Right Title', max_length=40)
    path1 = models.CharField('Path 1', max_length=50)
    path2 = models.CharField('Path 2', max_length=50)
    path3 = models.CharField('Path 3', max_length=50)
    path4 = models.CharField('Path 4', max_length=50)
    path5 = models.CharField('Path 5', max_length=50)
    path6 = models.CharField('Path 6', max_length=50)
    path7 = models.CharField('Path 7', max_length=50)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class HomeFirstPage(models.Model):

    video = models.FileField('Background Video', upload_to='videos')
    left_title = models.CharField('Left Title', max_length=40)
    right_title = models.CharField('Right Title', max_length=40)
    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)

    class Meta:

        verbose_name = 'Home First Page'
        verbose_name_plural = 'Home First Page'

class HighLights(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    video_link = models.URLField('Video Link')
    
    class Meta:

        verbose_name = 'HighLights'
        verbose_name_plural = 'HighLights'

    def __str__(self) -> str:
        return self.title
    
class About(models.Model):

    left_title = models.CharField('Left Title', max_length=40)
    right_title = models.CharField('Right Title', max_length=40)
    subtitle = models.CharField('Subtitle', max_length=80)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    left_btn = models.CharField('Left Button', max_length=40)
    right_btn = models.CharField('Right Button', max_length=40)
    img1 = models.ImageField('Image 1', upload_to='images')
    img2 = models.ImageField('Image 2', upload_to='images')
    img3 = models.ImageField('Image 3', upload_to='images')
    img4 = models.ImageField('Image 4', upload_to='images')
    info = models.CharField('Info 1', max_length=80)
        
    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class Speakers(models.Model):

    left_title = models.CharField('Left Title', max_length=40)
    right_title = models.CharField('Right Title', max_length=40)
    text = models.TextField('Text')
    title = models.CharField('Title', max_length=50)
    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=50)
    profession = models.CharField('Profession', max_length=60)
    social1 = models.CharField('Social 1', max_length=50, blank=True)
    social_url1 = models.URLField('Social Url 1', blank=True)
    social2 = models.CharField('Social 2', max_length=50, blank=True)
    social_url2 = models.URLField('Social Url 2', blank=True)
    social3 = models.CharField('Social 3', max_length=50, blank=True)
    social_url3 = models.URLField('Social Url 3', blank=True)

    class Meta:
        
        verbose_name = 'Speakers'
        verbose_name_plural = 'Speakers'

class SpeakersContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=50)
    profession = models.CharField('Profession', max_length=60)
    social1 = models.CharField('Social 1', max_length=50, blank=True)
    social_url1 = models.URLField('Social Url 1', blank=True)
    social2 = models.CharField('Social 2', max_length=50, blank=True)
    social_url2 = models.URLField('Social Url 2', blank=True)
    social3 = models.CharField('Social 3', max_length=50, blank=True)
    social_url3 = models.URLField('Social Url 3', blank=True)
    
    class Meta:
        
        verbose_name = 'Speakers Content'
        verbose_name_plural = 'Speakers Content'

    def __str__(self) -> str:
        return self.name

class Schedules(models.Model):

    left_title1 = models.CharField('Left Title 1', max_length=40)
    right_title1 = models.CharField('Right Title 1', max_length=40)
    img = models.ImageField('Background Image', upload_to='images')
    left_title2 = models.CharField('Left Title 2', max_length=40)
    right_title2 = models.CharField('Right Title 2', max_length=40)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)
        
    class Meta:
        
        verbose_name = 'Schedules'
        verbose_name_plural = 'Schedules'

class SchedulesCategories(models.Model):

    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=50)
    classname = models.CharField("Classname (Don't Change This)", max_length=30)
    
    class Meta:
        
        verbose_name = 'Schedules Categories'
        verbose_name_plural = 'Schedules Categories'

    def __str__(self) -> str:
        return self.title

class ScheldulesContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=60)
    text = models.TextField('Text')
    profile_img = models.ImageField('Profile Image', upload_to='images', blank=True)
    name = models.CharField('Name', max_length=50, blank=True)
    profession = models.CharField('Profession', max_length=50, blank=True)
    time = models.CharField('Time', max_length=50)
    place = models.CharField('Place', max_length=50)
    category = models.ForeignKey(SchedulesCategories, on_delete=models.CASCADE, related_name='cat_schedules')

class Pricing(models.Model):

    left_title = models.CharField('Left Title', max_length=40)
    right_title = models.CharField('Right Title', max_length=40)
    btn_name = models.CharField('Button Name', max_length=40)
        
    class Meta:
        
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing'


class PricingContent(models.Model):

    title = models.CharField('Title', max_length=50)
    price = models.FloatField('Price')
    offer1 = models.CharField('Offer 1', max_length=80)
    offer2 = models.CharField('Offer 2', max_length=80)
    offer3 = models.CharField('Offer 3', max_length=80)
    text = models.TextField('Text')

class Venue(models.Model):

    left_title = models.CharField('Left Title', max_length=40)
    right_title = models.CharField('Right Title', max_length=40)
    google_map = models.TextField('Google Map')
    title = models.CharField('Title', max_length=50)
    info1 = models.CharField('Info 1', max_length=80)
    info2 = models.CharField('Info 2', max_length=80)
    info3 = models.CharField('Info 3', max_length=80)

    class Meta:
    
        verbose_name = 'Venue'
        verbose_name_plural = 'Venue'

class ContactGet(models.Model):

    img = models.ImageField('Background Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    placeholder1 = models.CharField('Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Placeholder 2', max_length=50)
    placeholder3 = models.CharField('Placeholder 3', max_length=50)
    placeholder4 = models.CharField('Placeholder 4', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)
    

    class Meta:
    
        verbose_name = 'Contact GET'
        verbose_name_plural = 'Contact GET'

class ContactPost(models.Model):

    user_name = models.CharField('User Name', max_length=50)
    user_email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=80)
    message = models.TextField('Message')
    date = models.DateField('Date', auto_now=True)
    
    class Meta:
    
        verbose_name = 'Contact POST'
        verbose_name_plural = 'Contact POST'

class Footer(models.Model):

    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)
    subtitle3 = models.CharField('Subtitle 3', max_length=50)
    subtitle4 = models.CharField('Subtitle 4', max_length=50)
    social1 = models.CharField('Social 1', max_length=40)
    social_url1 = models.URLField('Social Url 1')
    social2 = models.CharField('Social 2', max_length=40)
    social_url2 = models.URLField('Social Url 2')
    social3 = models.CharField('Social 3', max_length=40)
    social_url3 = models.URLField('Social Url 3')
    social4 = models.CharField('Social 4', max_length=40)
    social_url4 = models.URLField('Social Url 4')
    copyright1 = models.TextField('Copyright 1')
    copyright2 = models.TextField('Copyright 2')
    design = models.CharField('Design', max_length=50)
    name = models.CharField('Name', max_length=50)
    name_link = models.URLField('Name Link')

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'