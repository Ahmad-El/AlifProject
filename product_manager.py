class ProductList:
    def __init__(self, filename):
        self.filename = filename

    def _read_products(self):
        try:
            with open(self.filename, 'r') as file:
                return [line.strip().split(' — ') for line in file if line.strip()]
        except FileNotFoundError:
            return []

    def _write_products(self, products):
        with open(self.filename, 'w') as file:
            for name, price in products:
                file.write(f"{name} — {price}\n")

    def add_product(self, name, price):
        products = self._read_products()
        products.append((name, str(price)))
        self._write_products(products)
        print(f"Added product: {name} — {price}")

    def update_product(self, name, new_price):
        products = self._read_products()
        for i, (product_name, _) in enumerate(products):
            if product_name == name:
                products[i] = (name, str(new_price))
                self._write_products(products)
                print(f"Updated product: {name} — {new_price}")
                return
        print(f"Product {name} not found.")

    def delete_product(self, name):
        products = self._read_products()
        products = [p for p in products if p[0] != name]
        self._write_products(products)
        print(f"Deleted product: {name}")

    def calculate_sum(self):
        products = self._read_products()
        return sum(int(price) for _, price in products)
