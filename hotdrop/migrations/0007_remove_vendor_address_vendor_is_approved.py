from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('hotdrop', '0006_rename_vendor_order_vendor_remove_vendor_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]