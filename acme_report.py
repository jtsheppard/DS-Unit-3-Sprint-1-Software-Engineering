import random
from acme import Product


adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Sword']


def generate_names(adjectives, nouns):
    name = random.sample(adjectives, 1)[0] + ' ' + random.sample(nouns, 1)[0]
    return name


def generate_products(num_products=30):
    products = []
    for p in range(30):
        x = Product(name=generate_names(adjectives, nouns),
                    price=random.randint(5, 100),
                    weight=random.randint(5, 100),
                    flammability=random.uniform(0.0, 2.5))
        products.append(x)

    return products


def inventory_report(products):
    prices = []
    weights = []
    flams = []
    for p in products:
        prices.append(p.price)
        weights.append(p.weight)
        flams.append(p.flammability)
    price_avg = sum(prices) / len(prices)
    weight_avg = sum(weights) / len(weights)
    flam_avg = sum(flams) / len(flams)

    print(price_avg, weight_avg, flam_avg)


if __name__ == '__main__':
    inventory_report(generate_products())
