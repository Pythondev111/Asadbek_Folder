import token

from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    if 'EmailHome' in request.POST:
        email = request.POST.get('EmailHome')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    if 'Name_Signup' in request.POST:
        name = request.POST.get('Name_Signup')
        email = request.POST.get('Email_Signup')
        password = request.POST.get('Password_Signup')
        confirm_password = request.POST.get('Password_Confirm_Signup')
        s = 'Plese, make sure your confirm password is equal to your password!'
        if confirm_password != password:
            confirm_password = request.POST.get('Password_Confirm_Signup')
        ids = [0]
        users = Sing_up.objects.all()
        for a in users:
            ids.append(a.id)
        Sing_up(max(ids)+1, name, email, password, confirm_password, ).save()
    elif 'Email_Signin' in request.POST:
        emailSS = request.POST.get('Email_Signin')
        passwordSS = request.POST.get('Password_Signin')
        names = Sing_up.objects.all()
        ismlar =[]
        for n in names:
            ismlar.append(n.email)
            for m in names:
                ismlar.append(m.password)
        if emailSS and passwordSS in ismlar:
            return render(request, 'index.html')
        else:
            return render(request, 'sinov.html')
        # idss = [0]
        # userss = Sign_in.objects.all()
        # for user in userss:
        #     idss.append(user.id)
        # Sign_in(67, emailSS, passwordSS).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    products = Mobile_products.objects.all()[0:3]
    tur = Mobile.objects.get(id=2)
    audiois = Mobile_products.objects.filter(type = tur)
    koms = Accesuar_products.objects.all()[0:3]
    turs = Home.objects.get(id=1)
    homes = Home_products.objects.filter(type = turs)
    kitchen = Home_products.objects.filter()


    if "cmdpro" in request.POST:
        type = request.POST.get('cmdpro')
        amount = request.POST.get('addpro')
        name = request.POST.get('w3ls_itempro')
        price = request.POST.get('amountpro')
        ids = [0]
        mobiles = Basket_mobile.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_mobile(max(ids)+1, name, price, amount, type).save()

    if "addaudio" in request.POST:
        type = request.POST.get('cmdaudio')
        amount = request.POST.get('addaudio')
        name = request.POST.get('w3ls_itemaudio')
        price = request.POST.get('amountaudio')
        ids = [0]
        mobiles = Basket_mobile.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_mobile(max(ids)+1, name, price, amount, type).save()

    if "w3ls_itemkom" in request.POST:
        type = request.POST.get('cmdkom')
        amount = request.POST.get('addkom')
        name = request.POST.get('w3ls_itemkom')
        price = request.POST.get('amountkom')
        ids = [0]
        mobiles = Basket_accesuars.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_accesuars(max(ids)+1, name, price, amount, type).save()

    if "cmdhome2" in request.POST:
        type = request.POST.get('cmdhome2')
        amount = request.POST.get('addhome2')
        name = request.POST.get('w3ls_itemhome2')
        price = request.POST.get('amounthome2')
        ids = [0]
        mobiles = Basket_home.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_home(max(ids)+1, name, price, amount,type).save()

    if "cmdkitchen" in request.POST:
        type = request.POST.get('cmdkitchen')
        amount = request.POST.get('addkitchen')
        name = request.POST.get('w3ls_itemkitchen')
        price = request.POST.get('amountkitchen')
        ids = [0]
        mobiles = Basket_home.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_home(max(ids)+1, name, price, amount,type).save()

    return render(request, 'index.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product': products, 'koms':koms, 'homes':homes, 'audios':audiois, 'kitchen':kitchen})

def about(request):
    if 'EmailAbout' in request.POST:
        email = request.POST.get('EmailAbout')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    if 'Email' in request.POST:
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        users = Sign_in.objetcs.all()
        ids = [0]
        for user in users:
            ids.append(user.id)
        Sign_in(max(ids)+1, email, password).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'about.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def codes(request):
    if 'EmailCodes' in request.POST:
        emaill = request.POST.get('EmailCodes')
        email = Newslettter.objects.all()
        id = [0]
        for i in email:
            id.append(i.id)
        Newslettter(max(id)+1, emaill).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'codes.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def faq(request):
    if 'EmailFaq' in request.POST:
        email = request.POST.get('EmailFaq')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'faq.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def icons(request):
    if 'EmailIcons' in request.POST:
        email = request.POST.get('EmailIcons')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'icons.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})



def products(request, id = 0):
    if 'EmailProducts' in request.POST:
        email = request.POST.get('EmailProducts')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id) + 1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    if id != 0:
        tur = Mobile.objects.get(id = id)
        produccts = Mobile_products.objects.filter(type = tur)
    else:
        produccts = Mobile_products.objects.all()
    colors = Color.objects.all()

    if "cmd" in request.POST:
        type = request.POST.get('cmd')
        amount = request.POST.get('add')
        name = request.POST.get('w3ls_item')
        price = request.POST.get('amount')
        ids = [0]
        mobiles = Basket_mobile.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_mobile(max(ids)+1, name, price, amount, type).save()

    if "cmd_mobile1" in request.POST:
        type = request.POST.get('cmd_mobile1')
        amount = request.POST.get('add_mobile1')
        name = request.POST.get('w3ls_item_mobile1')
        price = request.POST.get('amount_mobile1')
        ids = [0]
        mobiles = Basket_mobile.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_mobile(max(ids) + 1, name, price, amount, type).save()


    mobile = Mobile_products.objects.all()[3]
    kom = Accesuar_products.objects.all()[2]
    related = Home_products.objects.all()[1]

    return render(request, 'products.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product': produccts, 'color': colors, 'mobile':mobile, 'kom':kom, 'rehome2':related})

