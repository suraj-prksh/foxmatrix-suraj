# Generated by Django 5.0.6 on 2024-05-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationotp',
            name='expires_at',
            field=models.DateTimeField(null=True),
        ),
    ]
