from django.db import models


class Category(models.Model):
    """
    Database model for product categories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Returns name of category
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns friendly name of category if it exists,
        otherwise return programmatic name
        """
        return self.friendly_name if self.friendly_name else self.name


class Brand(models.Model):
    """
    Database model for product brands, primarily used
    for pre-packaged candy
    """
    name = models.CharField(max_length=254)
    website = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        Returns name of brand
        """
        return self.name


class ProductTag(models.Model):
    """
    Database model for simple product tags, eg. flavors/colors
    to allow simplified searches
    """
    name = models.CharField(max_length=254)
    # If tag should be visible during search
    search_visible = models.BooleanField()

    def __str__(self):
        """
        Returns name of product tag
        """
        return self.name


class ProductVariant(models.Model):
    """
    Database model for product variants, mainly
    used for sizes eg. 1/4 lb, 1/2 lb and 1 lb bags
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    variant_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """
        Returns name of size
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns friendly name of size if it exists,
        otherwise return programmatic name
        """
        return self.friendly_name if self.friendly_name else self.name


class Product(models.Model):
    """
    Database model for products
    """
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    brand = models.ForeignKey(
        "Brand",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    product_variants = models.ManyToManyField(ProductVariant, blank=True)
    product_tags = models.ManyToManyField(ProductTag, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Returns name of product
        """
        return self.name

    def get_minimum_price(self):
        """
        Returns the lowest price of all product variants,
        if no variants are present, return normal price
        """
        if self.product_variants.exists():
            # Sorts variants by price and returns the first result
            min = self.product_variants.all().order_by('variant_price').first()
            return min.variant_price
        else:
            return self.price
