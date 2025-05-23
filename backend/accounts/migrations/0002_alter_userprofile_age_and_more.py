# Generated by Django 5.0.4 on 2025-03-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, help_text='Věk v letech', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='basal_metabolic_rate',
            field=models.FloatField(blank=True, help_text='Bazální metabolismus v kcal', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Muž'), ('F', 'Žena')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(blank=True, help_text='Výška v cm', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.FloatField(blank=True, help_text='Váha v kg', null=True),
        ),
    ]
