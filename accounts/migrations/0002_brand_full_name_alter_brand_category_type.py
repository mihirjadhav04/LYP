# Generated by Django 4.0.4 on 2022-05-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='full_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='category_type',
            field=models.CharField(choices=[('Autos & Vehicles', 'Autos & Vehicles'), ('Comedy', 'Comedy'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Film & Animation', 'Film & Animation'), ('Gaming', 'Gaming'), ('Howto & Style', 'Howto & Style'), ('Music', 'Music'), ('News & Politics', 'News & Politics'), ('Nonprofits & Activisms', 'Nonprofits & Activisms'), ('People & Blogs', 'People & Blogs'), ('Pets & Animals', 'Pets & Animals'), ('Science & Technology', 'Science & Technology'), ('Travel & Events', 'Travel & Events'), ('Sports', 'Sports')], max_length=100),
        ),
    ]
