from Models.product import Product

class ProductHelper:
    
    @staticmethod
    def create_item_from_text(file_path):
        products = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    attributes = line.split(',')
                    
                    if len(attributes) >= 2:
                        name = attributes[0].strip()
                        price = float(attributes[1].strip())  
                        quantity = int(attributes[2].strip()) if len(attributes) > 2 else 1
                        brand = attributes[3].strip() if len(attributes) > 3 else None

                        product = Product(name, price, quantity, brand)
                        products.append(product)
                    else:
                        print(f"invalid row: {line}")
        except FileNotFoundError:
            print(f"Error: File {file_path} Not found.")
        
        return products

    @staticmethod
    def get_total_balance(products):
        total_balance = 0
        
        for product in products:
            total_balance += product.get_total_price()
        
        total_balance_with_tax = total_balance * 1.20
        
        return total_balance_with_tax
    
    @staticmethod
    def display_product_info(products):
        for product in products:
            print(product)
            print("-" * 50)