# Generated by Django 4.1.1 on 2022-09-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=40)),
                ('Name', models.CharField(max_length=40)),
                ('Textarea', models.CharField(max_length=2000)),
            ],
        ),
    ]
