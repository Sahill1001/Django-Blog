# Generated by Django 4.1.3 on 2022-12-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('srn', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=10)),
                ('date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
