# Generated by Django 2.2.16 on 2020-10-28 19:46

from django.db import migrations, models
import tendenci.apps.base.validators


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0016_auto_20201010_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position', 'name'), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, validators=[tendenci.apps.base.validators.UnicodeNameValidator()]),
        ),
    ]