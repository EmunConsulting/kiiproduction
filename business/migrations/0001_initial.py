# Generated by Django 5.0.7 on 2024-08-31 11:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopmentStageList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('development_stage', models.CharField(max_length=100, unique=True, verbose_name='Development Stage')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndustrySectorList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('industry_sector', models.CharField(max_length=100, unique=True, verbose_name='Industry Sector')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BusinessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('business_model', models.CharField(max_length=200, null=True, verbose_name='Business Model')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Name')),
                ('location', models.CharField(max_length=200, null=True, verbose_name='Location')),
                ('progress_metrics', models.CharField(max_length=200, null=True, verbose_name='Progress Metrics')),
                ('start_date', models.DateField()),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('development_stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='business.developmentstagelist')),
                ('industry_sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='business.industrysectorlist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutcomeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('milestone_achieved', models.TextField()),
                ('revenue', models.PositiveIntegerField()),
                ('exit_strategy', models.TextField()),
                ('business_record', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.businessrecord')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegistrationStatusList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('registration_status', models.CharField(max_length=100, unique=True, verbose_name='Registration Status')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='businessrecord',
            name='registration_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='business.registrationstatuslist'),
        ),
        migrations.CreateModel(
            name='ServicesProductsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('service_products', models.CharField(max_length=100, unique=True, verbose_name='Service/Products')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='businessrecord',
            name='services_products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='business.servicesproductslist'),
        ),
    ]
