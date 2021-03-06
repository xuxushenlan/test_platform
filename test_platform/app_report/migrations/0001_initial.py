# Generated by Django 2.2.2 on 2019-09-02 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=100, verbose_name='用例名')),
                ('is_pass', models.BooleanField(null=True, verbose_name='是否通过')),
                ('fail_desc', models.CharField(max_length=200, null=True, verbose_name='用例失败描述')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('error', models.IntegerField(default=0, verbose_name='错误用例')),
                ('failure', models.IntegerField(default=0, verbose_name='失败用例')),
                ('skipped', models.IntegerField(default=0, verbose_name='跳过用例')),
                ('tests', models.IntegerField(default=0, verbose_name='总用例数')),
                ('run_time', models.FloatField(default=0, verbose_name='运行时长')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TestSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_name', models.CharField(max_length=100, verbose_name='测试步骤截图')),
                ('full_path', models.CharField(max_length=200, verbose_name='完整的路径')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_report.TestCase')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TestFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100, verbose_name='测试文件名')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_report.TestReport')),
            ],
        ),
        migrations.AddField(
            model_name='testcase',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_report.TestFile'),
        ),
    ]
