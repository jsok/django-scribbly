from pricing.models import DiscountMatrixEntry

class PricedProduct:
    """
    An object describing a product which can be queried for a price,
    whose value is calculated by looking up the appropriate discount
    from the discount matrix.
    """

    product = None
    customer = None

    def __init__(self, product_model, customer_model):
        self.product = product_model
        self.customer = customer_model

    @property
    def name(self):
        return self.product.name

    @property
    def sku(self):
        return self.product.sku

    @property
    def retail_price(self):
        return self.product.price

    @property
    def discount(self):
        product_category = self.product.price_category
        customer_category = self.customer.customer_category

        try:
            discount_entry = DiscountMatrixEntry.objects.get(
                    product_category=product_category,
                    customer_category=customer_category)
        except DiscountMatrixEntry.DoesNotExist:
            return 0.0

        return discount_entry.discount

    @property
    def discount_as_percent_str(self):
        return "%s%%" % (self.discount * 100.00)

    @property
    def discounted_price(self):
        price = self.retail_price * (1 - self.discount)
        return price

    @property
    def on_hand(self):
        if self.customer.user.is_staff:
            return self.product.inventory_item.on_hand
        else:
            return self.product.inventory_item.on_hand_fuzzy

def get_products_for_taxon(taxon, customer):
    priced_products = {}

    for product in taxon.get_products():
        pp = PricedProduct(product, customer)
        priced_products[product.id] = pp

    for child in taxon.get_children():
        child_products = get_products_for_taxon(child, customer)
        priced_products.update(child_products)

    return priced_products

