# Generated by Django 4.2.3 on 2023-07-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=50)),
                ('grade', models.IntegerField(choices=[('11', '11'), ('12', '12')], max_length=5)),
                ('major', models.CharField(choices=[('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Biology', 'Biology')], max_length=20)),
            ],
        ),
    ]
