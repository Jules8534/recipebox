# Generated by Django 3.0.5 on 2020-05-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsitem',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='instructions',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsitem',
            name='time_required',
            field=models.CharField(default='none', max_length=30),
            preserve_default=False,
        ),
    ]
