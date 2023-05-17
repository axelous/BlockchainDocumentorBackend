# Generated by Django 4.1.3 on 2022-12-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlockhainDocumentor', '0005_alter_document_options_remove_document_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docFile',
            field=models.FileField(default=None, upload_to='media', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='document',
            name='size',
            field=models.CharField(max_length=10, verbose_name='Размер'),
        ),
    ]