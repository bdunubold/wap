"""Urls for app a01."""
from django.conf.urls import url

from a01.views import HomeView

from a01.views import MovieDetailView
from a01.views import HallDetailView
from a01.views import ScreeningDetailView
from a01.views import CustomerDetailView
from a01.views import PaymentDetailView

from a01.views import MovieListView
from a01.views import HallListView
from a01.views import ScreeningListView
from a01.views import CustomerListView
from a01.views import PaymentListView



from a01.views import PaymentPayView
from a01.views import ScreeningByMovieView
from a01.views import LatestMoviesView





urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^movie/(?P<id>[0-9]+)/$', MovieDetailView.as_view(), name='moviedetail'),
    url(r'^hall/(?P<id>[0-9]+)/$', HallDetailView.as_view(), name='halldetail'),
    url(r'^screening/(?P<id>[0-9]+)/$', ScreeningDetailView.as_view(), name='screeningdetail'),
    url(r'^customer/(?P<id>[0-9]+)/$', CustomerDetailView.as_view(), name='customerdetail'),
    url(r'^payment/(?P<id>[0-9]+)/$', PaymentDetailView.as_view(), name='paymentdetail'),

    url(r'^movie/list/$', MovieListView.as_view(), name='movie'),
    url(r'^hall/list/$', HallListView.as_view(), name='hall'),
    url(r'^screening/list/$', ScreeningListView.as_view(), name='screening'),
    url(r'^customer/list/$', CustomerListView.as_view(), name='customer'),
    url(r'^payment/list/$', PaymentListView.as_view(), name='payment'),


    url(r'^screening/movie/(?P<id>[0-9]+)/$', ScreeningByMovieView.as_view(), name='payment_pay'),

    url(r'^payment/pay/$', PaymentPayView.as_view(), name='payment_pay'),
    url(r'^movie/latest/$', LatestMoviesView.as_view(), name='latest_movies'),


]
