# Generated by Django 2.0.3 on 2018-04-01 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20180401_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseasemanagement',
            name='cow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Cow', verbose_name='গরু নং'),
        ),
        migrations.AddField(
            model_name='diseasemanagement',
            name='disease',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Disease', verbose_name='িকার নাম'),
        ),
        migrations.AlterField(
            model_name='cow',
            name='cow_no',
            field=models.CharField(max_length=100, null=True, verbose_name='গরু নং '),
        ),
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='টিকার নাম'),
        ),
    ]
