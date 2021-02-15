# Generated by Django 3.1.6 on 2021-02-15 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], max_length=10, null=True)),
                ('alcohol', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('icon_image', models.ImageField(blank=True, default=home.models.get_default_icon_image, null=True, upload_to=home.models.get_icon_image_file_path)),
                ('major_image', models.ImageField(blank=True, default=home.models.get_default_major_iamge, null=True, upload_to=home.models.get_major_image_file_path)),
                ('major_description', models.CharField(blank=True, max_length=40, null=True)),
                ('secondary_image', models.ImageField(blank=True, default=home.models.get_default_secondary_iamge, null=True, upload_to=home.models.get_secondary_image_file_path)),
                ('secondary_description', models.CharField(blank=True, max_length=40, null=True)),
                ('tertiary_image', models.ImageField(blank=True, default=home.models.get_default_tertiary_iamge, null=True, upload_to=home.models.get_tertiary_image_file_path)),
                ('tertiary_description', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True)),
                ('course', models.CharField(choices=[('Beverage', 'Beverage'), ('Starter', 'Starter'), ('Main-Course', 'Main-Course'), ('Dessert', 'Dessert')], max_length=65, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('total_amount', models.FloatField(null=True)),
                ('table_number', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Canelled', 'Canelled')], default='Pending', max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('ordered_dish', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dish', to='home.dishes')),
            ],
        ),
        migrations.AddField(
            model_name='dishes',
            name='food_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.tag'),
        ),
    ]
