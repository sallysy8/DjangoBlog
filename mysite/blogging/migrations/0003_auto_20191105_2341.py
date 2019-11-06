# Generated by Django 2.2.4 on 2019-11-06 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='blogging.Post'),
            preserve_default=False,
        ),
    ]