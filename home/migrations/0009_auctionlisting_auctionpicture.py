# Generated by Django 4.2.6 on 2024-03-31 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_bid_auction_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='auctionpicture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
