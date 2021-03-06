# Generated by Django 2.1.5 on 2019-02-13 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190209_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='products.Color', verbose_name='kleur'),
        ),
        migrations.AddField(
            model_name='price',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='products.Size', verbose_name='afmeting'),
        ),
    ]
