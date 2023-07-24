from django.urls import path
from .views.signup import Signup
from .views.index import Index
from .views.signin import Signin, logout
from .views.about import About
from .views.contact import Contact
from .views.faq import Faq
from .views.privacy_policy import Privacy_Policy
from .views.products_details import Products_Details
from .views.blog_details import Blog_Details
from .views.blog_grid import Blog_Grid
from .views.shop_grid import Shop_Grid
from .views.terms_conditions import Terms_Conditions
from .views.checkout import Checkout
from .views.cart import Cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    #login authentication
    path('signup', Signup.as_view(), name='signup'),
    path('signin', Signin.as_view(), name='signin'),
    path('logout', logout, name='logout'),


    path('about', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('faq', Faq.as_view(), name='faq'),
    path('privacy-policy', Privacy_Policy.as_view(), name='privacy-policy'),
    path('products-details/<int:pk>', Products_Details.as_view(), name='products-details'),
    path('blog-details', Blog_Details.as_view(), name='blog-details'),
    path('blog-grid', Blog_Grid.as_view(), name='blog-grid'),
    path('shop-grid/<str:category>/', Shop_Grid.as_view(), name='shop-grid'),
    path('terms-conditions', Terms_Conditions.as_view(), name='terms-conditions'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('cart/<int:pk>', Cart.as_view(), name='cart')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
