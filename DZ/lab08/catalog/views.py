from django.shortcuts import get_object_or_404, render
from .models import regard
from .models import Report

def index(request):
    regard_list = regard.objects.all()
    reports_1 = Report.objects.filter(regard_id=1)
    reports_2 = Report.objects.filter(regard_id=2)
    reports_3 = Report.objects.filter(regard_id=3)
    context = {'regard_list': regard_list, 'reports_1': reports_1, 'reports_2': reports_2, 'reports_3': reports_3 }
    return render(request, 'catalog/index.html', context)

def detail(request, mag_id):
    regard = regard.objects.get(id=mag_id)
    report_1 = Report.objects.get(regard_id=mag_id, quarter=2017)
    report_2 = Report.objects.get(regard_id=mag_id, quarter=2018)
    report_3 = Report.objects.get(regard_id=mag_id, quarter=2019)
    report_4 = Report.objects.get(regard_id=mag_id, quarter=2020)
    report_profit_sum = report_1.profit + report_2.profit + report_3.profit + report_4.profit

    context = {'regard': regard, 'report_1': report_1, 'report_2': report_2, 'report_3': report_3, 'report_4': report_4, 'report_profit_sum': report_profit_sum }
    return render(request, 'catalog/detail.html', context)
