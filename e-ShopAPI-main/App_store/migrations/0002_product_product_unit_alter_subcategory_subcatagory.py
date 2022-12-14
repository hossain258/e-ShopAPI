# Generated by Django 4.0.5 on 2022-08-23 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_unit',
            field=models.CharField(choices=[('Piece', 'Piece'), ('Packet', 'Packet'), ('BOX', 'BOX')], default=1, max_length=10, verbose_name='Product Unit Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='Subcatagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_cats', to='App_store.category'),
        ),
    ]
