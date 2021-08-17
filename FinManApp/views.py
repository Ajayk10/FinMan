from django.shortcuts import redirect, render
from . models import *
from .forms import *
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, "index.html" ,{})

def jointaccount(request):
    return render(request, "jointaccount.html" ,{})

def pensionaccount(request):
    return render(request, "pensionaccount.html" ,{})

def csbaccount(request):
    return render(request, "csbaccount.html" ,{})

def inhand(request):
    return render(request, "inhand.html" ,{})

def myaccount(request):
    return render(request, "myaccount.html" ,{})

#-------------------------------start of transaction pages-------------------------------

def jointaccounttransaction(request):
    if request.method == 'POST':
        form = JointAccountForm(request.POST or None)
        if form.is_valid():
            form.save()
        all_item=JointAccountModel.objects.all
        return redirect('jointaccountstatement')
    else:
        all_item=JointAccountModel.objects.all
        balance = JointAccountModel.objects.all().last()
        if balance == None:
            balance=100000
        context = {'all_item':all_item,'balance':balance}
        return render(request, "jointaccounttransaction.html" ,context)

def pensionaccounttransaction(request):
    if request.method == 'POST':
        form = PensionAccountForm(request.POST or None)
        if form.is_valid():
            form.save()
        pension_all_item=PensionAccountModel.objects.all()
        return redirect( 'pensionaccountstatement')
    else:
        pension_all_item=PensionAccountModel.objects.all
        balance = PensionAccountModel.objects.all().last()
        if balance == None:
            balance=100000
        context = {'pension_all_item':pension_all_item,'balance':balance}
        return render(request, "pensionaccounttransaction.html" ,context)   

def myaccounttransaction(request):
    if request.method == 'POST':
        form = MyAccountForm(request.POST or None)
        if form.is_valid():
            form.save()
        all_item=MyAccountModel.objects.all
        return redirect('myaccountstatement')
    else:
        all_item=MyAccountModel.objects.all
        balance = MyAccountModel.objects.all().last()
        if balance == None:
            balance=100000
        context = {'all_item':all_item,'balance':balance}
        return render(request, "myaccounttransaction.html" ,context)  

def inhandtransaction(request):
    if request.method == 'POST':
        form = InHandForm(request.POST or None)
        if form.is_valid():
            form.save()
        all_item=InHandModel.objects.all()
        return redirect('inhandstatement')
    else:
        all_item=InHandModel.objects.all()
        balance = InHandModel.objects.all().last()
        if balance == None:
            balance=100000
        context = {'all_item':all_item,'balance':balance}
        return render(request, "inhandtransaction.html" ,context)   

def csbaccounttransaction(request):
    if request.method == 'POST':
        form = CSBAccountForm(request.POST or None)
        if form.is_valid():
            form.save()
        all_item=CSBAccountModel.objects.all
        return redirect('csbaccountstatement')
    else:
        all_item=CSBAccountModel.objects.all
        balance = CSBAccountModel.objects.all().last()
        if balance == None:
            balance=100000
        context = {'all_item':all_item,'balance':balance}
        return render(request, "csbaccounttransaction.html" ,context)  

#-------------------------------end of transaction pages-------------------------------

#-------------------------------start of statement pages-------------------------------
def jointaccountstatement(request):
    joint_all_item=JointAccountModel.objects.all().order_by("-id")
    if request.method == 'POST':
        mydate = datetime.now()
        curr_month = request.POST["month"]
        curr_year = request.POST["year"]
        joint_all_item = JointAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "jointaccountstatement.html" ,{'joint_all_item':joint_all_item})
    else:
        joint_all_item=JointAccountModel.objects.all().order_by("-id")
        mydate = datetime.now()
        curr_month = mydate.strftime("%m")
        curr_year = mydate.strftime("%Y")
        joint_all_item = JointAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "jointaccountstatement.html" ,{'joint_all_item':joint_all_item})

