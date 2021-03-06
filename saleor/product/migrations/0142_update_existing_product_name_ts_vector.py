# Generated by Django 3.1.5 on 2021-02-05 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0141_update_product_ts_vector"),
    ]

    operations = [
        migrations.RunSQL(
            """
            UPDATE product_product
            SET search_vector =
            setweight(to_tsvector('pg_catalog.english', coalesce(name, '')), 'A') ||
            setweight(
            to_tsvector('pg_catalog.english', coalesce(description_plaintext, '')), 'B'
            );
            """
        ),
    ]
