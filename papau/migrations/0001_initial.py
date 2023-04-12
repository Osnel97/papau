# Generated by Django 4.2 on 2023-04-12 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('agent_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('license_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False)),
                ('property_type', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('square_footage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('listing_date', models.DateField()),
                ('listing_status', models.CharField(max_length=20)),
                ('listing_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papau.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=20)),
                ('transaction_date', models.DateField()),
                ('transaction_status', models.CharField(max_length=20)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('buyer_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_transactions', to='papau.agent')),
                ('buyer_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_transactions', to='papau.client')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papau.property')),
                ('seller_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_transactions', to='papau.agent')),
                ('seller_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_transactions', to='papau.client')),
            ],
        ),
    ]