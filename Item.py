class Item(object): 
    #initalizing - id, name, price & Qty for an item
    def __init__(self, name, price, qty):

        #check name passed in string
        if not isinstance(name, str):
            raise TypeError("name should be a string")

        #check price passed is float
        if not isinstance(price, float):
            raise TypeError("price should be a float")
            
        self.check_int_positive(qty)

        self.product_name = name
        self.product_price = price
        self.product_qty = qty

    #check if value is integer and positive  
    def check_int_positive(self, value):
        if not isinstance(value, int):
            raise TypeError("{} should be integer".format(value))
        if value < 1:
            raise ValueError("{} has to be more than 0".format(value))
    
