# Generated by Django 2.0.3 on 2018-04-03 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180403_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odgovori',
            name='vprasanje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='odg', to='api.Vprasanja'),
        ),
    ]
