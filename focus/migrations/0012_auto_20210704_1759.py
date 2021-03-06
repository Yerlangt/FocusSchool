# Generated by Django 3.0.4 on 2021-07-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0011_focusplan1_fp1_item2'),
    ]

    operations = [
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_additional',
            field=models.CharField(default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_item3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_item4',
            field=models.IntegerField(choices=[(1, 'Взаимосвязь темы с другими темами и разделами учебной программы'), (2, 'Преемственность темы урока и непрерывности ее изучения'), (3, 'Межпредметные связи учебной программы'), (4, 'Идеи авторской программы'), (5, 'Идеи авторской методики')], default=1),
        ),
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_item5',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_item6',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_item7',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_review',
            field=models.CharField(default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='focusplan1',
            name='fp1_review_pdg',
            field=models.CharField(default=' ', max_length=150),
        ),
    ]
