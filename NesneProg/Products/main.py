from Helpers.product_helper import ProductHelper

products = ProductHelper.create_item_from_text('products.txt')

ProductHelper.display_product_info(products)

total_balance = ProductHelper.get_total_balance(products)
print(f"Total Price (KDV with the inclusion): ${total_balance:.2f}")
