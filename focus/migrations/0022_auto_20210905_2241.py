# Generated by Django 3.0.4 on 2021-09-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0021_auto_20210905_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item10_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item11_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item12_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item2_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item3_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item4_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item6_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item8_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focuscomplex1',
            name='fc1_item9_comm',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
    ]