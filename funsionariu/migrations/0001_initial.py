# Generated by Django 3.2.9 on 2023-03-01 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funsionariu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran', models.CharField(max_length=200, null=True)),
                ('seksu', models.CharField(blank=True, choices=[('Mane', 'Mane'), ('Feto', 'Feto')], max_length=10, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('nu_telefone', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='funsionariu')),
                ('tipu_f', models.CharField(blank=True, choices=[('Dir', 'Diretor'), ('Fun', 'Funsionariu'), ('EIP', 'Ekipa Implementasaun Programa')], max_length=30, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('administrativepost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AdministrativePost', to='custom.administrativepost')),
                ('aldeia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom.aldeia')),
                ('areaadministrativepost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AreaAdministrativePost', to='custom.administrativepost')),
                ('areamunicipality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AreaMunicipality', to='custom.municipality')),
                ('areavillage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AreaVillage', to='custom.village')),
                ('municipality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Municipality', to='custom.municipality')),
            ],
        ),
        migrations.CreateModel(
            name='Pozisaun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naran', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFunsionariu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('hashed', models.CharField(blank=True, max_length=32, null=True)),
                ('funsionariu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='funsionariu.funsionariu')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userFunsionariu', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='funsionariu',
            name='pozisaun',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funsionariu.pozisaun'),
        ),
        migrations.AddField(
            model_name='funsionariu',
            name='user_created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='funsionariu',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Village', to='custom.village'),
        ),
    ]
