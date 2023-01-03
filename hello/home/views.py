from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime,timedelta 
from home.models import basetable,vendor_table,project_table,expired_table
from django.contrib import messages
from django.contrib.auth.models import User,auth,Group
from django.contrib.auth import logout,authenticate,login
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django import template

#global_object_basetable=basetable.objects.none()


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    total_PO=basetable.objects.all().count()
    startdate_search = datetime.today()
    enddate_search = startdate_search + timedelta(days=30)
    expired_PO=basetable.objects.filter(enddate__lt=startdate_search).count()
    PO_30days=basetable.objects.filter(enddate__range=[startdate_search,enddate_search]).count()
    danger_PO_not_raised=allpo_search=basetable.objects.filter(PR=None,enddate__range=[startdate_search,enddate_search]).count()
    danger_PO_raised=PO_30days-danger_PO_not_raised
    if PO_30days==0:
        PO_30days_percentage_temp=0
    else:    
        PO_30days_percentage_temp=(danger_PO_raised/PO_30days)*100
    PO_30days_percentage=float("{:.2f}".format(PO_30days_percentage_temp))
    enddate_search = startdate_search + timedelta(days=90)
    PO_90days=basetable.objects.filter(enddate__range=[startdate_search,enddate_search]).count()
    PR_not_raised=allpo_search=basetable.objects.filter(PR=None,enddate__range=[startdate_search,enddate_search]).count()
    print(PR_not_raised)
    PR_raised=PO_90days - PR_not_raised
    if PO_90days==0:
        PO_90days_percentage_temp=0
    else:
        PO_90days_percentage_temp=(PR_raised/PO_90days)*100
    PO_90days_percentage=float("{:.2f}".format(PO_90days_percentage_temp))
    #print(total_PO)
    context = {
        "total_PO" : total_PO,
        "expired_PO" : expired_PO,
        "PO_30days"  : PO_30days,
        "PO_90days"  : PO_90days,
        "PR_raised": PR_raised,
        "danger_PO_not_raised":danger_PO_not_raised,
        "PO_30days_percentage":PO_30days_percentage,
        "PO_90days_percentage":PO_90days_percentage,
    }
    #messages.info(request, 'welcome {{%request.user %}} to AMC Management System')
    return render(request,'index.html',context)
    #return HttpResponse("This is HomePage")

def CL(request):
    #return HttpResponse("This is Your Critical List")
    return render(request,'CL.html')

def update(request):
    update_search_PO=request.POST.get('update_search_PO')
    global global_search_PO_update 
    global_search_PO_update=update_search_PO
    global_search_PO=update_search_PO
    print("Update Search_PO=")
    print(update_search_PO)
    if request.method=="POST":
        try :
            #edit_obj=basetable.objects.filter(PO='search_PO')
            basetable.objects.get(PO=update_search_PO)
            return redirect("update_internal")
        except ObjectDoesNotExist:
            messages.error(request, 'Entry Not Found')

    return render(request,'update.html')

def update_internal(request):
    print("Here Success update Internal Edit")
    print("global Search_PO update=")
    print(global_search_PO_update)
    eio_update=basetable.objects.get(PO=global_search_PO_update)
    print(eio_update.PO)
    if 'cancel_button' in request.POST:
        print("In Cancel")
        return redirect("/update")
    elif 'submit_button' in request.POST:
        eio_update.BC1=request.POST.get('BC1')
        eio_update.BC2=request.POST.get('BC2')
        eio_update.BC3=request.POST.get('BC3')
        eio_update.BC4=request.POST.get('BC4')
        eio_update.PMC1=request.POST.get('PMC1')
        eio_update.PMC2=request.POST.get('PMC2')
        eio_update.PMC3=request.POST.get('PMC3')
        eio_update.PMC4=request.POST.get('PMC4')
        #new=basetable(project_id=project,vendor_id=vendor,PO=PO,oldPO=oldPO,typePO=typePO,desc=desc,price=price,startdate=startdate,enddate=enddate,BC=BC,PMC=PMC,PR=PR,PRdate=PRdate)
        eio_update.save()
        messages.success(request, 'VOILA!!!PO Status Updated Succesfully!')
        return redirect("/update")

    
    return render(request,'update_internal.html',{"basetable":eio_update})


