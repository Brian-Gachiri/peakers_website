# Generated by Django 3.2.6 on 2021-11-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20211118_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]