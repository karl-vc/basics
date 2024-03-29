# Generated by Django 2.0.6 on 2019-09-25 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_siteuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('userFullName', models.CharField(default='', max_length=200)),
                ('userEmail', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('userPassword', models.CharField(default='', max_length=200)),
                ('userImage', models.CharField(default='', max_length=200)),
                ('userMobile', models.BigIntegerField()),
                ('isActive', models.BooleanField(default=True)),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.UserRole')),
            ],
        ),
    ]