def new(request):
    #return HttpResponse("This is New")
    projectobj=project_table.objects.all()
    vendorobj=vendor_table.objects .all()
    """if 'check_button' in request.POST:
        project=request.POST['project']
        vendor=request.POST['vendor']
        PO=request.POST.get('PO')
        oldPO=request.POST.get('oldPO')
        typePO=request.POST.get('typePO')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        
        if enddate<startdate:
            messages.error(request, 'Startdate is higher than enddate')
        if PO=='':
            messages.error(request, 'PO is mandatory')
        if project=="0" or vendor=="0":
            messages.error(request, 'Please select valid Project and vendor name')
        else:
            try :
            #edit_obj=basetable.objects.filter(PO='search_PO')
                basetable.objects.get(PO=PO)
                messages.error(request, 'PO allready Exists!')
            except ObjectDoesNotExist:
                messages.success(request, 'PO entries are valid Please Proceed')
    
    elif 'submit_button' in request.POST:

    elif 'cancel_button' in request.POST:
        """
    if request.method=="POST":
        project=request.POST['project']
        vendor=request.POST['vendor']
        PO=request.POST.get('PO')
        oldPO=request.POST.get('oldPO')
        typePO=request.POST.get('typePO')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        

        if enddate<startdate:
            messages.error(request, 'OOPS!! Startdate is higher than enddate. Kindly Re-submit with End date higher than start date')
        elif PO=='':
            messages.error(request, 'OOPS!! PO is mandatory. Kindly Re-submit with an Unique PO Number')
        elif project=="0" or vendor=="0":
            messages.error(request, 'Please select valid Project and Vendor name')
        else:
            try :
            #edit_obj=basetable.objects.filter(PO='search_PO')
                basetable.objects.get(PO=PO)
                messages.error(request, 'OOPS!! PO allready Exists. Kindly Re-submit with an Unique PO Number')
            except ObjectDoesNotExist:
                new=basetable(project_id=project,vendor_id=vendor,PO=PO,oldPO=oldPO,typePO=typePO,desc=desc,price=price,startdate=startdate,enddate=enddate)
                new.save()
                messages.success(request, 'VOILA!!!New PO entered Succesfully!')
    return render(request,'new.html',{"project_table":projectobj,"vendor_table":vendorobj})

def edit(request):
    search_PO=request.POST.get('search_PO')
    global global_search_PO 
    global_search_PO=search_PO
    global_search_PO_update=search_PO
    print("Search_PO=")
    print(search_PO)
    if request.method=="POST":
        try :
            #edit_obj=basetable.objects.filter(PO='search_PO')
            basetable.objects.get(PO=search_PO)
            return redirect("edit_internal")
        except ObjectDoesNotExist:
            print("yes i am here")
            messages.error(request, 'Entry Not Found')
    return render(request,'edit.html')

