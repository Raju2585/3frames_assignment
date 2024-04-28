#I've added code in the below. Python product configuration system with a tiny footprint, with Amazon-like search capabilities
# and effective in-memory storage provided by the solution. For flexible product representation,
# it defines a Product class, and for product management, it defines a ProductConfiguration class. The system prioritizes
# performance, flexibility, and simplicity with features for adding products and searching by name or category.

class Product:
    def __init__(self, name, category, description, details, price):
        self.name = name
        self.category = category
        self.description = description
        self.details = details
        self.price = price

class Configuration:
    def __init__(self):
        self.products = {}  # In-memory storage for products

    def add_product(self, pro_id, prod):
        self.products[pro_id] = prod

    def search_by_name(self, key):
        res = []
        for prod_id, prod in self.products.items():
            if key.lower() in prod.name.lower():
                res.append(prod)
        return res

    def search_by_category(self, ctg):
        res = []
        for prod_id, prod in self.products.items():
            if ctg.lower() == prod.category.lower():
                res.append(prod)
        return res

config = Configuration()

# Adding products
config.add_product(1, Product("Laptop", "Electronics", "Powerful laptop", {"Brand": "HP"}, 1000))
config.add_product(2, Product("Smartphone", "Electronics", "Latest smartphone", {"Brand": "Samsung"}, 800))
config.add_product(3, Product("Book", "Books", "Bestseller book", {"Author": "John Doe"}, 20))

# Searching for products
search_results = config.search_by_name("laptop")
print("search results:")
for product in search_results:
    print(product.name, product.category, product.price)

category_results = config.search_by_category("electronics")
print("search results:")
for product in category_results:
    print(product.name, product.category, product.price)
