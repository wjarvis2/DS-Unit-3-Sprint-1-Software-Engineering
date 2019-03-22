import unittest
from acme import Product
import acme_report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)



    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)



    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_default_stealability_and_explosive_quality(self):
        """ Test default product stealability and explosive quality"""
        prod = Product('Test Product')
        stealable = prod.stealability()
        explosive = prod.explode()
        self.assertEqual(stealable, 'Kinda stealable')
        self.assertEqual(explosive, '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Test report functions"""
    def test_default_n_products(self):
        """Test default n_items = 30"""
        test_n_items = acme_report.generate_products()
        self.assertEqual(len(test_n_items), 30)
    
    def test_legal_names(self):
        """Test legal names"""
        product_names = acme_report.generate_products()
        descriptor_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
        for i in range(len([product_names])):
            test_product_name = product_names[i].name
            divided_list = test_product_name.split()
            self.assertIn(divided_list[0],descriptor_list)
            self.assertIn(divided_list[1],noun_list)



if __name__ == '__main__':
    unittest.main()