def edit_internal(request):
    projectobj=project_table.objects.all()
    vendorobj=vendor_table.objects .all()
    print("Here Success Internal Edit")
    print("global Search_PO=")
    print(global_search_PO)
    eio=basetable.objects.get(PO=global_search_PO)
    print(eio.PO)
    if 'cancel_button' in request.POST:
        print("In Cancel")
        messages.info(request, 'Ohh Snapp!!!!You Didnt made any changes')
        return redirect("/edit")
    elif 'submit_button' in request.POST:
        eio.project_id=request.POST['project']
        eio.vendor_id=request.POST['vendor']
       # eio.PO=request.POST.get('PO')
        eio.oldPO=request.POST.get('oldPO')
        eio.typePO=request.POST.get('typePO')
        eio.desc=request.POST.get('desc')
        eio.price=request.POST.get('price')
        eio.startdate=request.POST.get('startdate')
        eio.enddate=request.POST.get('enddate')
        eio.BC1=request.POST.get('BC1')
        eio.BC2=request.POST.get('BC2')
        eio.BC3=request.POST.get('BC3')
        eio.BC4=request.POST.get('BC4')
        eio.PMC1=request.POST.get('PMC1')
        eio.PMC2=request.POST.get('PMC2')
        eio.PMC3=request.POST.get('PMC3')
        eio.PMC4=request.POST.get('PMC4')
        eio.PR=request.POST.get('PR')
        PRdate_form=request.POST.get('PRdate')
        if PRdate_form=="":
            print("Empty PR Date")
        else:
            eio.PRdate=PRdate_form
            
        #cr_date = '2013-10-31 18:23:29.000227'
        #cr_date = datetime.datetime.strptime(cr_date, '%Y-%m-%d %H:%M:%S.%f')
        #cr_date = cr_date.strftime("%m/%d/%Y")
        #formatDate_PR=PRdate_form.strftime("%Y-%m-%d")
        #eio.PRdate=formatDate_PR
        #new=basetable(project_id=project,vendor_id=vendor,PO=PO,oldPO=oldPO,typePO=typePO,desc=desc,price=price,startdate=startdate,enddate=enddate,BC=BC,PMC=PMC,PR=PR,PRdate=PRdate)
        eio.save()
        messages.success(request, 'VOILA!!!PO Updated Succesfully!')
        return redirect("/edit")
    elif 'expire_button' in request.POST:
        print("cabinet Entries")
        expired_project=request.POST['project']
        expired_vendor=request.POST['vendor']
        expired_PO=eio.PO
        expired_oldPO=request.POST.get('oldPO')
        expired_typePO=request.POST.get('typePO')
        expired_desc=request.POST.get('desc')
        expired_price=request.POST.get('price')
        expired_startdate=request.POST.get('startdate')
        expired_enddate=request.POST.get('enddate')
        expired_BC1=request.POST.get('BC1')
        expired_BC2=request.POST.get('BC2')
        expired_BC3=request.POST.get('BC3')
        expired_BC4=request.POST.get('BC4')
        expired_PMC1=request.POST.get('PMC1')
        expired_PMC2=request.POST.get('PMC2')
        expired_PMC3=request.POST.get('PMC3')
        expired_PMC4=request.POST.get('PMC4')
        expired_PR=request.POST.get('PR')
        expired_PRdate=request.POST.get('PRdate')
        if expired_PRdate=="":
            print("Empty PR Date")
            expired_new=expired_table(project_id=expired_project,vendor_id=expired_vendor,PO=expired_PO,oldPO=expired_oldPO,typePO=expired_typePO,desc=expired_desc,price=expired_price,startdate=expired_startdate,enddate=expired_enddate,BC1=expired_BC1,BC2=expired_BC2,BC3=expired_BC3,BC4=expired_BC4,PMC1=expired_PMC1,PMC2=expired_PMC2,PMC3=expired_PMC3,PMC4=expired_PMC4,PR=expired_PR)
        else:
            expired_new=expired_table(project_id=expired_project,vendor_id=expired_vendor,PO=expired_PO,oldPO=expired_oldPO,typePO=expired_typePO,desc=expired_desc,price=expired_price,startdate=expired_startdate,enddate=expired_enddate,BC1=expired_BC1,BC2=expired_BC2,BC3=expired_BC3,BC4=expired_BC4,PMC1=expired_PMC1,PMC2=expired_PMC2,PMC3=expired_PMC3,PMC4=expired_PMC4,PR=expired_PR,PRdate=expired_PRdate)
        expired_new.save()
        messages.success(request, 'PO Send to cabinet Succesfully, Please check the entry in Cabinet table!')
        eio.delete()
        print("deleted")
        messages.success(request, 'PO from Main Table Deleted Succesfully!')
        return redirect("/expired_edit")
    elif 'delete_button' in request.POST:
        eio.delete()
        print("deleted")
        messages.success(request, 'PO Deleted Succesfully!')
        return redirect("/expired_edit")
    
    
    return render(request,'edit_internal.html',{"basetable":eio,"project_table":projectobj,"vendor_table":vendorobj})



def expired_edit(request):
    expired_search_PO=request.POST.get('expired_search_PO')
    global expired_global_search_PO 
    expired_global_search_PO=expired_search_PO
    global_search_PO_update=expired_search_PO
    global_search_PO=expired_global_search_PO
    print("expired_Search_PO=")
    print(expired_search_PO)
    if request.method=="POST":
        try :
            #edit_obj=basetable.objects.filter(PO='search_PO')
            expired_table.objects.get(PO=expired_search_PO)
            return redirect("expired_edit_internal")
        except ObjectDoesNotExist:
            messages.error(request, 'Entry Not Found')
    
    return render(request,'expired_edit.html')

