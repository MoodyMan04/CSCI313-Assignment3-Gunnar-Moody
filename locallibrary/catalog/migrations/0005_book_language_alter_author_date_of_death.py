# Generated by Django 5.0.3 on 2024-04-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Select a language for this book', to='catalog.language'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='died'),
        ),
    ]