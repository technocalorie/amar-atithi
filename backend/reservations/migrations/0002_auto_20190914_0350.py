# Generated by Django 2.1.7 on 2019-09-13 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0001_initial'),
        ('places', '0003_auto_20190914_0350'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='invoice',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='res_invoice', to='transactions.Invoice'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='place',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Place'),
        ),
    ]
