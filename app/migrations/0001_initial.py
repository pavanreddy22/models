# Generated by Django 3.2.5 on 2021-07-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('subject_name', models.CharField(max_length=30)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