def expired_edit_internal(request):
    projectobj=project_table.objects.all()
    vendorobj=vendor_table.objects .all()
    print("Here Success Internal Edit")
    print("global Search_PO=")
    print(expired_global_search_PO)
    expired_eio=expired_table.objects.get(PO=expired_global_search_PO)
    print(expired_eio.PO)
    if 'cancel_button' in request.POST:
        print("In Cancel")
        return redirect("/expired_edit")
    elif 'submit_button' in request.POST:
        #expired_eio.project_id=request.POST['project']
        #expired_eio.vendor_id=request.POST['vendor']
       # eio.PO=request.POST.get('PO')
        expired_eio.oldPO=request.POST.get('oldPO')
        expired_eio.typePO=request.POST.get('typePO')
        expired_eio.desc=request.POST.get('desc')
        expired_eio.price=request.POST.get('price')
        expired_eio.startdate=request.POST.get('startdate')
        expired_eio.enddate=request.POST.get('enddate')
        expired_eio.BC1=request.POST.get('BC1')
        expired_eio.BC2=request.POST.get('BC2')
        expired_eio.BC3=request.POST.get('BC3')
        expired_eio.BC4=request.POST.get('BC4')
        expired_eio.PMC1=request.POST.get('PMC1')
        expired_eio.PMC2=request.POST.get('PMC2')
        expired_eio.PMC3=request.POST.get('PMC3')
        expired_eio.PMC4=request.POST.get('PMC4')
        expired_eio.PR=request.POST.get('PR')
        expired_eio.PRdate=request.POST.get('PRdate')
        #new=basetable(project_id=project,vendor_id=vendor,PO=PO,oldPO=oldPO,typePO=typePO,desc=desc,price=price,startdate=startdate,enddate=enddate,BC=BC,PMC=PMC,PR=PR,PRdate=PRdate)
        expired_eio.save()
        messages.success(request, 'VOILA!!!Expired PO Updated Succesfully!')
        return redirect("/expired_edit")
    elif 'delete_button' in request.POST:
        expired_eio.delete()
        print("deleted")
        messages.success(request, 'PO Deleted Succesfully!')
        return redirect("/expired_edit")
    
    
    return render(request,'expired_edit_internal.html',{"expired_table":expired_eio,"project_table":projectobj,"vendor_table":vendorobj})








def billing(request):
    #return HttpResponse("This is Billing")
    return render(request,'billing.html')

def PM(request):
    #return HttpResponse("This is Preventive Maintenance ")
    return render(request,'PM.html')

