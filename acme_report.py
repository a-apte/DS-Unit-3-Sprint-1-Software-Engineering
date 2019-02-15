#!/usr/bin/env python

import random as rand
from acme import *

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

n_prod_default = 30

def generate_products(n_products = n_prod_default):
    """Produces a random list of n_products of class Product"""
    
    a = 1000000
    b = 9999999
    prod_list = []

    for i in range(n_products):
        name = rand.choice(ADJECTIVES) + rand.choice(NOUNS)
        price = rand.randint(5,100)
        weight = rand.randint(5,100)
        flammability = rand.uniform(0.0,2.5)
        identifier = rand.randint(a,b)
        product = Product(name, price, weight, flammability, identifier)
        prod_list.append(product)
    return prod_list

def inventory_report(product_list):
    """Takes a list of products and produces a summary"""
    N = len(product_list)
    names = [p.name for p in product_list]
    unique_names = len(set(names))
    avg_price = sum(p.price for p in product_list) / N
    avg_weight = sum(p.weight for p in product_list) / N
    avg_flam = sum(p.flammability for p in product_list) / N

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT") 
    print("Unique product names:",unique_names)
    print("Average price:", avg_price)
    print("Average weight:", avg_weight)
    print("Average flammability:", avg_flam)


if __name__ == '__main__':
    inventory_report(generate_products())