# Generated by Django 5.1.7 on 2025-03-22 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('role_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChartOfAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255)),
                ('account_type', models.CharField(choices=[('Asset', 'Asset'), ('Liability', 'Liability'), ('Equity', 'Equity'), ('Revenue', 'Revenue'), ('Expense', 'Expense')], max_length=50)),
                ('parent_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.chartofaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_type', models.CharField(max_length=100)),
                ('company_kra_pin', models.CharField(max_length=100, unique=True)),
                ('company_contact', models.CharField(max_length=155)),
                ('company_mail', models.EmailField(max_length=200, unique=True)),
                ('company_address', models.CharField(max_length=100)),
                ('company_approval', models.BooleanField(default=False)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_companies', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role')),
            ],
            options={
                'unique_together': {('user', 'company')},
            },
        ),
        migrations.CreateModel(
            name='AccountsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255)),
                ('account_type', models.CharField(blank=True, max_length=100, null=True)),
                ('account_code', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('account_currency', models.CharField(blank=True, max_length=10, null=True)),
                ('account_opening', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(db_column='company_id', on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('company_user', models.ForeignKey(db_column='company_user_id', on_delete=django.db.models.deletion.CASCADE, to='api.companyuser')),
            ],
        ),
        migrations.CreateModel(
            name='ConsignmentInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consignment_no', models.CharField(max_length=255)),
                ('delivery_no', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.companyuser')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=200, unique=True)),
                ('debit', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chartofaccounts')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_invoice_no', models.CharField(max_length=255)),
                ('item_grade', models.CharField(max_length=100)),
                ('item_no_of_bags', models.PositiveIntegerField()),
                ('item_tare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_pallet_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_net_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_gross_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_comment', models.TextField(blank=True, null=True)),
                ('warranty_no', models.CharField(blank=True, max_length=255, null=True)),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.companyuser')),
                ('consignment_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.consignmentinventory')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInventoryTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broker', models.CharField(blank=True, max_length=255, null=True)),
                ('buyer', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sold_at', models.DateTimeField(blank=True, null=True)),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.companyuser')),
                ('item_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.iteminventory')),
            ],
        ),
        migrations.CreateModel(
            name='PriceSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_name', models.CharField(max_length=255)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('company_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.companyuser')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=50, unique=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('purchase_order', models.ForeignKey(db_column='po_id', on_delete=django.db.models.deletion.CASCADE, to='api.purchaseorders')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(db_column='company_id', on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('item_inventory', models.ForeignKey(db_column='item_inventory_id', on_delete=django.db.models.deletion.CASCADE, to='api.iteminventory')),
            ],
        ),
        migrations.CreateModel(
            name='ChargesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_name', models.CharField(blank=True, max_length=255, null=True)),
                ('item_name', models.CharField(blank=True, max_length=255, null=True)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('units', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('company', models.ForeignKey(db_column='company_id', on_delete=django.db.models.deletion.CASCADE, to='api.company')),
                ('item_inventory', models.ForeignKey(db_column='item_inventory_id', on_delete=django.db.models.deletion.CASCADE, to='api.iteminventory')),
                ('transaction', models.ForeignKey(db_column='transaction_id', on_delete=django.db.models.deletion.CASCADE, to='api.transactionitem')),
            ],
        ),
    ]
