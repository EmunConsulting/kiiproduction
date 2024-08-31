import datetime

from django.http import request
from django.shortcuts import render
from django.utils import timezone

from mentor.models import Mentorship
from .program_deco import update_record, create_record, delete_record
from .models import ProgramPlanner, ProgramList, ProgramCategoryList
from .forms import ProgramCategoryListForm, ProgramListForm, ProgramPlannerForm
from application.models import Application

# Create your views here.


def program_category_list(request):

    pro_cat_lis = ProgramCategoryList.objects.all()

    return render(request, 'program_category_list.html', {'pro_cat_lis': pro_cat_lis})


@create_record(ProgramCategoryList, ProgramCategoryListForm, 'program_category_form.html', 'program_category_list', redirect_id=None)
def create_program_category(request):
    pass


@update_record(ProgramCategoryList, ProgramCategoryListForm, 'program_category_form.html', 'program_category_list', redirect_id=None)
def update_program_category(request, pk):
    pass


@delete_record(ProgramCategoryList, 'program_category_list', redirect_id=None)
def delete_program_category(request, pk):
    pass


def program_list(request):

    programs = ProgramList.objects.all()

    return render(request, 'program_list.html', {'programs': programs})


@create_record(ProgramList, ProgramListForm, 'program_list_form.html', 'program_list', redirect_id=None)
def create_program_list(request):
    pass


@update_record(ProgramList, ProgramListForm, 'program_list_form.html', 'program_list', redirect_id=None)
def update_program_list(request, pk):
    pass


@delete_record(ProgramList, 'program_list', redirect_id=None)
def delete_program_list(request, pk):
    pass


def planned_program_list(request):
    pla_pro = ProgramPlanner.objects.all()
    return render(request, 'planned_program_list.html', {'pla_pro': pla_pro})


def approved_attendees_list(request, pk):
    app_att = Application.objects.filter(approved=True, program=pk)
    mentors = Mentorship.objects.filter(program=pk)
    return render(request, 'approved_attendees_list.html', {
        'app_att': app_att,
        'mentors': mentors,
    })


def events_list(request):
    app = Application.objects.filter(user=request.user)
    pla_pro = ProgramPlanner.objects.all()
    current_day = timezone.now().date()
    return render(request, 'events_list.html', {
        'pla_pro': pla_pro,
        'current_day': current_day,
        'app': app,
    })


def current_events_list(request):
    current_day = timezone.now().date()
    pla_pro = ProgramPlanner.objects.filter(end_date__gte=timezone.now())
    app = Application.objects.filter(user=request.user)

    return render(request, 'events_list.html', {
        'pla_pro': pla_pro,
        'current_day': current_day,
        'app': app,
    })


@create_record(ProgramPlanner, ProgramPlannerForm, 'program_planner_form.html', 'planned_program_list', redirect_id=None)
def create_program(request):
    pass


@update_record(ProgramPlanner, ProgramPlannerForm, 'program_planner_form.html', 'planned_program_list', redirect_id=None)
def update_program(request, pk):
    pass


@delete_record(ProgramPlanner, 'planned_program_list', redirect_id=None)
def delete_program(request, pk):
    pass
