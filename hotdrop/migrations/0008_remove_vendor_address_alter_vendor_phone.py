from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('hotdrop', '0007_remove_vendor_address_vendor_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='phone',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]