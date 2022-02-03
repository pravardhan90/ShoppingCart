class Cart(object):
    #initaitizing - cart(dict), product, tax and final total
    def __init__(self):
        self.cart_content = dict()
        self.product_total = 0
        self.tax_total = 0
        self.final_total = 0

    #add item to cart only if item does not exist, else update Qty
    def add_item(self, item):
        if item.product_name not in self.cart_content:
            self.cart_content.update({item.product_name: item})
        else:
            self.cart_content.get(item.product_name).product_qty += item.product_qty
    
    #to get total qty in the cart
    def get_cart_qty(self):
        return sum([v.product_qty for _,v in self.cart_content.items()])

    #to get product items list
    def get_cart_item_qty(self):
        return [{v.product_name : v.product_qty} for _,v in self.cart_content.items()]        

    #to get total value of cart
    def get_cart_total(self):
        self.get_product_total()
        self.get_tax_total()
        self.final_total = round(self.product_total + self.tax_total,2)
        return self.final_total
    
    #to get product total value
    def get_product_total(self):
        self.product_total = round(sum([v.product_price * v.product_qty for _, v in self.cart_content.items()]),2)
        return self.product_total

    #to get tax value of the product total value
    def get_tax_total(self):
        self.tax_total = round(self.product_total * 12.5/100,2)
        return self.tax_total