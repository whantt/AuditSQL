# Generated by Django 2.0.2 on 2018-05-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0014_auto_20180531_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('webhook_addr', models.CharField(default='', max_length=256, verbose_name='webhook地址')),
            ],
            options={
                'verbose_name': '钉钉机器人',
                'verbose_name_plural': '钉钉机器人',
                'db_table': 'auditsql_webhook',
                'default_permissions': (),
            },
        ),
    ]
