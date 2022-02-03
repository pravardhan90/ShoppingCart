import unittest

from Item import Item
from Cart import Cart

class TestItemMethods(unittest.TestCase):

    #test correct input
    def test_correct_item_value(self):
        obj_1 = Item("Dove Soap", 39.99, 1) 
        self.assertEqual(obj_1.product_name, "Dove Soap")
        self.assertEqual(obj_1.product_price, 39.99)
        self.assertEqual(obj_1.product_qty, 1)

    #test qty as negative to raise equivalent exception
    def test_qty_negative(self):
        with self.assertRaises(ValueError):
            obj_2 = Item("Dove Soap", 39.99, -1) 
    
    #test qty as float to raise equivalent exception
    def test_qty_float(self):
        with self.assertRaises(TypeError):
            obj_3 = Item("Dove Soap", 39.99, 1.5) 
    
    #test name  with interger to raise equivalent exception
    def test_wrong_name(self):
        with self.assertRaises(TypeError):
            obj_4 = Item(123, 39.99, 1)
    
    #test qty as Zero to raise equivalent exception
    def test_qty_zero(self):
        with self.assertRaises(ValueError):
            obj_5 = Item("Dove Soap", 39.99, 0)

class TestCartMethods(unittest.TestCase):

    #setup needed for all cases
    def setUp(self):
        self.cart = Cart()

    #test cart is empty with out adding items
    def test_cart_content_empty(self):

        self.assertEqual(self.cart.cart_content, {})
        
    #test cart functions with one item addition
    def test_add_item(self):
        obj_1 = Item("Dove Soap", 39.99, 1)
        self.cart.add_item(obj_1)
        self.assertEqual(self.cart.cart_content, {"Dove Soap":obj_1})
        self.assertEqual(self.cart.get_cart_qty(), 1)
        self.assertEqual(self.cart.get_product_total(), 39.99)
        self.assertEqual(self.cart.get_cart_item_qty(), [{"Dove Soap":1}])
        self.assertEqual(self.cart.get_tax_total(), 5.00)
        self.assertEqual(self.cart.get_cart_total(), 44.99)

    #test cart functions with multiple same items addition
    def test_add_multiple_same_items(self):

        obj_1 = Item("Dove Soap", 39.99, 1)
        obj_2 = Item("Dove Soap", 39.99, 5)
        obj_3 = Item("Dove Soap", 39.99, 6)
        self.cart.add_item(obj_1)
        self.cart.add_item(obj_2)
        self.assertEqual(self.cart.get_cart_qty(), obj_3.product_qty)
        self.assertEqual(self.cart.get_cart_item_qty(), [{obj_3.product_name:obj_3.product_qty}])
        self.assertEqual(self.cart.get_product_total(), 239.94)
        self.assertEqual(self.cart.get_tax_total(), 29.99)
        self.assertEqual(self.cart.get_cart_total(), 269.93)

    #test cart functions with different items in cart
    def test_add_multiple_diff_items(self):

        obj_1 = Item("Dove Soap", 39.99, 1)
        obj_4 = Item("Axe Deos", 39.99, 4)
        self.cart.add_item(obj_1)
        self.cart.add_item(obj_4)
        self.assertEqual(self.cart.get_cart_qty(), 5)
        self.assertEqual(self.cart.get_cart_item_qty(), [{"Dove Soap": 1},{"Axe Deos": 4}])
        self.assertEqual(self.cart.get_product_total(), 199.95)
        self.assertEqual(self.cart.get_tax_total(), 24.99)
        self.assertEqual(self.cart.get_cart_total(), 224.94)
        
    
if __name__ == '__main__':
    unittest.main()