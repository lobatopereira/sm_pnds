# Generated by Django 3.2.9 on 2023-03-03 13:49

import custom.utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ukl', '0003_auto_20230303_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenefisiariuDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=custom.utils.upload_doc_benefit, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Upload Dokumentu')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('benefisiariu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benefitdoc', to='ukl.benefisiariuukl')),
                ('user_created', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
