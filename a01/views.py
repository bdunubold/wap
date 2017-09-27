
import json
import datetime

from django.db import models

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.core import serializers
from django.core.serializers import serialize
# Create your views here.


from django.views import View
from django.views.generic import TemplateView

from django.http import JsonResponse
from django.http import HttpResponse

from a01.models import Customer
from a01.models import Hall
from a01.models import Movie
from a01.models import Payment
from a01.models import Screening


class HomeView(TemplateView):

    template_name = 'a01/home.html'

    def get_context_data(self, **kwargs):
        """Context data."""
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


################################################################################
# DETAIL VIEWS


class DetailView(View):
    get_class = None

    def get(self, req, id):
        obj = get_object_or_404(self.get_class, pk=id)

        json_data = serializers.serialize('json', [obj, ])

        return HttpResponse(json_data, content_type='json')


class MovieDetailView(DetailView):
    get_class = Movie


class HallDetailView(DetailView):
    get_class = Hall


class ScreeningDetailView(DetailView):
    get_class = Screening


class CustomerDetailView(DetailView):
    get_class = Customer


class PaymentDetailView(DetailView):
    get_class = Payment

################################################################################
# DETAIL VIEWS


class ListView(View):
    get_class = None

    def get(self, *args):
        obj_list = self.get_class.objects.all()
        json_data = serializers.serialize('json', obj_list)

        return HttpResponse(json_data, content_type='json')


class MovieListView(ListView):
    get_class = Movie


class HallListView(ListView):
    get_class = Hall


class ScreeningListView(ListView):
    get_class = Screening


class CustomerListView(ListView):
    get_class = Customer


class PaymentListView(ListView):
    get_class = Payment


class TicketOrder(View):

    def post(self):
        pass


class PaymentPayView(View):
    def post(self, request):
        screening_id = request.POST.get('screening_id')
        cardnum = request.POST.get('cardnum')
        email = request.POST.get('email')
        startdate = request.POST.get('startdate')
        expdate = request.POST.get('expdate')

        total_seats = request.POST.get('total_seats')
        sendseats = request.POST.get('seats')
        userseats = request.POST.get('userseats')

        sendseats = json.loads(sendseats)
        userseats = json.loads(userseats)

        screen = get_object_or_404(Screening, pk=screening_id)
        screen.totalcustomer += int(total_seats)
        screen.seats = sendseats
        screen.save()

        customer = Customer()
        customer.email = email
        customer.screen = screen
        customer.seats = int(total_seats)
        customer.bseats = userseats
        customer.save()

        payment = Payment()
        payment.customer = customer
        payment.cardnum = cardnum
        payment.startdate = startdate
        payment.expdate = expdate
        payment.save()

        return HttpResponse({'msg': 'Payment is completed'}, content_type='json')



class ScreeningReserveView(View):
    def post(self, request):
        pdata = request.POST


        screen = get_object_or_404(Screening, pk=pdata.get('screen_id'))
        customer = Customer()
        customer.screen = screen
        customer.email = pdata.get('email')
        customer.seats = pdata.get('seats')
        customer.bseats = pdata.get('bseats')
        customer.save()

        return HttpResponse(content_type="application/json", status_code=200)


class ScreeningByMovieView(View):
    def get(self, req, id):
        obj = get_object_or_404(Movie, pk=id)
        screens = Screening.objects.filter(movie=obj)
        json_data = serializers.serialize('json', screens)
        return HttpResponse(json_data, content_type='json')
