# Generated by Django 4.2.6 on 2023-11-01 17:44

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='customer_name', unique=True)),
                ('customer_name', models.CharField(blank=True, max_length=20, null=True)),
                ('transaction_date', models.DateTimeField(auto_now=True, null=True)),
                ('quantity', models.FloatField(default=0.0)),
                ('payment_method', models.CharField(blank='True', choices=[('MP', 'MPESA'), ('VISA', 'VISA'), ('CS', 'CASH'), ('VM', 'VOOMA'), ('BK', 'BANK')], max_length=20, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('total_value', models.FloatField(blank=True, null=True)),
                ('amount_received', models.FloatField(default=False)),
                ('balance', models.FloatField(default=False)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='Served by')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='vendor', unique=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='Delivery Date')),
                ('quantity', models.FloatField(default=0.0)),
                ('delivery_status', models.CharField(choices=[('P', 'PENDING'), ('S', 'SUCCESSFUL')], default='P', max_length=3, verbose_name='Delivery Status')),
                ('price', models.FloatField(default=0.0, verbose_name='Price per item(Birr)')),
                ('total_value', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='accounts.vendor')),
            ],
            options={
                'ordering': ['order_date'],
            },
        ),
    ]
