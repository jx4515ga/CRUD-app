# Generated by Django 4.1.7 on 2023-03-20 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=10)),
                ('position_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=50)),
                ('appl_submitted', models.DateField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_application.status')),
            ],
        ),
    ]
