# Generated by Django 4.1.1 on 2022-09-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=40)),
                ('Contact', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
            ],
        ),
    ]
