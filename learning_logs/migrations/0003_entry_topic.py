# Generated by Django 3.0.7 on 2020-06-07 09:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning_logs.Topic'),
            preserve_default=False,
        ),
    ]
