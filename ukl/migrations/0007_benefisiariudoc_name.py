# Generated by Django 3.2.9 on 2023-03-04 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukl', '0006_alter_benefisiariuukl_eleitoral'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefisiariudoc',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
