from django.shortcuts import render
from hr.models import Employee
from OA.models import Project
# Create your views here.
def index(request):
    #Employee_list = Employee.objects.order_by('-user_workcode')
    emp = Employee.objects.all()
    emp_count = emp.count()
    Project_list = Project.objects.order_by('proj_code')
    #order_by('-user_workcode')[:5]
    sd = Employee.objects.filter(user_position="SD")
    cc =Employee.objects.filter(user_position="CC")
    cr =Employee.objects.filter(user_position="CR")
    dos =Employee.objects.filter(user_position="DOS")
    asd =Employee.objects.filter(user_position="ASD")
    ccs =Employee.objects.filter(user_position="CCS")
    ccm =Employee.objects.filter(user_position="CCM")
    crs =Employee.objects.filter(user_position="CCS")
    tr =Employee.objects.filter(user_position__iregex="TR")

    sd_c = sd.count()
    cc_c = cc.count()
    cr_c = cr.count()
    dos_c= dos.count()
    asd_c= asd.count()
    ccs_c= ccs.count()
    ccm_c= ccm.count()
    crs_c= crs.count()
    tr_c=tr.count()



    context_dict = {'projects':Project_list,
                    'emp_count':emp_count,
                    'sd_c':sd_c,
                    'cc_c':cc_c,
                    'cr_c':cr_c,
                    'dos_c':dos_c,
                    'asd_c':asd_c,
                    'ccs_c':ccs_c,
                    'ccm_c':ccm_c,
                    'crs_c':crs_c,
                    'tr_c':tr_c,
                    }


    return render(request, 'hr/index.html', context_dict)

def school(request, user_school_id):
    context_dict = {}
    try:
        projects = Project.objects.get(pk=user_school_id)
        context_dict['project_name']=projects.Proj_name
        employee = Employee.objects.filter(user_school=projects)
        context_dict['employee']=employee
        context_dict['projects']=projects

    except projects.DoesNotExist:
        pass

    return render(request, 'hr/emp_detail.html', context_dict)
'''
def statistics(request):
    emp = Employee.objects.all()
    sd = Employee.objects.filter(user_position="SD")
    cc =Employee.objects.filter(user_position="CC")
    cr =Employee.objects.filter(user_position="CR")
    dos =Employee.objects.filter(user_position="DOS")
    asd =Employee.objects.filter(user_position="ASD")
    ccs =Employee.objects.filter(user_position="CCS")
    ccm =Employee.objects.filter(user_position="CCM")
    crs =Employee.objects.filter(user_position="CCS")

    emp_count= emp.count()

    context_dict={'emp_count':emp_count}


    return render(request, 'hr/index.html', context_dict)
'''