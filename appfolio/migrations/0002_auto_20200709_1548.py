# Generated by Django 3.0.8 on 2020-07-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_email',
            field=models.EmailField(blank=True, default='hidden', max_length=50),
        ),
    ]
