# Generated by Django 3.2.2 on 2023-08-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpage', '0002_alter_jobdata_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdata',
            name='oidc_auth_user',
        ),
        migrations.AddField(
            model_name='jobdata',
            name='creator_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
