# Generated by Django 5.1.2 on 2024-10-28 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='enrollno',
        ),
        migrations.DeleteModel(
            name='Classes',
        ),
        migrations.DeleteModel(
            name='GuardianDetails',
        ),
        migrations.RemoveField(
            model_name='results',
            name='enrollno',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='enrollno',
        ),
        migrations.DeleteModel(
            name='Subjects',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.DeleteModel(
            name='StudentDetails',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]