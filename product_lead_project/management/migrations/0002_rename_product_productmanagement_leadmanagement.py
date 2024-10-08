# Generated by Django 5.1.1 on 2024-09-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductManagement',
        ),
        migrations.CreateModel(
            name='LeadManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('interested_products', models.ManyToManyField(related_name='leads', to='management.productmanagement')),
            ],
        ),
    ]
