from django.db import models


class ProductImages(models.Model):

    id = models.AutoField(db_column="id", primary_key=True)
    product_id = models.IntegerField(db_column="product_id", blank=False)
    image_url = models.CharField(max_length=1000, db_column="image_url", blank=False)

    class Meta:
        db_table = "product_images"

    @classmethod
    def create(cls, product_id, image_url):
        db_row = cls(
            product_id=product_id,
            image_url=image_url
        )
        db_row.save()
        return db_row.id
