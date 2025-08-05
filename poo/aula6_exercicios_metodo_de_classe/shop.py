class Shop:
    tax : float = 0.02
   
    def __init__(self,gross_product_value : float) -> None:
        self.__gross_product_value = gross_product_value

    def set_gross_product_value(self,gross_product_value: float) -> None | ValueError:
        if gross_product_value:
            self.__gross_product_value = gross_product_value
        else:
            raise ValueError("Gross value product is invalid")

    def get_gross_product_value(self) -> float:
        return self.__gross_product_value + (self.__gross_product_value * Shop.tax)

    @classmethod
    def set_tax(cls,tax: float) -> None:
        if tax:
            cls.tax = tax
        else:
            raise ValueError("Tax is invalid")

    @classmethod
    def get_tax(cls) -> float:
        return cls.tax




