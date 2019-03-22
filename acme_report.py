from acme import Product
import random


def generate_products(n_products=30):
    products = {}
    for i in range(n_products):
        descriptors = ['Awesome', 'Shiny', 'Portable', 'Improved']
        nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        descript = random.choice(descriptors)
        noun = random.choice(nouns)


        name = '{} {}'.format(descript, noun)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5) 


        products[i] = Product(name, price, weight, flammability)

    return products



def inventory_report(prod_list):
    names = []
    prices = []
    weights = []
    flammability_ratings = []



    for i in range(len(prod_list)):
        names.append(prod_list[i].name)
        prices.append(prod_list[i].price)
        weights.append(prod_list[i].weight)
        flammability_ratings.append(prod_list[i].flammability)

    product_names = set(names)

    def average_calc(value):
        return sum(value) / len(value)

    print ('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print ('Unique product names:', len(product_names))
    print ('Average price:', average_calc(prices))
    print ('Average weight:', average_calc(weights))
    print ('Average flammability rating:', average_calc(flammability_ratings))

if __name__ == '__main__':
    inventory_report(generate_products())


