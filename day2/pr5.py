class Product:
    def __init__(self,product_id , name , price , stock , category):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
        self.category= category

    def add_stock(self,amt):
        self.stock += amt

    def reduce_stock(self,amt):
        if amt <= self.stock:
            self.stock -=amt
        else:
            print("not enought stock for {this.name}")

    def apply_discount(self,percentage):
        self.price -= self.price * (percentage / 100)
