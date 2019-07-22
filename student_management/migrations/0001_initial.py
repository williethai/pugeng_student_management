# Generated by Django 2.0.8 on 2019-07-22 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=60)),
                ('number_of_classes', models.IntegerField(default=0)),
                ('year', models.CharField(default='', max_length=5)),
                ('semester', models.CharField(default='', max_length=5)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('create_at', models.DateTimeField()),
                ('introduction', models.CharField(default='', max_length=2000)),
            ],
            options={
                'verbose_name_plural': '班別',
            },
        ),
        migrations.CreateModel(
            name='Class_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=2000)),
                ('class_to_schedule', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_class_set', to='student_management.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Class_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=60)),
                ('create_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=60)),
                ('clerical_name', models.CharField(default='', max_length=60)),
                ('date_of_birth', models.DateTimeField()),
                ('national_id_num', models.CharField(default='', max_length=20)),
                ('phone_num', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=100)),
                ('emergency_contact_person', models.CharField(default='', max_length=60)),
                ('emergency_contact_phone', models.CharField(default='', max_length=20)),
                ('create_at', models.DateTimeField()),
                ('gender', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='gender_set', to='student_management.Gender')),
                ('invite_person', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='invite_person_set', to='student_management.Student')),
            ],
            options={
                'verbose_name_plural': '學員',
            },
        ),
        migrations.CreateModel(
            name='Student_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default='0000-00-00')),
                ('class_group', models.CharField(default='', max_length=5)),
                ('present_check', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField()),
                ('class_of_student', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='student_with_class_set', to='student_management.Class')),
            ],
            options={
                'verbose_name_plural': '學員-班別新增',
            },
        ),
        migrations.CreateModel(
            name='Student_Class_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Volunteer_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default='0000-00-00')),
                ('create_at', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': '學員-班別新增',
            },
        ),
        migrations.CreateModel(
            name='Volunteer_Group',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=60)),
                ('create_at', models.DateTimeField()),
                ('assist_leader', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_group_assist_leader_set', to='student_management.Student')),
                ('leader', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_group_leader_set', to='student_management.Student')),
                ('volunteer_students', models.ManyToManyField(through='student_management.Student_Volunteer_Group', to='student_management.Student')),
            ],
            options={
                'verbose_name_plural': '功德組',
            },
        ),
        migrations.CreateModel(
            name='Volunteer_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=60)),
                ('create_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='student_volunteer_group',
            name='status',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_status_set', to='student_management.Volunteer_Status'),
        ),
        migrations.AddField(
            model_name='student_volunteer_group',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='in_student_volunteer_group_student_set', to='student_management.Student'),
        ),
        migrations.AddField(
            model_name='student_volunteer_group',
            name='volunteer_group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_group_set', to='student_management.Volunteer_Group'),
        ),
        migrations.AddField(
            model_name='student_class',
            name='status',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='student_class_status_set', to='student_management.Student_Class_Status'),
        ),
        migrations.AddField(
            model_name='student_class',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='in_class_student_set', to='student_management.Student'),
        ),
        migrations.AddField(
            model_name='class_group',
            name='assistant_leader',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='assist_group_leader_set', to='student_management.Student'),
        ),
        migrations.AddField(
            model_name='class_group',
            name='class_group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='class_group_set', to='student_management.Class'),
        ),
        migrations.AddField(
            model_name='class_group',
            name='leader',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='group_leader_set', to='student_management.Student'),
        ),
        migrations.AddField(
            model_name='class',
            name='monitor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='class_monitor_set', to='student_management.Student'),
        ),
        migrations.AddField(
            model_name='class',
            name='status',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='class_status_set', to='student_management.Class_Status'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(through='student_management.Student_Class', to='student_management.Student'),
        ),
    ]
