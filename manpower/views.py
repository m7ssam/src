from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .models import Mp_list
from .forms import Mp_move, Mp_search
from .filters import Mp_list_Filter
# from django.db import IntegrityError
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# from django.db.models.query import QuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.core.cache import cache
from django.db.models import Q


@login_required()
def mp_home(request):
  return render(request, 'manpower/mp_home.html')


@login_required()
def user_page(request,pk):
  target_user = Mp_list.objects.get(id = pk)
  context = {"target_user": target_user}
  return render(request, "manpower/user_page.html", context)


class MpList(ListView):
  model = Mp_list
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    counter = Mp_list.objects.count()
    context['counter'] = counter
    return context
  # def get_queryset(self,filter) -> QuerySet[Any]:
  #   return Mp_list.objects.filter(title = filter)
  ordering = ["-id"]
  paginate_by = 200

# -------------------- جدول بيانات العمال
@login_required()
def mp_list(request):
  mp_list = Mp_list.objects.all()
  mp_list_filter = Mp_list_Filter(request.GET, queryset= mp_list)
  mp_list = mp_list_filter.qs
  page = request.GET.get('page', 1)
  paginator = Paginator(mp_list_filter.qs, 50)
  try:
    mp_list = paginator.page(page)
  except PageNotAnInteger:
    mp_list = paginator.page(1)
  except EmptyPage:
    mp_list = paginator.page(paginator.num_pages) 
  context = {
     "mp_list": mp_list,
     "filter": mp_list_filter,
              }
  return render(request, 'manpower/mp_list.html',context )
# --------------------


@login_required()
def mp_search(request):
  mp_list = Mp_list.objects.all()
  filter = Mp_list_Filter(request.GET, queryset=mp_list)
  mp_list = filter.qs
  context = {"filter": filter}
  return render(request, 'manpower/mp_search.html',context )

@login_required()
def mp_search_list(request):
  mp_list = Mp_list.objects.all()
  filter = Mp_list_Filter(request.GET, queryset=mp_list)
  mp_list = filter.qs
  context = {"mp_list": mp_list}
  return render(request, 'manpower/mp_list.html',context )





@login_required()
def error(request):
  return render(request, 'manpower/error.html')


@login_required()
def something_went_wrong(request):
  return render(request, 'manpower/something_went_wrong.html')


@login_required()
def created(request):
  return render(request, 'manpower/created.html')