def inhandstatement(request):
    all_item=InHandModel.objects.all().order_by("-id")
    if request.method == 'POST':
        mydate = datetime.now()
        curr_month = request.POST["month"]
        curr_year = request.POST["year"]
        all_item = InHandModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "inhandstatement.html" ,{'all_item':all_item})
    else:
        all_item=InHandModel.objects.all().order_by("-id")
        mydate = datetime.now()
        curr_month = mydate.strftime("%m")
        curr_year = mydate.strftime("%Y")
        all_item = InHandModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "inhandstatement.html" ,{'all_item':all_item})

def pensionaccountstatement(request):
    all_item=PensionAccountModel.objects.all().order_by("-id")
    if request.method == 'POST':
        mydate = datetime.now()
        curr_month = request.POST["month"]
        curr_year = request.POST["year"]
        all_item = PensionAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "pensionaccountstatement.html" ,{'all_item':all_item})
    else:
        all_item=PensionAccountModel.objects.all().order_by("-id")
        mydate = datetime.now()
        curr_month = mydate.strftime("%m")
        curr_year = mydate.strftime("%Y")
        all_item = PensionAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "pensionaccountstatement.html" ,{'all_item':all_item})

def csbaccountstatement(request):
    all_item=CSBAccountModel.objects.all().order_by("-id")
    if request.method == 'POST':
        mydate = datetime.now()
        curr_month = request.POST["month"]
        curr_year = request.POST["year"]
        all_item = CSBAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "csbaccountstatement.html" ,{'all_item':all_item})
    else:
        all_item=CSBAccountModel.objects.all().order_by("-id")
        mydate = datetime.now()
        curr_month = mydate.strftime("%m")
        curr_year = mydate.strftime("%Y")
        all_item = CSBAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "csbaccountstatement.html" ,{'all_item':all_item})

def myaccountstatement(request):
    all_item=MyAccountModel.objects.all().order_by("-id")
    if request.method == 'POST':
        mydate = datetime.now()
        curr_month = request.POST["month"]
        curr_year = request.POST["year"]
        all_item = MyAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "myaccountstatement.html" ,{'all_item':all_item})
    else:
        all_item=MyAccountModel.objects.all().order_by("-id")
        mydate = datetime.now()
        curr_month = mydate.strftime("%m")
        curr_year = mydate.strftime("%Y")
        all_item = MyAccountModel.objects.filter(month=curr_month , year = curr_year).order_by("-id")
        return render(request, "myaccountstatement.html" ,{'all_item':all_item})


#-------------------------------end of statement pages-------------------------------


#-------------------------------start of details pages-------------------------------


def jointaccountdetails(request,JointAccountModel_id):
    try:
        item = JointAccountModel.objects.get(pk=JointAccountModel_id)
        if request.method == 'POST':
            item.amount=request.POST["amount"]
            item.title=request.POST["title"]
            item.description=request.POST["description"]
            item.save()
            all_item=JointAccountModel.objects.all
            return redirect('jointaccountstatement')
        else:
            item = JointAccountModel.objects.get(pk=JointAccountModel_id)
            return render(request, "jointaccountdetails.html" ,{'item':item})
    except:
        return redirect('jointaccountstatement')

def pensionaccountdetails(request,PensionAccountModel_id):
    try:
        item = PensionAccountModel.objects.get(pk=PensionAccountModel_id)
        if request.method == 'POST':
            item.amount=request.POST["amount"]
            item.title=request.POST["title"]
            item.description=request.POST["description"]
            item.save()
            all_item=PensionAccountModel.objects.all
            return redirect('pensionaccountstatement')
        else:
            item = PensionAccountModel.objects.get(pk=PensionAccountModel_id)
            return render(request, "pensionaccountdetails.html" ,{'item':item})
    except:
        return redirect('pensionaccountstatement')


def myaccountdetails(request,MyAccountModel_id):
    try:
        item = MyAccountModel.objects.get(pk=MyAccountModel_id)
        if request.method == 'POST':
            item.amount=request.POST["amount"]
            item.title=request.POST["title"]
            item.description=request.POST["description"]
            item.save()
            all_item=MyAccountModel.objects.all
            return redirect('myaccountstatement')
        else:
            item = MyAccountModel.objects.get(pk=MyAccountModel_id)
            return render(request, "myaccountdetails.html" ,{'item':item})
    except:
        return redirect('myaccountstatement')


