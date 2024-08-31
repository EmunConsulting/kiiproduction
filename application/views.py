from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from program.models import ProgramPlanner
from .app_deco import update_record, create_record, delete_record

from .models import Application
from .forms import ApplicationForm

# Create your views here.


def pending_application_list(request):
    app_lis = Application.objects.filter(approved=False)
    return render(request, 'application_list.html', {'app_lis': app_lis})


def application_list(request):
    app_lis = Application.objects.all()
    return render(request, 'application_list.html', {'app_lis': app_lis})


def create_application(request, pk=None):
    # Get the program based on the provided pk
    program = get_object_or_404(ProgramPlanner, pk=pk)

    # Create a new Application directly
    application = Application.objects.create(
        user=request.user,
        program=program
    )
    # Optionally add a success message
    messages.success(request, 'Application submitted successfully.')

    # Redirect to the events list or any other page
    return redirect('events_list')


def approve_application(request, pk):
    # Get the program based on the provided pk
    app = get_object_or_404(Application, id=pk)

    # set Approved to True
    app.approved = True
    app.save()

    # Optionally add a success message
    messages.success(request, 'Application approved.')

    # Redirect to the events list or any other page
    return redirect('pending_application_list')


@update_record(Application, ApplicationForm, 'application_form.html', 'application_list', redirect_id=None)
def update_application(request, pk):
    pass


@delete_record(Application, 'application_list', redirect_id=None)
def delete_application(request, pk):
    pass


@delete_record(Application, 'events_list', redirect_id=None)
def delete_application_user(request, pk):
    pass
