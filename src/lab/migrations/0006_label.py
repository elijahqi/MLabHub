# Generated by Django 3.2.2 on 2023-09-23 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_alter_pic_lab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortname', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=200)),
                ('lab', models.ForeignKey(db_column='labs', on_delete=django.db.models.deletion.CASCADE, related_name='label', to='lab.lab')),
            ],
        ),
    ]
