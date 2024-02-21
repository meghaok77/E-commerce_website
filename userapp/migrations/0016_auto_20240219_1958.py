# Generated by Django 3.2.7 on 2024-02-19 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_product'),
        ('userapp', '0015_auto_20240219_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carttotal',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.userdetails'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='uid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.userdetails'),
        ),
    ]