from django.db import models


class ProductCategories(models.Model):

    id = models.AutoField(db_column="id", primary_key=True)
    product_id = models.IntegerField(db_column="product_id", blank=False)
    category = models.CharField(max_length=1000, db_column="category", blank=False)

    class Meta:
        db_table = "product_categories"

    @classmethod
    def create(cls, product_id, category):
        db_row = cls(
            product_id=product_id,
            category=category
        )
        db_row.save()
        return db_row.id