def view_all(request):
    #return HttpResponse("This is view all")
    #allpo=basetable.objects.all()
    projectobj=project_table.objects.all()
    vendorobj=vendor_table.objects.all()
    if request.method=='POST':
        project=request.POST['project']
        vendor=request.POST['vendor']
        duration=request.POST.get('duration')
        #Sample.objects.filter(date__range=[startdate, enddate])
        #print("duration=")
        #print(duration)
        #print("project=")
        #print(project)
        #print("vendor=")
        #print(vendor)
        if project=="ALL" and vendor=="ALL":
            if duration=='30days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=30)
                allpo_search=basetable.objects.filter(enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
            elif duration=='90days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=90)
                allpo_search=basetable.objects.filter(enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
            elif duration=='Expired':
                startdate_search = datetime.today()
                #enddate_search = startdate_search + timedelta(days=90)
                allpo_search=basetable.objects.filter(enddate__lt=startdate_search).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
        if project=="ALL":
            if duration=='30days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=30)
                allpo_search=basetable.objects.filter(vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
            elif duration=='90days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=90)
                allpo_search=basetable.objects.filter(vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})        
            else:
                startdate_search = datetime.today()
                #enddate_search = startdate_search + timedelta(days=90)
                allpo_search=basetable.objects.filter(vendor_id=vendor,enddate__lt=startdate_search).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})


        if vendor=="ALL":
            if duration=='30days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=30)
                allpo_search=basetable.objects.filter(project_id=project,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
            elif duration=='90days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=90)
                allpo_search=basetable.objects.filter(project_id=project,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})        
            else:
                startdate_search = datetime.today()
                #enddate_search = startdate_search + timedelta(days=90)
                allpo_search=basetable.objects.filter(project_id=project,enddate__lt=startdate_search).order_by('enddate')
                return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})


        if duration=='30days':
            startdate_search = datetime.today()
            enddate_search = startdate_search + timedelta(days=30)
            allpo_search=basetable.objects.filter(project_id=project,vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
            return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
        elif duration=='90days':
            startdate_search = datetime.today()
            enddate_search = startdate_serach + timedelta(days=90)
            allpo_search=basetable.objects.filter(project_id=project,vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
            return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
        #allpo_search=basetable.objects.raw('SELECT * FROM maindb WHERE vendor_id= '+vendor+'  project_id='+project+'' ) 
        elif duration=='Expired':
            startdate_search = datetime.today()
            #enddate_search = startdate_search + timedelta(days=90)
            allpo_search=basetable.objects.filter(project_id=project,vendor_id=vendor,enddate__lt=startdate_search).order_by('enddate')
            return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})

        else:
            allpo_search=basetable.objects.filter(project_id=project).filter(vendor_id=vendor).order_by('enddate')
            return render(request,'view_all.html',{"basetable":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
    else:
        #allpo=basetable.objects.raw('SELECT * FROM maindb').order_by('-enddate')
        allpo=basetable.objects.all().order_by('enddate')
        return render(request,'view_all.html',{"basetable":allpo,"project_table":projectobj,"vendor_table":vendorobj})    
    #context={"allpo":allpo,"project_table":projectobj,"vendor_table":vendorobj}
 
def expired_view_all(request):
        #return HttpResponse("This is view all")
    #allpo=basetable.objects.all()
    projectobj=project_table.objects.all()
    vendorobj=vendor_table.objects.all()
    if request.method=='POST':
        project=request.POST['project']
        vendor=request.POST['vendor']
        duration=request.POST.get('duration')
        #Sample.objects.filter(date__range=[startdate, enddate])
        #print("duration=")
        #print(duration)
        #print("project=")
        #print(project)
        #print("vendor=")
        #print(vendor)
        if project=="ALL" and vendor=="ALL":
            if duration=='30days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=30)
                allpo_search=expired_table.objects.filter(enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
            else:
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=90)
                allpo_search=expired_table.objects.filter(enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
        
        if project=="ALL":
            if duration=='30days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=30)
                allpo_search=expired_table.objects.filter(vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
            else:
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=90)
                allpo_search=expired_table.objects.filter(vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})        
        
        if vendor=="ALL":
            if duration=='30days':
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=30)
                allpo_search=expired_table.objects.filter(project_id=project,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
            else:
                startdate_search = datetime.today()
                enddate_search = startdate_search + timedelta(days=90)
                allpo_search=expired_table.objects.filter(project_id=project,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
                return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})        
        
        if duration=='30days':
            startdate_search = datetime.today()
            enddate_search = startdate_search + timedelta(days=30)
            allpo_search=expired_table.objects.filter(project_id=project,vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
            return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
        elif duration=='90days':
            startdate_search = datetime.today()
            enddate_search = startdate_serach + timedelta(days=90)
            allpo_search=expired_table.objects.filter(project_id=project,vendor_id=vendor,enddate__range=[startdate_search,enddate_search]).order_by('enddate')
            return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
        #allpo_search=basetable.objects.raw('SELECT * FROM maindb WHERE vendor_id= '+vendor+'  project_id='+project+'' ) 
        else:
            allpo_search=expired_table.objects.filter(project_id=project).filter(vendor_id=vendor).order_by('enddate')
            return render(request,'expired_view_all.html',{"expired_table":allpo_search,"project_table":projectobj,"vendor_table":vendorobj})
    else:
        #allpo=basetable.objects.raw('SELECT * FROM maindb').order_by('-enddate')
        allpo=expired_table.objects.all().order_by('enddate')
        return render(request,'expired_view_all.html',{"expired_table":allpo,"project_table":projectobj,"vendor_table":vendorobj})    
    #context={"allpo":allpo,"project_table":projectobj,"vendor_table":vendorobj}
           
    
def login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        # Check if user has entered correct credental
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request,("Hey!! You were logout out"))
    return redirect("/")
