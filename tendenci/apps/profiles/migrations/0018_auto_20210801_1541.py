# Generated by Django 3.2.5 on 2021-08-01 15:41

from django.db import migrations


def prep_nullbooleanfield_migration(apps, schema_editor):
    # Prepare for migration from NullBooleanField to BooleanField
    Profile = apps.get_model("profiles", "Profile")
    fields = ("allow_anonymous_view",
              "allow_user_view",
              "allow_member_view",
              "allow_user_edit",
              "allow_member_edit",
              "status")

    for field in fields:
        filter_param = {f"{field}__isnull": True}
        update_param = {field: False}
        Profile.objects.filter(**filter_param).update(**update_param)

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20210504_1536'),
    ]

    operations = [
        migrations.RunPython(prep_nullbooleanfield_migration),
    ]