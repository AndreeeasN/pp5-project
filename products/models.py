from django.db import models


class Category(models.Model):
    """
    Database model for product categories
    """
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
        return self.name


class ProductTag(models.Model):
    """
    Database model for simple product tags, eg. flavors/colors
    to allow simplified searches
    """
    name = models.CharField(max_length=254)
    # Should tag be visible during search?
    search_visible = models.BooleanField()

    def __str__(self):
        return self.name

    def get_search_visible(self):
        return self.search_visible


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
    product_tags = models.ManyToManyField(ProductTag, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
