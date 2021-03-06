# Generated by Django 3.0.5 on 2020-04-13 06:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20200413_0811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='修改时间', verbose_name='修改时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='删除标记', verbose_name='删除标记')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('desc', models.CharField(blank=True, max_length=50, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '职位/岗位',
                'verbose_name_plural': '职位/岗位',
            },
        ),
        migrations.AddField(
            model_name='role',
            name='datas',
            field=models.CharField(choices=[('全部', '全部'), ('本级', '本级'), ('本级及以下', '本级及以下'), ('仅本人', '仅本人'), ('自定义', '自定义')], default='本级及以下', max_length=50, verbose_name='数据权限'),
        ),
        migrations.AddField(
            model_name='role',
            name='depts',
            field=models.ManyToManyField(to='rbac.Organization', verbose_name='部门'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='rbac.Role', verbose_name='角色'),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.ManyToManyField(to='rbac.Position', verbose_name='岗位'),
        ),
    ]
