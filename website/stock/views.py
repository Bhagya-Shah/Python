from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Stockdata
from .models import Tradedata
from django.contrib import messages
import mathfilters

def stock(request):
    data=Stockdata.objects.all().values()
    template=loader.get_template('allData.html')
    context={
        'stockdata':data
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    stock=Stockdata.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'stockdata':stock,
    }
    return HttpResponse(template.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def adddata(request):
    if request.method=='POST':
        # sdate=request.POST['sdate']
        code=request.POST['code']
        sname=request.POST['stockname']
        sprice=request.POST['price']
        sqty=request.POST['quantity']
        if request.POST.get("buy"):
            action='BUY'
        elif request.POST.get("sell"): 
            action='SELL'
        bdata=Tradedata(action=action,sname=sname,sprice=sprice,sqty=sqty,code=code)
        # bdata=Tradedata(action=action,sname=sname,sprice=sprice,sqty=sqty,sdate=sdate)
        bdata.save() 
        mes=code+' => '+action+' '+sname+' at '+sprice+' @ '+sqty
        messages.info(request,mes)
    template=loader.get_template('collectdata.html')
    return HttpResponse(template.render(request=request))


def trades(request):
    stocks=Tradedata.objects.all()
    context={
        'stocks':stocks
    }
    template=loader.get_template('trades.html')
    return HttpResponse(template.render(context,request))


def viewcode(request):
    # codes=list(set(Tradedata.objects.values_list('sname').values()))
    codes=list(set(Tradedata.objects.values_list('code')))
    codes=[i[0] for i in codes]
    # print(codes[0][0])
    template=loader.get_template('viewcode.html')
    context={
        'allcodes':codes
    }
    return HttpResponse(template.render(context,request))


def codes(request,code):
    data=Tradedata.objects.filter(code=code).values()
    print(data)
    template=loader.get_template('codes.html')
    context={
        'c':code,
        'view':data
    }
    return HttpResponse(template.render(context,request))


# def netpos(request,code):
#     data=Tradedata.objects.filter(code=code).values()
#     # data=Tradedata.objects.raw("SELECT stock, SUM(CASE WHEN order_type = 'Buy' THEN quantity ELSE -quantity END) as remaining_quantity FROM trades GROUP BY stock")
#     template=loader.get_template('netpos.html')
#     context={
#         'c':code,
#         'view':data
#     }
    # return HttpResponse(template.render(context,request))