# Generated by Django 4.1.7 on 2023-03-01 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0007_remove_resourcestudy_topik_topik_keywords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='word',
            field=models.CharField(max_length=35, verbose_name='слово, словосочетание'),
        ),
        migrations.AlterField(
            model_name='roadmapstudy',
            name='name',
            field=models.CharField(help_text='на русском', max_length=35, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='roadmapstudy',
            name='name_en',
            field=models.CharField(help_text='на английском', max_length=20, verbose_name='Roadmap'),
        ),
        migrations.RemoveField(
            model_name='topik',
            name='roadmap',
        ),
        migrations.AddField(
            model_name='topik',
            name='roadmap',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadmap.roadmapstudy', verbose_name='план изучения (roadmap)'),
        ),
    ]
