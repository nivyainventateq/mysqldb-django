# Generated by Django 3.0.3 on 2020-02-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logintb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(blank=True, max_length=50, null=True)),
                ('pwd', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
