
class Checkout:
    class Discount:
        def __init__(self, nbrOfItems, price):
            self.nbrOfItems = nbrOfItems
            self.price = price

        def numberOfDiscountsFor(self, cnt):
            return cnt / self.nbrOfItems
        
        def remainingOfDiscountFor(self, cnt):
            return cnt % self.nbrOfItems

        def applyTo(self, cnt, regular_price):
            remaining = self.remainingOfDiscountFor(cnt)
            return self.numberOfDiscountsFor(cnt) * self.price +\
                self.remainingOfDiscountFor(cnt) * regular_price

    def __init__(self):
        self.prices = { }
        self.discounts = { }
        self.items = { }

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if not item in self.prices:
            raise Exception('item {} does not have price'.format(item))
        if not item in self.items:
            self.items[item] = 0
        self.items[item] += 1
 
    def getTotal(self):
        total = 0
        for item in self.items:
            cnt = self.items[item]
            if item in self.discounts:
                discount = self.discounts[item]
                total += discount.applyTo(cnt, self.prices[item])
            else:
                total += self.prices[item] * cnt
        return total

    def addDiscount(self, item, nbrOfItems, price):
        self.discounts[item] = self.Discount(nbrOfItems, price)
