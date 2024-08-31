from django.contrib import messages
from django.shortcuts import render, redirect
from .business_deco import update_record, create_record, delete_record
from .models import ServicesProductsList, RegistrationStatusList, DevelopmentStageList, IndustrySectorList, BusinessRecord, OutcomeRecord
from .forms import ServicesProductsListForm, RegistrationStatusListForm, DevelopmentStageListForm, \
    IndustrySectorListForm, BusinessRecordForm, OutcomeRecordForm


# Services or Products

def service_products_list(request):
    rec_list = ServicesProductsList.objects.all()
    return render(request, 'service_products_list.html', {'rec_list': rec_list})


@create_record(ServicesProductsList, ServicesProductsListForm, 'service_products_form.html', 'service_products_list', redirect_id=None)
def create_service_products(request):
    pass


@update_record(ServicesProductsList, ServicesProductsListForm, 'service_products_form.html', 'service_products_list', redirect_id=None)
def update_service_products(request, pk):
    pass


@delete_record(ServicesProductsList, 'service_products_list', redirect_id=None)
def delete_service_products(request, pk):
    pass


# Registration Status

def registration_status_list(request):
    rec_list = RegistrationStatusList.objects.all()
    return render(request, 'registration_status_list.html', {'rec_list': rec_list})


@create_record(RegistrationStatusList, RegistrationStatusListForm, 'registration_status_form.html', 'registration_status_list', redirect_id=None)
def create_registration_status(request):
    pass


@update_record(RegistrationStatusList, RegistrationStatusListForm, 'registration_status_form.html', 'registration_status_list', redirect_id=None)
def update_registration_status(request, pk):
    pass


@delete_record(RegistrationStatusList, 'registration_status_list', redirect_id=None)
def delete_registration_status(request, pk):
    pass


# Development Stage

def development_stage_list(request):
    rec_list = DevelopmentStageList.objects.all()
    return render(request, 'development_stage_list.html', {'rec_list': rec_list})


@create_record(DevelopmentStageList, DevelopmentStageListForm, 'development_stage_form.html', 'development_stage_list', redirect_id=None)
def create_development_stage(request):
    pass


@update_record(DevelopmentStageList, DevelopmentStageListForm, 'development_stage_form.html', 'development_stage_list', redirect_id=None)
def update_development_stage(request, pk):
    pass


@delete_record(DevelopmentStageList, 'development_stage_list', redirect_id=None)
def delete_development_stage(request, pk):
    pass


# Industry Sector

def industry_sector_list(request):
    rec_list = IndustrySectorList.objects.all()
    return render(request, 'industry_sector_list.html', {'rec_list': rec_list})


@create_record(IndustrySectorList, IndustrySectorListForm, 'industry_sector_form.html', 'industry_sector_list', redirect_id=None)
def create_industry_sector(request):
    pass


@update_record(IndustrySectorList, IndustrySectorListForm, 'industry_sector_form.html', 'industry_sector_list', redirect_id=None)
def update_industry_sector(request, pk):
    pass


@delete_record(IndustrySectorList, 'industry_sector_list', redirect_id=None)
def delete_industry_sector(request, pk):
    pass


# Business Record

def business_list(request):
    rec_list = BusinessRecord.objects.filter(user=request.user)
    out_list = OutcomeRecord.objects.all()
    return render(request, 'business_list.html', {
        'rec_list': rec_list,
        'out_list': out_list,
    })


def create_business(request):
    # Get the user and program instances
    user = request.user

    if request.method == 'POST':
        form = BusinessRecordForm(request.POST)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.user = user
            rec.save()
            # Redirect or handle success scenario
            return redirect('business_list')
    else:
        # Pre-fill the form with user
        form = BusinessRecordForm(initial={'user': user})

    return render(request, 'business_form.html', {'form': form})


@update_record(BusinessRecord, BusinessRecordForm, 'business_form.html', 'business_list', redirect_id=None)
def update_business(request, pk):
    pass


@delete_record(BusinessRecord, 'business_list', redirect_id=None)
def delete_business(request, pk):
    pass


# Outcome Record

def outcome_record_list(request, pk):
    rec_list = OutcomeRecord.objects.get(business_record=pk)
    return render(request, 'outcome_record_list.html', {'rec_list': rec_list})


def create_outcome_record(request, pk):
    try:
        # Get the BusinessRecord instance using the pk
        business_record = BusinessRecord.objects.get(pk=pk)
    except BusinessRecord.DoesNotExist:
        messages.error(request, 'The business record does not exist.')
        return redirect('business_list')  # Redirect if record does not exist

    if request.method == 'POST':
        form = OutcomeRecordForm(request.POST)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.business_record = business_record  # Assign the instance, not the pk
            rec.save()
            messages.success(request, 'Outcome record created successfully.')
            return redirect('business_list')
    else:
        # Pre-fill the form with the BusinessRecord instance
        form = OutcomeRecordForm(initial={'business_record': business_record})

    return render(request, 'outcome_record_form.html', {'form': form})


@update_record(OutcomeRecord, OutcomeRecordForm, 'outcome_record_form.html', 'business_list', redirect_id=None)
def update_outcome_record(request, pk):
    pass


@delete_record(OutcomeRecord, 'business_list', redirect_id=None)
def delete_outcome_record(request, pk):
    pass

