# Generated by Django 4.2.6 on 2023-10-07 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('risk_assessment', '0001_initial'),
        ('fieldwork_setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditInProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_type', models.CharField(blank=True, max_length=100, null=True)),
                ('level_name', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.CharField(blank=True, max_length=100, null=True)),
                ('actual_start_date', models.DateField(blank=True, null=True)),
                ('start_audit_process', models.CharField(blank=True, max_length=100, null=True)),
                ('audit_procedure', models.CharField(blank=True, max_length=100, null=True)),
                ('move_to_audit_program', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('risk_details', models.CharField(blank=True, max_length=100, null=True)),
                ('response_action', models.CharField(blank=True, max_length=100, null=True)),
                ('risk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='risk_assessment.riskassessment')),
            ],
            options={
                'verbose_name': 'Risk Control Matrix (RCM)',
                'verbose_name_plural': 'Audit In Progress',
                'ordering': ['risk'],
            },
        ),
        migrations.CreateModel(
            name='AuditPorgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_details', models.CharField(blank=True, max_length=100, null=True)),
                ('response_action', models.CharField(blank=True, max_length=100, null=True)),
                ('audit_procedure', models.CharField(blank=True, max_length=100, null=True)),
                ('total_population', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sample_size', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('test_result', models.CharField(blank=True, max_length=100, null=True)),
                ('move_to_issue_control', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('issue_classification', models.CharField(blank=True, choices=[('Option 1', 'Option 1'), ('Option 2', 'Option 2')], max_length=100, null=True)),
                ('issue_description', models.CharField(blank=True, max_length=100, null=True)),
                ('impact', models.CharField(blank=True, max_length=100, null=True)),
                ('recommendation', models.CharField(blank=True, max_length=100, null=True)),
                ('audit_in_progress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fieldwork2.auditinprogress')),
                ('information_required', models.ManyToManyField(blank=True, to='fieldwork_setup.informationrequired')),
                ('management_comments', models.ManyToManyField(blank=True, to='fieldwork_setup.managementcomments')),
            ],
            options={
                'verbose_name': 'Audit Program',
                'verbose_name_plural': 'Audit Program',
            },
        ),
    ]
