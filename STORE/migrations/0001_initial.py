# Generated by Django 4.2.6 on 2023-10-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('decription', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='product_image')),
                ('category', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