def csbaccountdetails(request,CSBAccountModel_id):
    try:
        item = CSBAccountModel.objects.get(pk=CSBAccountModel_id)
        if request.method == 'POST':
            item.amount=request.POST["amount"]
            item.title=request.POST["title"]
            item.description=request.POST["description"]
            item.save()
            all_item=CSBAccountModel.objects.all
            return redirect('csbaccountstatement')
        else:
            item = CSBAccountModel.objects.get(pk=CSBAccountModel_id)
            return render(request, "csbaccountdetails.html" ,{'item':item})
    except:
        return redirect('csbaccountstatement')


def inhanddetails(request,InHandModel_id):
    try:
        item = InHandModel.objects.get(pk=InHandModel_id)
        if request.method == 'POST':
            item.amount=request.POST["amount"]
            item.title=request.POST["title"]
            item.description=request.POST["description"]
            item.save()
            all_item=InHandModel.objects.all
            return redirect('inhandstatement')
        else:
            item = InHandModel.objects.get(pk=InHandModel_id)
            return render(request, "inhanddetails.html" ,{'item':item})
    except:
        print(item.amount)
        return redirect('index')

#-------------------------------end of details pages-------------------------------


#--------------------------------Dashboard-----------------------------------------
def dashboard(request):
    mydate = datetime.now()
    curr_month = mydate.strftime("%m")
    curr_year = mydate.strftime("%Y")
    jointcredit = jointdebit = csbcredit=csbdebit=0
    pensioncredit=pensiondebit=inhandcredit=inhanddebit=mycredit=mydebit= 0
    totalcredit = totaldebit = 0

    joint = JointAccountModel.objects.all().last()
    csb = CSBAccountModel.objects.all().last()
    pension = PensionAccountModel.objects.all().last()
    inhand = InHandModel.objects.all().last()
    my = MyAccountModel.objects.all().last()

    joint_all = JointAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
    for v in joint_all:
                if v['amount'] >  0:
                    jointcredit =jointcredit + v['amount']
                else:
                    jointdebit = jointdebit + v['amount']
                    
    csb_all = CSBAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
    for v in csb_all:
                if v['amount'] >  0:
                    csbcredit =csbcredit + v['amount']
                else:
                    csbdebit = csbdebit + v['amount']
                
    pension_all = PensionAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
    for v in pension_all:
                if v['amount'] >  0:
                    pensioncredit =pensioncredit + v['amount']
                else:
                    pensiondebit = pensiondebit + v['amount']

    inhand_all = InHandModel.objects.filter(month=curr_month , year = curr_year).values('amount')
    for v in inhand_all:
                if v['amount'] >  0:
                    inhandcredit =inhandcredit + v['amount']
                else:
                    inhanddebit = inhanddebit + v['amount']

    my_all = MyAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
    for v in my_all:
                if v['amount'] >  0:
                    mycredit =mycredit + v['amount']
                else:
                    mydebit = mydebit + v['amount']

    totalcredit = jointcredit+mycredit+csbcredit+pensioncredit+inhandcredit
    totaldebit = jointdebit+mydebit+csbdebit+pensiondebit+inhanddebit

    context ={'joint':joint,'csb':csb,'pension':pension,'inhand':inhand,
            'my':my,'joint_all':joint_all,
            'jointcredit':jointcredit,'jointdebit':jointdebit,
            'csbcredit':csbcredit,'csbdebit':csbdebit,
            'pensioncredit':pensioncredit,'pensiondebit':pensiondebit,
            'mycredit':mycredit,'mydebit':mydebit,
            'inhandcredit':inhandcredit,'inhanddebit':inhanddebit,
            'totalcredit':totalcredit,'totaldebit':totaldebit,}
    return render(request, "dashboard.html" ,context)


