from django.urls import path

from homepage.views import Home, plan, Contact, about, certificate, terms, privacy, blogdetails, blog

# blogdetails, blog,
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('blog/<slug>', blogdetails.as_view(), name='blog-details'),
    path('contact', Contact.as_view(), name='contact'),
    path('certificate', certificate, name='certificate'),
    path('plan', plan, name='plan'),
    path('terms', terms, name='terms'),
    path('privacy', privacy, name='privacy'),

]




