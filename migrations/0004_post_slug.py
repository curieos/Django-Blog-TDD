# Generated by Django 2.2.2 on 2019-06-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190616_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default', editable=False),
            preserve_default=False,
        ),
    ]
