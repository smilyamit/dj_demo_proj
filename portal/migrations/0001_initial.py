# Generated by Django 4.0.10 on 2023-12-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('installer_partner_cmy_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstallerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installer_vorname', models.CharField(max_length=60)),
                ('installer_nachname', models.CharField(max_length=60)),
                ('installer_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
