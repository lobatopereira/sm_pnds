# Generated by Django 3.2.9 on 2023-03-03 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_anofiscal'),
        ('ukl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyukl',
            name='aldeia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.aldeia', verbose_name="Survey iha Aldeia ne'ebe?"),
        ),
    ]
