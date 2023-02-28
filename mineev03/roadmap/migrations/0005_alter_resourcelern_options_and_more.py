# Generated by Django 4.1.7 on 2023-02-25 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0004_faq_alter_resourcelern_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcelern',
            options={'verbose_name': 'ссылка на курс', 'verbose_name_plural': 'ссылки на курсы'},
        ),
        migrations.AlterModelOptions(
            name='resourcestudy',
            options={'verbose_name': 'ссылка на ресурс по теме', 'verbose_name_plural': 'ссылки на ресурсы'},
        ),
        migrations.AlterModelOptions(
            name='topik',
            options={'verbose_name': 'тема обсуждения и изучения', 'verbose_name_plural': 'темы обсуждения и изучения'},
        ),
        migrations.AddField(
            model_name='topik',
            name='roadmap',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roadmap.roadmapstudy', verbose_name='план изучения (roadmap)'),
        ),
    ]