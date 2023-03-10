# Generated by Django 4.1.1 on 2023-02-21 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rental_price_per_day', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('book_status', models.CharField(blank=True, choices=[('available', 'available'), ('sold', 'sold'), ('rented', 'rented')], max_length=50, null=True)),
                ('rental_period', models.IntegerField(blank=True, null=True)),
                ('activity', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='libapp.category')),
            ],
        ),
    ]
