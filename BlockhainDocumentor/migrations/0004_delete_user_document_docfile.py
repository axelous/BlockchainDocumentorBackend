# Generated by Django 4.1.3 on 2022-11-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlockhainDocumentor', '0003_rename_login_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='document',
            name='docFile',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]