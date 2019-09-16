import unittest
from Acme import Product
from Acme_report import generate_products, adjectives, nouns

class AcmeProductTests(unittest.TestCase):
    """Ensuring Acme products are top of the line!"""

    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertIsInstance(prod.price, int)

    def test_default_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        self.assertIsInstance(prod.weight, int)

    def test_default_flammability(self):
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)
        self.assertIsInstance(prod.flammability, float)

    def test_steability(self):
        steal1 = Product('steal1', 10, 20)
        steal2 = Product('steal2', 5, 20)
        steal3 = Product('steal3', 20, 20)
        steal4 = Product('steal4', 21, 20)

        self.assertEqual(steal1.stealability(), "Kinda stealable.")
        self.assertEqual(steal2.stealability(), "Not so stealable...")
        self.assertEqual(steal3.stealability(), "Very stealable!")
        self.assertEqual(steal4.stealability(), "Very stealable!")

    def test_explode(self):
        explode1 = Product('explode1', 0, 10, 0.5)
        explode2 = Product('explode2', 0, 20, 0.5)
        explode3 = Product('explode3', 0, 49, 1)
        explode4 = Product('explode4', 0, 50, 1)

        self.assertEqual(explode1.explode(), "...fizzle.")
        self.assertEqual(explode2.explode(), "...boom!")
        self.assertEqual(explode3.explode(), "...boom!")
        self.assertEqual(explode4.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        prod_list = generate_products()
        self.assertEqual(len(prod_list), 30)

    def test_legal_names(self):
        prod_list = generate_products()
        names = [prod.name for prod in prod_list]

        for name in names:
            self.assertEqual(name.count(' '), 1)
            self.assertEqual(len(name.split()), 2)
            self.assertIn(name.split()[0], adjectives)
            self.assertIn(name.split()[1], nouns)


if __name__ == '__main__':
    unittest.main()
