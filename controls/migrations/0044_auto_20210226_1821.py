# Generated by Django 3.0.11 on 2021-02-26 18:21

import auto_prefetch
from django.db import migrations
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0043_merge_20210203_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commoncontrol',
            options={'base_manager_name': 'prefetch_manager'},
        ),
        migrations.AlterModelOptions(
            name='deployment',
            options={'base_manager_name': 'prefetch_manager'},
        ),
        migrations.AlterModelOptions(
            name='element',
            options={'base_manager_name': 'prefetch_manager'},
        ),
        migrations.AlterModelOptions(
            name='system',
            options={'base_manager_name': 'prefetch_manager'},
        ),
        migrations.AlterModelOptions(
            name='systemassessmentresult',
            options={'base_manager_name': 'prefetch_manager'},
        ),
        migrations.AlterModelManagers(
            name='commoncontrol',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='deployment',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='element',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='elementcommoncontrol',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='elementcontrol',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='statement',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='system',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='systemassessmentresult',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='commoncontrol',
            name='common_control_provider',
            field=auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controls.CommonControlProvider'),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='system',
            field=auto_prefetch.ForeignKey(blank=True, help_text='The system associated with the deployment', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deployments', to='controls.System'),
        ),
        migrations.AlterField(
            model_name='element',
            name='import_record',
            field=auto_prefetch.ForeignKey(blank=True, help_text='The Import Record which created this Element.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='import_record_elements', to='controls.ImportRecord'),
        ),
        migrations.AlterField(
            model_name='elementcommoncontrol',
            name='common_control',
            field=auto_prefetch.ForeignKey(help_text='The Common Control for this association.', on_delete=django.db.models.deletion.CASCADE, related_name='element_common_control', to='controls.CommonControl'),
        ),
        migrations.AlterField(
            model_name='elementcommoncontrol',
            name='element',
            field=auto_prefetch.ForeignKey(help_text='The Element (e.g., System, Component, Host) to which common controls are associated.', on_delete=django.db.models.deletion.CASCADE, related_name='common_controls', to='controls.Element'),
        ),
        migrations.AlterField(
            model_name='elementcontrol',
            name='element',
            field=auto_prefetch.ForeignKey(help_text='The Element (e.g., System, Component, Host) to which controls are associated.', on_delete=django.db.models.deletion.CASCADE, related_name='controls', to='controls.Element'),
        ),
        migrations.AlterField(
            model_name='historicaldeployment',
            name='system',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The system associated with the deployment', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.System'),
        ),
        migrations.AlterField(
            model_name='historicalstatement',
            name='consumer_element',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The element the statement is about.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.Element'),
        ),
        migrations.AlterField(
            model_name='historicalstatement',
            name='import_record',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The Import Record which created this Statement.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.ImportRecord'),
        ),
        migrations.AlterField(
            model_name='historicalstatement',
            name='parent',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='Parent statement', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.Statement'),
        ),
        migrations.AlterField(
            model_name='historicalstatement',
            name='producer_element',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The element producing this statement.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.Element'),
        ),
        migrations.AlterField(
            model_name='historicalstatement',
            name='prototype',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='Prototype statement', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.Statement'),
        ),
        migrations.AlterField(
            model_name='historicalsystemassessmentresult',
            name='deployment',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The deployment associated with the assessment result.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.Deployment'),
        ),
        migrations.AlterField(
            model_name='historicalsystemassessmentresult',
            name='system',
            field=auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The system associated with the system assessment result', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.System'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='consumer_element',
            field=auto_prefetch.ForeignKey(blank=True, help_text='The element the statement is about.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statements_consumed', to='controls.Element'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='import_record',
            field=auto_prefetch.ForeignKey(blank=True, help_text='The Import Record which created this Statement.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='import_record_statements', to='controls.ImportRecord'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='parent',
            field=auto_prefetch.ForeignKey(blank=True, help_text='Parent statement', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='controls.Statement'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='producer_element',
            field=auto_prefetch.ForeignKey(blank=True, help_text='The element producing this statement.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statements_produced', to='controls.Element'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='prototype',
            field=auto_prefetch.ForeignKey(blank=True, help_text='Prototype statement', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instances', to='controls.Statement'),
        ),
        migrations.AlterField(
            model_name='system',
            name='root_element',
            field=auto_prefetch.ForeignKey(help_text='The Element that is this System. Element must be type [Application, General Support System]', on_delete=django.db.models.deletion.CASCADE, related_name='system', to='controls.Element'),
        ),
        migrations.AlterField(
            model_name='systemassessmentresult',
            name='deployment',
            field=auto_prefetch.ForeignKey(blank=True, help_text='The deployment associated with the assessment result.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessment_results', to='controls.Deployment'),
        ),
        migrations.AlterField(
            model_name='systemassessmentresult',
            name='system',
            field=auto_prefetch.ForeignKey(blank=True, help_text='The system associated with the system assessment result', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='system_assessment_result', to='controls.System'),
        ),
    ]
