# Generated by Django 4.1.5 on 2023-03-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_sign_up_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='Address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
