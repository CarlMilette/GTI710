from . import models


######### division pour application web ##########

def getCategories(): #GET categories
    queryset = models.ProductCategory.objects.all()
    categorySet = {}
    for cat in queryset:
        categorySet[cat.id] = cat.name

    return categorySet

def getProducts(): #GET produits
    prdPrd = models.ProductTemplate.objects.all()
    productSet = {}
    for pr in prdPrd:
        product = {}
        product['name'] = pr.name
        product['categoryId'] = pr.categ_id
        product['listPrice'] = pr.list_price
        productSet[pr.id] = product

    print(productSet.__len__())
    for each in productSet.values():
        print(each['name'])

    return productSet

def getCategoryToProductAssociation(): #GET related products (amazon)
    return ""

def postCommande(): #POST commande
    return ""

def postRating(): #POST rating
    return ""


######### division pour application mobile ##########

def getTotalVente():

    venteTot = {}
    vente = 0

    queryset = models.SaleOrderLine.objects.all()
    for each in queryset:
        print(each.qty_invoiced)
        vente += each.qty_invoiced

    venteTot['total'] = vente

    ################################################

    venteTot['revenue'] = 0
    venteTot['profit'] = 0

    queryset = models.SaleOrderLine.objects.all()
    for each in queryset:
        vente = {}
        # print(each.product_id)
        # print(each.qty_invoiced)
        vente['quantity'] = each.qty_invoiced
        vente['product_id'] = each.product_id

        queryset3 = models.ProductTemplate.objects.all()
        for each3 in queryset3:
            # print(each3.id)
            # print(each3.list_price)
            if each3.id == vente['product_id']:
                vente['revenue'] = each.qty_invoiced * each3.list_price
                venteTot['revenue'] += vente['revenue']

        queryset3bis = models.IrProperty.objects.all()
        for each3bis in queryset3bis:
            test = str(each3bis.res_id)
            testbis = test.split(",", 1)[-1]
            # print(each3bis.value_float)
            if str(vente['product_id']) == testbis:
                vente['profit'] = float(vente['revenue']) - each3bis.value_float
                venteTot['profit'] += vente['profit']

    venteTot['profit'] = str(round(venteTot['profit'],2))

    return venteTot

def getVentesParProduit():

    venteSet = {}

    queryset = models.SaleOrderLine.objects.all()
    for each in queryset:
        vente = {}
        #print(each.product_id)
        #print(each.qty_invoiced)
        vente['quantity'] = each.qty_invoiced
        vente['product_id'] = each.product_id

        queryset2 = models.ProductProduct.objects.all()
        for each2 in queryset2:
            #print(each2.product_tmpl_id)
            #print(each2.name_template)
            if each2.product_tmpl_id == vente['product_id']:
                vente['name'] = each2.name_template

        queryset3 = models.ProductTemplate.objects.all()
        for each3 in queryset3:
            #print(each3.id)
            #print(each3.list_price)
            if each3.id == vente['product_id']:
                vente['revenue'] = each.qty_invoiced * each3.list_price

        queryset3bis = models.IrProperty.objects.all()
        for each3bis in queryset3bis:
            test = str(each3bis.res_id)
            testbis = test.split(",", 1)[-1]
            #print(each3bis.value_float)
            if str(vente['product_id']) == testbis:
                vente['profit'] = float(vente['revenue']) - each3bis.value_float

        vente['profit'] = str(round(vente['profit'], 2))

        venteSet[each.id] = vente

    print(venteSet.__len__())
    for each4 in venteSet.values():
        print(each4['name'])

    return venteSet

def getVenteParDate():

    # TODO : corriger cette API

    venteSet = {}

    queryset = models.SaleOrderLine.objects.all()
    for each in queryset:
        vente = {}

        date = str(each.create_date)
        datebis = date.split(" ", 1)[0]

        venteSet[datebis] = vente


    for eachf in venteSet:
        queryset = models.SaleOrderLine.objects.all()

        vente = {}

        vente['revenue'] = 0
        vente['profit'] = 0

        for each1 in queryset:
            # print(each.product_id)
            # print(each.qty_invoiced)

            datecreate1 = str(each1.create_date)
            datecreatebbis1 = datecreate1.split(" ", 1)[0]

            queryset3 = models.ProductTemplate.objects.all()
            for each3 in queryset3:
                # print(each3.id)
                # print(each3.list_price)
                if each3.id == each1.product_id:
                    if eachf == datecreatebbis1:
                        vente['revenue'] += each1.qty_invoiced * each3.list_price

        ##

        queryset = models.SaleOrderLine.objects.all()
        for each in queryset:

            datecreate2 = str(each.create_date)
            datecreatebbis2 = datecreate2.split(" ", 1)[0]

            ventebis = {}
            # print(each.product_id)
            # print(each.qty_invoiced)
            ventebis['quantity'] = each.qty_invoiced
            ventebis['product_id'] = each.product_id

            queryset2 = models.ProductProduct.objects.all()
            for each2 in queryset2:
                # print(each2.product_tmpl_id)
                # print(each2.name_template)
                if each2.product_tmpl_id == ventebis['product_id']:
                    ventebis['name'] = each2.name_template

            queryset33 = models.ProductTemplate.objects.all()
            for each33 in queryset33:
                # print(each3.id)
                # print(each3.list_price)
                if each33.id == ventebis['product_id']:
                    ventebis['revenue'] = each.qty_invoiced * each33.list_price

            queryset3bis = models.IrProperty.objects.all()
            for each3bis in queryset3bis:
                test = str(each3bis.res_id)
                testbis = test.split(",", 1)[-1]
                # print(each3bis.value_float)
                if str(ventebis['product_id']) == testbis:
                    if eachf == datecreatebbis2:
                        vente['profit'] += float(ventebis['revenue']) - each3bis.value_float

            datecreate = str(each1.create_date)
            datecreatebbis = datecreate.split(" ", 1)[0]

            #vente['profit'] = str(round(vente['profit'], 2))

        ##

            ##print (venteSet[eachf])
            ##if eachf == datecreatebbis:
            venteSet[eachf] = vente

    #print(venteSet.__len__())
    #for each2 in venteSet.values():
    #    print(each2['date'])

    return venteSet

def getInventaire():

    # TODO : implementer API

    return ""





