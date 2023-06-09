# Generated by Django 2.1.7 on 2019-09-13 21:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=None, max_length=56, null=True)),
                ('label', models.CharField(default=None, max_length=256, null=True)),
                ('description', models.CharField(default=None, max_length=1024, null=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('subtract', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft', models.BooleanField(default=True)),
                ('refunded', models.BooleanField(default=False)),
                ('refund_type', models.CharField(default=None, max_length=56, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=None, max_length=56, null=True)),
                ('tran_date', models.DateTimeField(default=None, null=True)),
                ('tran_id', models.CharField(default=None, max_length=128, null=True)),
                ('val_id', models.CharField(default=None, max_length=128, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('store_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('card_type', models.CharField(default=None, max_length=128, null=True)),
                ('card_no', models.CharField(default=None, max_length=128, null=True)),
                ('currency', models.CharField(default=None, max_length=128, null=True)),
                ('bank_tran_id', models.CharField(default=None, max_length=128, null=True)),
                ('card_issuer', models.CharField(default=None, max_length=128, null=True)),
                ('card_brand', models.CharField(default=None, max_length=128, null=True)),
                ('currency_type', models.CharField(default=None, max_length=128, null=True)),
                ('currency_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('risk_level', models.IntegerField(default=None, null=True)),
                ('risk_title', models.CharField(default=None, max_length=56, null=True)),
                ('verified', models.BooleanField(default=False, null=True)),
                ('invoice', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='associated_invoice', to='transactions.Invoice')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='associated_payment', to='transactions.Payment'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='reservation',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice_reservation', to='reservations.Reservation'),
        ),
    ]
