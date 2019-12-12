from django.db import models


class ProductDetails(models.Model):

    product_id = models.AutoField(db_column="product_id", primary_key=True)
    product_name = models.CharField(max_length=1000, db_column="product_name", blank=False)
    product_brand = models.CharField(max_length=1000, db_column="product_brand", blank=False)

    class Meta:
        db_table = "product_details"

    @classmethod
    def create(cls, product_name, product_brand):
        db_row = cls(
            product_name=product_name,
            product_brand=product_brand
        )
        db_row.save()
        return db_row.product_id