def products1(request, id=0):
    if 'EmailProducts1' in request.POST:
        email = request.POST.get('EmailProducts1')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    if id  != 0:
        tur2 = Accessories.objects.get(id = id)
        products_acc = Accesuar_products.objects.filter(type = tur2)
    else:
        products_acc = Accesuar_products.objects.all()

    if "cmd" in request.POST:
        type = request.POST.get('cmd')
        amount = request.POST.get('add')
        name = request.POST.get('w3ls_item')
        price = request.POST.get('amount')
        ids = [0]
        mobiles = Basket_accesuars.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_accesuars(max(ids)+1, name, price, amount, type).save()

    return render(request, 'products1.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product_acc':products_acc})

def products2(request, id = 0):
    if 'EmailProducts2' in request.POST:
        email = request.POST.get('EmailProducts2')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    if id != 0:
        tur1 = Home.objects.get(id = id)
        product_home = Home_products.objects.filter(type = tur1)
    else:
        product_home = Home_products.objects.all()

    if "cmd" in request.POST:
        type = request.POST.get('cmd')
        amount = request.POST.get('add')
        name = request.POST.get('w3ls_item')
        price = request.POST.get('amount')
        ids = [0]
        mobiles = Basket_home.objects.all()
        for mobile in mobiles:
            ids.append(mobile.id)

        Basket_home(max(ids)+1, name, price, amount,type).save()
    return render(request, 'products2.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home, 'product_home': product_home})

def single(request):
    if 'Name' in request.POST:
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        message = request.POST.get('Review')
        idlar = [0]
        emaillar = Single_review.objects.all()
        for e in emaillar:
            idlar.append(e.id)
        Single_review(max(idlar)+1, name, email, tel, message).save()
    elif 'EmailSingle' in request.POST:
        email = request.POST.get('EmailSingle')
        emails = Newslettter.objects.all()
        id = [0]
        for i in emails:
            id.append(i.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'single.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def mail(request):
    if 'Name' in request.POST:
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        tel = request.POST.get('Telephone')
        message = request.POST.get('message')

        idlar = [0]
        emaillar = Mail.objects.all()
        for e in emaillar:
            idlar.append(e.id)
        Mail(max(idlar)+1, name, email, tel, message).save()
    elif 'Email' in request.POST:
        email = request.POST.get('Email')
        emails = Newslettter.objects.all()
        id = [0]
        for a in emails:
            id.append(a.id)
        Newslettter(max(id)+1, email).save()
    mobillar = Mobile.objects.all()
    accesuars = Accessories.objects.all()
    home = Home.objects.all()
    return render(request, 'mail.html', {"mobiles": mobillar, "accesuars": accesuars, "home": home})

def korzinka(request, id = 0, id_home = 0, id_accosories =0):
    if id != 0:
        mobiles = Basket_mobile.objects.get(id = id).delete()
    else:
        pass

    mobiles = Basket_mobile.objects.all()

    if id_accosories != 0:
        koms = Basket_accesuars.objects.get(id = id_accosories).delete()
    else:
        pass

    if id_home != 0:
        m = Basket_home.objects.get(id = id_home).delete()
    else:
        pass


    mobile_narx = 0
    for mobile in mobiles:
        mobile_narx += mobile.newprice

    koms = Basket_accesuars.objects.all()
    koms_narx = 0
    for kom in koms:
        koms_narx += kom.newprice

    homes = Basket_home.objects.all()
    homes_narx = 0
    for home in homes:
        mobile_narx += home.newprice


    return  render(request, 'korzinka2.html', {'mobiles': mobiles, 'koms': koms, 'homes':homes, 'narx1': mobile_narx, 'narx2': koms_narx, 'narx3': homes_narx })

def updatee(request, id1=0, id2=0, id3=0):

    colors = Color.objects.all()

    mobiles = Mobile.objects.all()
    homes = Home.objects.all()
    accesories = Accessories.objects.all()
    if request.method == 'POST':
        type = request.POST.get('type')
        if type in mobiles:
            id = request.POST.get('idnumber')
            max = Home_products.objects.get(id = id)
            rang = request.POST.get('rang')
            miqdor = request.POST.get('amount')
            Mobile_products(id, max.name, max.newprice, max.oldprice, max.rate, max.type, rang, max.image, miqdor).save()
        elif type in homes:
            id = request.POST.get('idnumber')
            max = Home_products.objects.get(id=id)
            rang = request.POST.get('rang')
            miqdor = request.POST.get('amount')
            Home_products(id, max.name, max.newprice, max.oldprice, max.rate, max.type, rang, max.image, miqdor).save()

        mobile = Mobile_products.objects.all()
        home = Home_products.objects.all()

        return render(request, 'korzinka.html', {"mobile":mobile, "homes":home})
    if id1 !=0:
        maxx = Mobile_products.objects.get(id=id1)
    elif id2 !=0:
        maxx = Basket_home.objects.get(id=id2)
        pro_name = maxx.name
        pro_type = maxx.type
        pro_price = maxx.newprice
        pro_amount = request.POST.get("num")
        Basket_home(id2, pro_name, pro_price, pro_amount, pro_type).save()

    shoplist = Basket_home.objects.all

    return render(request, "korzinka2.html", {"mobiles":shoplist, "colors":colors})