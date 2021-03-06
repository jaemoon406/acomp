# Generated by Django 4.0.2 on 2022-03-06 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_parents', to='board.category'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_parents', to='board.comment'),
        ),
    ]
