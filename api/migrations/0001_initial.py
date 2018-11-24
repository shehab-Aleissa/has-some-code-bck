# Generated by Django 2.1.2 on 2018-11-14 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='classesOfTheBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('year_of_made', models.IntegerField(blank=True, choices=[(1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], null=True)),
                ('transmission', models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=120, null=True)),
                ('exterior_color', models.CharField(blank=True, choices=[('White', 'White'), ('Black', 'Black'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Red', 'Red'), ('Blue', 'Blue'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Tan', 'Tan'), ('Brown', 'Brown'), ('Grey', 'Grey')], max_length=120, null=True)),
                ('interior_color', models.CharField(blank=True, choices=[('White', 'White'), ('Black', 'Black'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Red', 'Red'), ('Blue', 'Blue'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Tan', 'Tan'), ('Brown', 'Brown'), ('Grey', 'Grey')], max_length=120, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('Kilometer', models.IntegerField(blank=True, null=True)),
                ('body_type', models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Pickup Truck', 'Pickup Truck'), ('Sport', 'Sport'), ('MicroCar', 'MicroCar'), ('Van', 'Van')], max_length=120, null=True)),
                ('sunroof', models.CharField(blank=True, choices=[('No', 'No'), ('Normal', 'Normal'), ('Panorama', 'Panorama')], max_length=120, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('convertable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SellingBrandsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='api.Category')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SellingBrandsCategory'),
        ),
        migrations.AddField(
            model_name='post',
            name='brand_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classesOfTheBrand'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classesofthebrand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.SellingBrandsCategory'),
        ),
    ]
