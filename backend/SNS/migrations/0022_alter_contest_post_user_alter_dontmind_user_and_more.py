# Generated by Django 5.0.3 on 2024-05-19 02:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNS', '0021_alter_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest_post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SNS.user'),
        ),
        migrations.AlterField(
            model_name='dontmind',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SNS.user'),
        ),
        migrations.AlterField(
            model_name='learned',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SNS.user'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SNS.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SNS.user'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SNS.user'),
        ),
    ]
