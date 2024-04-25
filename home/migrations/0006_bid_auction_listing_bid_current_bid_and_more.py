# Generated by Django 4.2.6 on 2024-02-19 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_userprofile_avail_bal'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='auction_listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.auctionlisting'),
        ),
        migrations.AddField(
            model_name='bid',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='auction',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]