# Generated by Django 2.0.3 on 2018-03-13 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioSecurity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bioSecurity', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cow_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cow_no', models.IntegerField(default=0)),
                ('cow_weight', models.IntegerField(default=0)),
                ('cow_milk', models.IntegerField(default=0)),
                ('cow_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CowFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=100, verbose_name='মিশ্রণ তালিকা')),
                ('cornMix', models.IntegerField(default=0, verbose_name='ভুট্টা ভাংগা')),
                ('wheatMix', models.IntegerField(default=0, verbose_name='গম ভাংগা')),
                ('wheatBhushi', models.IntegerField(default=0, verbose_name='গমের ভুষি')),
                ('riceBran', models.IntegerField(default=0, verbose_name='রাইস ব্রান')),
                ('dalMix', models.IntegerField(default=0, verbose_name='ডাল ভাংগা')),
                ('dalBhushi', models.IntegerField(default=0, verbose_name='ডাল ভুষি')),
                ('khoil', models.IntegerField(default=0, verbose_name='খৈল')),
                ('limestonDCP', models.IntegerField(default=0, verbose_name='লাইমস্টোন/ডি,সি,পি')),
                ('soda', models.IntegerField(default=0, verbose_name='সোডা')),
                ('salt', models.IntegerField(default=0, verbose_name='লবণ')),
                ('vitamin', models.IntegerField(default=0, verbose_name='ভিটামিন প্রিমিক্স')),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cowNo', models.CharField(max_length=100, verbose_name='গরু নং ')),
            ],
        ),
        migrations.CreateModel(
            name='FMDSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ScheduleTime', models.DateTimeField(null=True, verbose_name='ক্ষুরারােগ টিকা প্রদাণের সময়')),
                ('NextScheduleTime', models.DateTimeField(null=True, verbose_name='পরবর্তী প্রদাণের তারিখ')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FMD', to='home.DiseaseManagement')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=200)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('image', models.ImageField(height_field='height', upload_to='', width_field='width')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='VaccineSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccinename', models.CharField(max_length=100, verbose_name='টিকার নাম')),
                ('vaccinedose', models.CharField(max_length=100, verbose_name='প্রয়োগ মাত্রা')),
                ('vaccineInterval', models.CharField(max_length=100, verbose_name='কতদিন পর পর')),
                ('eligableAge', models.CharField(max_length=100, verbose_name='কোন বয়সে')),
                ('pushingPosition', models.CharField(max_length=100, verbose_name='প্রয়ােগ স্থান')),
                ('preserveTemp', models.CharField(max_length=100, verbose_name='সংরক্ষণ তাপমাত্রা')),
            ],
        ),
    ]