#-------------------------------------Detailed Statistics------------------------------
def statistics(request):
    if request.method == 'POST':
        mydate = datetime.now()
        curr_month = request.POST["month"]
        curr_year = request.POST["year"]
        jointcredit = jointdebit = csbcredit=csbdebit=0
        pensioncredit=pensiondebit=inhandcredit=inhanddebit=mycredit=mydebit= 0
        totalcredit = totaldebit = 0
        joint_all = JointAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in joint_all:
                    if v['amount'] >  0:
                        jointcredit =jointcredit + v['amount']
                    else:
                        jointdebit = jointdebit + v['amount']
                        
        csb_all = CSBAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in csb_all:
                    if v['amount'] >  0:
                        csbcredit =csbcredit + v['amount']
                    else:
                        csbdebit = csbdebit + v['amount']
                    
        pension_all = PensionAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in pension_all:
                    if v['amount'] >  0:
                        pensioncredit =pensioncredit + v['amount']
                    else:
                        pensiondebit = pensiondebit + v['amount']

        inhand_all = InHandModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in inhand_all:
                    if v['amount'] >  0:
                        inhandcredit =inhandcredit + v['amount']
                    else:
                        inhanddebit = inhanddebit + v['amount']

        my_all = MyAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in my_all:
                    if v['amount'] >  0:
                        mycredit =mycredit + v['amount']
                    else:
                        mydebit = mydebit + v['amount']

        totalcredit = jointcredit+mycredit+csbcredit+pensioncredit+inhandcredit
        totaldebit = jointdebit+mydebit+csbdebit+pensiondebit+inhanddebit

        context ={'joint_all':joint_all,
                'jointcredit':jointcredit,'jointdebit':jointdebit,
                'csbcredit':csbcredit,'csbdebit':csbdebit,
                'pensioncredit':pensioncredit,'pensiondebit':pensiondebit,
                'mycredit':mycredit,'mydebit':mydebit,
                'inhandcredit':inhandcredit,'inhanddebit':inhanddebit,
                'totalcredit':totalcredit,'totaldebit':totaldebit,}
        return render(request, "statistics.html" ,context)
    else:
        mydate = datetime.now()
        curr_month = mydate.strftime("%m")
        curr_year = mydate.strftime("%Y")
        jointcredit = jointdebit = csbcredit=csbdebit=0
        pensioncredit=pensiondebit=inhandcredit=inhanddebit=mycredit=mydebit= 0
        totalcredit = totaldebit = 0
        joint_all = JointAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in joint_all:
                    if v['amount'] >  0:
                        jointcredit =jointcredit + v['amount']
                    else:
                        jointdebit = jointdebit + v['amount']
                        
        csb_all = CSBAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in csb_all:
                    if v['amount'] >  0:
                        csbcredit =csbcredit + v['amount']
                    else:
                        csbdebit = csbdebit + v['amount']
                    
        pension_all = PensionAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in pension_all:
                    if v['amount'] >  0:
                        pensioncredit =pensioncredit + v['amount']
                    else:
                        pensiondebit = pensiondebit + v['amount']

        inhand_all = InHandModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in inhand_all:
                    if v['amount'] >  0:
                        inhandcredit =inhandcredit + v['amount']
                    else:
                        inhanddebit = inhanddebit + v['amount']

        my_all = MyAccountModel.objects.filter(month=curr_month , year = curr_year).values('amount')
        for v in my_all:
                    if v['amount'] >  0:
                        mycredit =mycredit + v['amount']
                    else:
                        mydebit = mydebit + v['amount']

        totalcredit = jointcredit+mycredit+csbcredit+pensioncredit+inhandcredit
        totaldebit = jointdebit+mydebit+csbdebit+pensiondebit+inhanddebit

        context ={'joint_all':joint_all,
                'jointcredit':jointcredit,'jointdebit':jointdebit,
                'csbcredit':csbcredit,'csbdebit':csbdebit,
                'pensioncredit':pensioncredit,'pensiondebit':pensiondebit,
                'mycredit':mycredit,'mydebit':mydebit,
                'inhandcredit':inhandcredit,'inhanddebit':inhanddebit,
                'totalcredit':totalcredit,'totaldebit':totaldebit,}
        return render(request, "statistics.html" ,context)

    
