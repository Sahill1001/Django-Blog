# Generated by Django 4.1.3 on 2022-12-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_srn_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='srn',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='srn',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
