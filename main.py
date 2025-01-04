import sys
from product_manager import ProductList

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <filename> <action> [args...]")
        sys.exit(1)

    filename = sys.argv[1]
    action = sys.argv[2].lower()
    product_list = ProductList(filename)

    if action == 'add':
        if len(sys.argv) < 5:
            print("Usage: python main.py <filename> add <name> <price>")
            sys.exit(1)
        name = sys.argv[3]
        price = int(sys.argv[4])
        product_list.add_product(name, price)
    elif action == 'update':
        if len(sys.argv) < 5:
            print("Usage: python main.py <filename> update <name> <new_price>")
            sys.exit(1)
        name = sys.argv[3]
        new_price = int(sys.argv[4])
        product_list.update_product(name, new_price)
    elif action == 'delete':
        if len(sys.argv) < 4:
            print("Usage: python main.py <filename> delete <name>")
            sys.exit(1)
        name = sys.argv[3]
        product_list.delete_product(name)
    elif action == 'sum':
        total = product_list.calculate_sum()
        print(f"Total sum of prices: {total}")
    else:
        print("Invalid action. Available actions: add, update, delete, sum")

if __name__ == "__main__":
    main()
