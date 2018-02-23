from django.db import models


class TestScrapyModel(models.Model):
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        app_label = 'JobWeb'
        db_table = 'job_scrapy_test'
