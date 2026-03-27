class ProductError(Exception):
    pass
class ProductAlreadyExists(ProductError):
    pass
class ProductDoesntExists(ProductError):
    pass