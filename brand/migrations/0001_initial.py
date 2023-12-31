# Generated by Django 4.2.5 on 2023-10-04 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandShapka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('photo', models.ImageField(blank=True, upload_to='ports/')),
                ('is_visible', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ports', to='brand.portfolio')),
            ],
        ),
    ]
