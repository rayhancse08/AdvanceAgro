# Generated by Django 2.0.3 on 2018-04-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_cowdetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cowfood',
            options={'verbose_name_plural': 'Rationing Formula'},
        ),
        migrations.AddField(
            model_name='cowdetail',
            name='collected_time_info',
            field=models.TextField(null=True, verbose_name='সংগ্রহকালীন তথ্য'),
        ),
        migrations.AlterField(
            model_name='cowdetail',
            name='status',
            field=models.CharField(choices=[('M', 'Milking'), ('D', 'Dry Preiod'), ('C', 'Calf')], max_length=1, verbose_name='গরুর ধরন'),
        ),
    ]
