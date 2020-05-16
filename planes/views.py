from django.shortcuts import render,HttpResponse, redirect
from planes.models import Curator, FinanceCosts, Planning
from datetime import datetime as dt
import json
from .forms import PlanningForm

def plane(request):
    finance_costs = FinanceCosts.objects.all()
    # year = dt.now().year
    send_list = []
    money = None
    for item in finance_costs:
        try:
            money = item.with_planning.get(curator__title="ALL")
        except Planning.DoesNotExist:
            plan = Planning()
            plan.FinanceCosts = FinanceCosts.objects.get(pk = item.id)
            plan.curator = Curator.objects.get(title = "ALL")
            plan.q_1 = 0
            plan.q_2 = 0
            plan.q_3 = 0
            plan.q_4 = 0
            plan.year = dt.now().year
            plan.period = dt.now().date()
            plan.save()
            money = item.with_planning.get(curator__title="ALL")
        send_list.append([item, money])
    print(send_list)

    response = {"finance_costs": finance_costs,'send_list':send_list}
    return render(request, './planes/plane.html', response)



def curators(request, finance_cost_id):
    planning = Planning.objects.filter(FinanceCosts=finance_cost_id).exclude(curator__title='ALL')
    finance_cost_name = FinanceCosts.objects.get(pk=finance_cost_id).title
    response = {
        'planning': planning,
        'finance_cost_name': finance_cost_name,
        'finance_cost_id':finance_cost_id           
    }
    return render (request, './planes/curators.html', response)
# Create your views here.
def from_js(request):
    a = request.body.decode('utf-8')
    jsn = json.loads(a)
    try:
        result_curator = Curator.objects.get(title='ALL')
        id_result_curator = result_curator.id
    except Curator.DoesNotExist:
        print('error')
        result_curator = Curator()
        result_curator.title = 'ALL'
        result_curator.save()
        id_result_curator = result_curator.id


    finance_cost_title = jsn['cost_title']
    id_finance_cost = FinanceCosts.objects.get(title=finance_cost_title).id

    try:
        planing = Planning.objects.filter(FinanceCosts = id_finance_cost)
        result_cur = planing.get(curator__title='ALL')
    except Planning.DoesNotExist:
        plan = Planning()
        plan.FinanceCosts = FinanceCosts.objects.get(pk = id_finance_cost)
        plan.curator = Curator.objects.get(pk = id_result_curator)
        plan.q_1 = jsn['result_money'][0]
        plan.q_2 = jsn['result_money'][1]
        plan.q_3 = jsn['result_money'][2]
        plan.q_4 = jsn['result_money'][3]
        plan.year = dt.now().year
        plan.period = dt.now().date()
        plan.save()
        result_cur = planing.get(curator__title='ALL')
    
    if result_cur.q_1 != jsn['result_money'][0] : 
        result_cur.q_1 = jsn['result_money'][0]
        print('helo')
    if result_cur.q_2 != jsn['result_money'][1]:
        result_cur.q_2 = jsn['result_money'][1]
    if result_cur.q_3 != jsn['result_money'][2]:
        result_cur.q_3 = jsn['result_money'][2]
    if result_cur.q_4 != jsn['result_money'][3]:
        result_cur.q_4 = jsn['result_money'][3]
    result_cur.save()
    return HttpResponse('123')


def edit_plane(request, item_id):
    plan = Planning.objects.get(pk=item_id)
    plan_form = PlanningForm(instance=plan)
    response = {'plan_form':plan_form, 'item_id':item_id}
    print(request.POST)
    if(request.method == 'POST'):
        print('in post')
        plan_form = PlanningForm(request.POST, instance=plan)
        if plan_form.is_valid():
            if plan_form.cleaned_data.get('delete'):
                Planning.objects.get(pk=item_id).delete()
                return redirect(f'/plane/{str(plan.FinanceCosts.id)}/curators' ) 
            plan_form.save()
            return redirect(f'/plane/{str(plan.FinanceCosts.id)}/curators' )
    return render(request, './planes/edit_plane.html', response)

def add(request, finance_cost_id):
    plane_form = PlanningForm(initial={
        'FinanceCosts': finance_cost_id,
        'year': dt.now().year,
       'period':dt.now().date()
        })
    response = {
        'plane_form':plane_form,
        'finance_cost_id':finance_cost_id
    }
    if(request.method == 'POST'):
        plane_form = PlanningForm(request.POST)
        if plane_form.is_valid():
            plane_form.save()
            return redirect(f'/plane/{str(finance_cost_id)}/curators' )
    return render(request, './planes/add.html', response)