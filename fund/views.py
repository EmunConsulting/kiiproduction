from django.shortcuts import render
from .fund_deco import update_record, create_record, delete_record
from .models import FundTypeList, FundRecord, InvestorTypeList, InvestorRecord, InvestmentRecord
from .forms import FundTypeListForm, FundRecordForm, InvestorTypeListForm, InvestorRecordForm
# Create your views here.


# Fund Type

def fund_type_list(request):
    rec_list = FundTypeList.objects.all()
    return render(request, 'fund_type_list.html', {'rec_list': rec_list})


@create_record(FundTypeList, FundTypeListForm, 'fund_type_form.html', 'fund_type_list', redirect_id=None)
def create_fund_type(request):
    pass


@update_record(FundTypeList, FundTypeListForm, 'fund_type_form.html', 'fund_type_list', redirect_id=None)
def update_fund_type(request, pk):
    pass


@delete_record(FundTypeList, 'fund_type_list', redirect_id=None)
def delete_fund_type(request, pk):
    pass


# Fund Record

def fund_record_list(request):
    rec_list = FundRecord.objects.all()
    return render(request, 'fund_record_list.html', {'rec_list': rec_list})


def fund_record_detail(request, pk):
    rec_list = FundRecord.objects.get(id=pk)
    return render(request, 'fund_record_detail.html', {'rec_list': rec_list})


@create_record(FundRecord, FundRecordForm, 'fund_record_form.html', 'fund_record_list', redirect_id=None)
def create_fund_record(request):
    pass


@update_record(FundRecord, FundRecordForm, 'fund_record_form.html', 'fund_record_list', redirect_id=None)
def update_fund_record(request, pk):
    pass


@delete_record(FundRecord, 'fund_record_list', redirect_id=None)
def delete_fund_record(request, pk):
    pass


# Investor Type

def investor_type_list(request):
    rec_list = InvestorTypeList.objects.all()
    return render(request, 'investor_type_list.html', {'rec_list': rec_list})


@create_record(InvestorTypeList, InvestorTypeListForm, 'investor_type_form.html', 'investor_type_list', redirect_id=None)
def create_investor_type(request):
    pass


@update_record(InvestorTypeList, InvestorTypeListForm, 'investor_type_form.html', 'investor_type_list', redirect_id=None)
def update_investor_type(request, pk):
    pass


@delete_record(InvestorTypeList, 'investor_type_list', redirect_id=None)
def delete_investor_type(request, pk):
    pass


# Investor Record

def investor_record_list(request):
    rec_list = InvestorRecord.objects.all()
    return render(request, 'investor_record_list.html', {'rec_list': rec_list})


@create_record(InvestorRecord, InvestorRecordForm, 'investor_record_form.html', 'investor_record_list', redirect_id=None)
def create_investor_record(request):
    pass


@update_record(InvestorRecord, InvestorRecordForm, 'investor_record_form.html', 'investor_record_list', redirect_id=None)
def update_investor_record(request, pk):
    pass


@delete_record(InvestorRecord, 'investor_record_list', redirect_id=None)
def delete_investor_record(request, pk):
    pass
