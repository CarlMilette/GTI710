from apps import models

def getCategories():
    queryset = models.ProductCategory.objects.all()
    categorySet = {}
    for cat in queryset:
        categorySet[cat.id] = cat.name

    return categorySet

def getProducts():
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

def getCategoryToProductAssociation():
 return "";
