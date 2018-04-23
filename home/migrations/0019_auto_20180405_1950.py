# Generated by Django 2.0.3 on 2018-04-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20180405_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter File Name', max_length=200, verbose_name='Doc Name')),
                ('file', models.FileField(default=False, help_text='Upload File', upload_to='')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['upload_time'],
            },
        ),
        migrations.AlterField(
            model_name='foodmanagement',
            name='grass',
            field=models.FloatField(default=0, verbose_name='ঘাস(কে.জি)'),
        ),
        migrations.AlterField(
            model_name='foodmanagement',
            name='khor',
            field=models.FloatField(default=0, verbose_name='খড়(কে.জি)'),
        ),
    ]