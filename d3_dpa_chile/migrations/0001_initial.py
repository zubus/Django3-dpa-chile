from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Region",
            fields=[
                ("codigo", models.CharField(max_length=10, primary_key=True)),
                ("tipo", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=255)),
                ("lat", models.CharField(max_length=50)),
                ("lng", models.CharField(max_length=50)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Comuna",
            fields=[
                ("codigo", models.CharField(max_length=10, primary_key=True)),
                ("tipo", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=255)),
                ("lat", models.CharField(max_length=50)),
                ("lng", models.CharField(max_length=50)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Provincia",
            fields=[
                ("codigo", models.CharField(max_length=10, primary_key=True)),
                ("tipo", models.CharField(max_length=10)),
                ("nombre", models.CharField(max_length=255)),
                ("lat", models.CharField(max_length=50)),
                ("lng", models.CharField(max_length=50)),
                ("url", models.URLField()),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="d3_dpa_chile.Region",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comuna",
            name="provincia",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="d3_dpa_chile.Provincia"
            ),
        ),
        migrations.AddField(
            model_name="comuna",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="d3_dpa_chile.Region"
            ),
        ),
    ]
