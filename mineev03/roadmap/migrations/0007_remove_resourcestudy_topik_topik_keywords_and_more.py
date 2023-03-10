# Generated by Django 4.1.7 on 2023-03-01 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0006_alter_roadmapstudy_options_keyword_keywords_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcestudy',
            name='topik',
        ),
        migrations.AddField(
            model_name='topik',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='roadmap.keyword', verbose_name='ключевые слова'),
        ),
        migrations.AddField(
            model_name='topik',
            name='resourcestudy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='roadmap.resourcestudy', verbose_name='ссылка на курс'),
        ),
    ]
