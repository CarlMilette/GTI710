from apps import models


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
    return ""

def getVentesParProduit():
    return ""

def getVenteParDate():
    return ""

def getInventaire():
    return ""





