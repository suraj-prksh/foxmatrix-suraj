# Generated by Django 5.0.6 on 2024-05-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_verificationotp_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationotp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
