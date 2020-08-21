# Generated by Django 3.0.8 on 2020-08-19 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('published', models.BooleanField(default=False)),
                ('article_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('text', models.TextField(blank=True)),
                ('goal', models.CharField(max_length=100, null=True)),
                ('goalText', models.TextField(blank=True)),
                ('languages', models.CharField(blank=True, max_length=100, null=True)),
                ('languagesText', models.TextField(blank=True)),
                ('softwares', models.CharField(blank=True, max_length=100)),
                ('softwaresText', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appfolio.PostCategory')),
            ],
        ),
    ]
