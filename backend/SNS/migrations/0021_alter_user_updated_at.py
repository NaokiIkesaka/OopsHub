# Generated by Django 5.0.3 on 2024-05-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNS', '0020_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
