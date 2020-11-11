from shop.models import Product, Category
from coupons.models import Coupon
from account.models import MyUser

class abstractObjectSort(object):
    def sortIt(self, array, order, datatype):
        self.outerBubbleSortLoop(array, 0)
        array = self.sortedIDSToSortedArray(array, datatype)
        if order == 1:
            array.reverse()
        return array


#recursive bubble sort
#recursive outer loop
    def outerBubbleSortLoop(self, array, i):
        
        if i == (len(array)):
                return(array)
        else:
                self.innerBubbleSortLoop(array, 0)
                self.outerBubbleSortLoop(array, (i+1))
#recursive inner loop
    def innerBubbleSortLoop(self, array, j):
        if j == (len(array)-1):
                return(array)
        else:
                if array[j][1] > array[j+1][1]:
                        temp = array[j+1]
                        array[j+1] = array[j]
                        array[j] = temp
                self.innerBubbleSortLoop(array, (j+1))

    def sortedIDSToSortedArray(self, array, datatype):
        sortedArray = []
        for element in array:
                if datatype == 0:
                        elementObject = Product.objects.get(id = element[0])
                elif datatype == 1:
                        elementObject = Category.objects.get(id = element[0])
                elif datatype == 2:
                        elementObject = Coupon.objects.get(id = element[0])
                elif datatype == 3:
                        elementObject = Product.objects.get(id = element[0])

                elif datatype == 4:
                        elementObject = MyUser.objects.get(id = element[0])
                elif datatype == 5:
                        elementObject = MyUser.objects.get(id = element[0])
                elif datatype == 6:
                        elementObject = MyUser.objects.get(id = element[0])
                elif datatype == 7:
                        elementObject = MyUser.objects.get(id = element[0])

                sortedArray.append(elementObject)
        return sortedArray

class abstractPopularity(abstractObjectSort):
    def getPopularity(self, order, datatype):
        popularity = []
        if datatype == 0:
            products = Product.objects.filter()
            for product in products:
                popularity.append([product.id, product.totalQuantity()])
        elif datatype == 1:
            categories = Category.objects.filter()
            for category in categories:
                popularity.append([category.id, category.getTotal(0)])
        elif datatype == 2:
            coupons = Coupon.objects.filter()
            for coupon in coupons:
                popularity.append([coupon.id, coupon.findTotalUse()])
        elif datatype == 3:
            products = Product.objects.filter()
            for product in products:
                popularity.append([product.id, product.amountOftimesOrdered()])

        elif datatype == 4:
            customers = MyUser.objects.filter()
            for customer in customers:
                popularity.append([customer.id, customer.numOfOrdersOfCus()])
        elif datatype == 5:
            customers = MyUser.objects.filter()
            for customer in customers:
                popularity.append([customer.id, customer.numOfDeliveriesOfCus()])
        elif datatype == 6:
            customers = MyUser.objects.filter()
            for customer in customers:
                popularity.append([customer.id, customer.numOfCollectionsOfCus()])
        elif datatype == 7:
            customers = MyUser.objects.filter()
            for customer in customers:
                popularity.append([customer.id, customer.numOfInStoreOfCus()])

        elif datatype == 8:
            customers = MyUser.objects.filter()
            for customer in customers:
                popularity.append([customer.id, customer.totalSpent()])
        elif datatype == 9:
            customers = MyUser.objects.filter()
            for customer in customers:
                popularity.append([customer.id, customer.averageSpent()])

        return self.sortIt(popularity, order, datatype)