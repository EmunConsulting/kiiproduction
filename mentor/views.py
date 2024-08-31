from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from program.models import ProgramPlanner
from .ment_deco import update_record, create_record, delete_record, new_mentor

from .models import MentorList, Mentorship, MentorComRec
from .forms import MentorListForm, MentorshipForm, MentorComRecForm
from program.models import ProgramPlanner
# Create your views here.


def mentors_list(request):
    men_lis = MentorList.objects.all()
    return render(request, 'mentors_list.html', {'men_lis': men_lis})


@new_mentor(MentorList, MentorListForm, 'mentors_list_form.html', 'mentors_list', redirect_id=None)
def create_mentor(request):
    pass


@update_record(MentorList, MentorListForm, 'mentors_list_form.html', 'mentors_list', redirect_id=None)
def update_mentor(request, pk):
    pass


@delete_record(MentorList, 'mentors_list', redirect_id=None)
def delete_mentor(request, pk):
    pass


def assign_mentor(request, mentee, program):
    # Get the user and program instances
    user_instance = get_object_or_404(User, pk=mentee)
    program_instance = get_object_or_404(ProgramPlanner, pk=program)

    if request.method == 'POST':
        form = MentorshipForm(request.POST)
        if form.is_valid():
            mentorship = form.save(commit=False)
            mentorship.user = user_instance  # Assign the user instance
            mentorship.program = program_instance  # Assign the program instance
            mentorship.save()
            # Redirect or handle success scenario
            return redirect('approved_attendees_list', pk=program)
    else:
        # Pre-fill the form with the mentee and program instances
        form = MentorshipForm(initial={'user': user_instance, 'program': program_instance})

    return render(request, 'assign_mentor_form.html', {'form': form})


def show_mentor(request, mentee, program):
    # Get the user and program instances
    user_instance = get_object_or_404(User, pk=mentee)
    program_instance = get_object_or_404(ProgramPlanner, pk=program)
    rec = Mentorship.objects.filter(user=user_instance, program=program_instance)

    return render(request, 'show_mentor.html', {
        'rec': rec,
    })


@update_record(Mentorship, MentorshipForm, 'assign_mentor_form.html', 'planned_program_list', redirect_id=None)
def update_mentorship(request, pk):
    pass


@delete_record(Mentorship, 'planned_program_list', redirect_id=None)
def delete_mentorship(request, pk):
    pass
