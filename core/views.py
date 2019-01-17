from collections import namedtuple
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView

from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from django_tables2.paginators import LazyPaginator


from django.core.exceptions import ValidationError
from rest_framework import authentication, permissions, viewsets, filters
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework_tracking.models import APIRequestLog
from django_filters.rest_framework import DjangoFilterBackend
from .models import Consulta, ExameRealizado, Logdb
from .serializers import ConsultaSerializer, TrackSerializer, LogdbSerializer
from .tables import ConsultaTable, ExamesTable, LogdbTable
from .forms import ConsultaForm, ExameForm
from util.logapi import Log_api

log_api = Log_api()

class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""

    authentication_classes = (
         authentication.BasicAuthentication,
         authentication.TokenAuthentication,
    )
    permission_classes = (
         permissions.IsAuthenticated,
    )

    # authentication_classes = ()
    # permission_classes = ()

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class ConsultaListView(ListView):
    model = Consulta
    template_name = 'core/Consulta_list.html'
    context_object_name = 'Consulta'

    def get_context_data(self, **kwargs):
        context = super(ConsultaListView, self).get_context_data(**kwargs)
        table = ConsultaTable(Consulta.objects.all().order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table
        return context

class ExamesListView(ListView):
    model = ExameRealizado
    template_name = 'core/exame_list.html'
    context_object_name = 'ExameRealizado'

    def get_context_data(self, **kwargs):
        context = super(ExamesListView, self).get_context_data(**kwargs)
        table = ExamesTable(ExameRealizado.objects.all().order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table
        return context


class ConsultaViewSet(DefaultsMixin, LoggingMixin, viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    search_fields = ('numero_Consulta' )
    queryset = Consulta.objects.all()

    def get_queryset(self):
        queryset = Consulta.objects.all()
        num_Consulta = self.request.query_params.get('numero_Consulta', None)
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)
        empty = self.request.query_params.get('empty', None)

        if empty is not None:
            try:
                Consulta.objects.all().delete()
                raise ValidationError('Empty Ok')
            except Exception as e:
                print(e)

        if num_Consulta is not None:
            return queryset.filter(numero_Consulta=num_Consulta)
        elif limit is not None:
            return queryset[:int(limit)]
        elif last is not None:
            return queryset.order_by('-numero_Consulta')[:int(last)]

        return queryset


    def _perform(self, anterior):
        self.request.query_params._mutable = True
        self.request.query_params['user'] = self.request.user

        return  {"user_id": str(self.request.user), "numero_Consulta": self.request.POST.get("numero_Consulta"),
                "dados_atual": self.request.POST.get("dados_Consulta"),
                "dados_anterior": anterior}


    def perform_create(self, serializer):
        data = self._perform('')
        log_api.update_api(data)
        serializer.save()


    def perform_update(self, serializer):
        anterior = Consulta.objects.filter(numero_Consulta=self.request.POST.get('numero_Consulta'))[0].dados_Consulta
        data = self._perform(anterior)
        log_api.update_api(data)
        serializer.save()


class TrackingViewSet(DefaultsMixin, LoggingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = TrackSerializer
    search_fields = ('user','host', )
    queryset = APIRequestLog.objects.all()


    def get_queryset(self):
        queryset = APIRequestLog.objects.all()
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)

        if limit is not None:
            queryset = queryset[:int(limit)]
        elif last is not None:
            return queryset.order_by('-numero_Consulta')[:int(last)]
        return queryset


class LogPostsViewSet(DefaultsMixin, LoggingMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = LogdbSerializer
    queryset =Logdb.objects.all()

    def get_queryset(self):
        queryset = Logdb.objects.all()
        limit = self.request.query_params.get('limit', None)
        last = self.request.query_params.get('last', None)

        if limit is not None:
            queryset = queryset[:int(limit)]
        elif last is not None:
            return queryset[:int(last)]
        return queryset

class LogdbListView(ListView):
    model = Logdb
    template_name = 'core/log_posts_list.html'
    context_object_name = 'logdb'

    def get_context_data(self, **kwargs):
        context = super(LogdbListView, self).get_context_data(**kwargs)
        table = LogdbTable(Logdb.objects.all().order_by('-pk'))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


def _log_post(obj, before, rq):

    data = {"user_id": str(rq.user), "numero_Consulta": obj.numero_Consulta,
            "dados_atual": obj.dados_Consulta, "dados_anterior": before}
    log_api.update_api(data)


class ConsultaCreateView(CreateView):
    model = Consulta
    template_name = 'core/consulta-create.html'
    form_class = ConsultaForm
    success_url = '/consultas'

    def form_valid(self, form):
        structs = namedtuple('structs', 'dados_Consulta numero_Consulta id')
        d1 = form.cleaned_data
        obj = structs(dados_Consulta=d1['dados_Consulta'], numero_Consulta=d1['numero_Consulta'], id=str(d1['user']))

        _log_post(obj, "", self.request)
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class ConsultaUpdateView(UpdateView):
    model = Consulta
    template_name = 'core/consulta-create.html'
    form_class = ConsultaForm
    success_url = '/consultas'

    def form_valid(self, form,):
        before = Consulta.objects.filter(pk=self.object.id)[0]
        if not (before.dados_consulta == self.object.dados_consulta):

            print ('Objjjjject-->',self.object)
            _log_post(self.object, before.dados_consulta, self.request)

        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

class ExameUpdateView(UpdateView):
    model = ExameRealizado
    template_name = 'core/exame-create.html'
    form_class = ExameForm
    success_url = '/exames'

    def form_valid(self, form,):
        before = ExameRealizado.objects.filter(pk=self.object.id)[0]
        if not (before.numero_guia_consulta == self.object.numero_guia_consulta):

            _log_post(self.object, before.numero_guia_consulta, self.request)

        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

