# Generated by Django 4.1.3 on 2023-04-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlockhainDocumentor', '0010_alter_document_options_alter_document_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='own',
            field=models.CharField(max_length=100),
        ),
    ]