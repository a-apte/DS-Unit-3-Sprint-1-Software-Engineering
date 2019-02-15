#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


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

    def test_default_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertAlmostEqual(prod.flammability, 0.5, places = 5)

    def test_stealability(self):
        """Tests that stealability method works correctly"""
        prod1 = Product('Test Product', price = 50, weight = 10)
        prod2 = Product('Test Product', price = 10, weight = 50)
        prod3 = Product('Test Product', price = 60, weight = 80)
        self.assertEqual(prod1.stealability(), "Very stealable!")
        self.assertEqual(prod2.stealability(), "Not so stealable...")
        self.assertEqual(prod3.stealability(), "Kinda stealable.")

    def test_explode(self):
        """Tests that explode method works correctly"""
        prod1 = Product('Test Product', weight = 5, flammability=1.0)
        prod2 = Product('Test Product', weight = 10, flammability=1.0)
        prod3 = Product('Test Product', weight = 50, flammability=1.0)
        self.assertEqual(prod1.explode(), "...fizzle")
        self.assertEqual(prod2.explode(), "...BABOOM!!")
        self.assertEqual(prod3.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_num_products(self):
        """Tests to see if the number of default products is 30"""
        self.assertEqual(acme_report.n_prod_default, 30)

    def test_legal_names(self):
        """ Tests to see if the names in name list are legal names"""
        prod_list = generate_products()
        names = [p.name for p in prod_list]
        adj_name = []
        noun_name = []
        for name in names:
            adj, noun = name.split()
            adj_name.append(adj)
            noun_name.append(noun)
        for adj in adj_name:
            self.assertIn(adj, ADJECTIVES)
        for noun in noun_name:
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()