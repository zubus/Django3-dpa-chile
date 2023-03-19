import requests
import json
from django.core.management.base import BaseCommand, CommandError
from d3_dpa_chile.models import Region, Provincia, Comuna

BASE_URL = "https://apis.digital.gob.cl/dpa/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


class Command(BaseCommand):
    help = "Populate Political-Administrative Division of Chile"

    def handle(self, *args, **options):
        if Region.objects.all().exists():
            self.stdout.write(
                self.style.WARNING("La base de datos ya ha sido poblada anteriormente.")
            )
            return

        try:
            self.stdout.write(
                self.style.WARNING("Descargando la información de la API...")
            )
            response = requests.get(f"{BASE_URL}regiones", headers=HEADERS)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            raise CommandError(f"Failed to retrieve regions - Exception: {e}")

        for region in data:
            try:
                self.stdout.write(self.style.SUCCESS(f"Region: {region['nombre']}"))

                region_fields = {
                    "tipo": region["tipo"],
                    "nombre": region["nombre"],
                    "lat": str(region["lat"]),
                    "lng": str(region["lng"]),
                    "url": region["url"],
                }

                region_obj, region_created = Region.objects.update_or_create(
                    codigo=region["codigo"], defaults=region_fields
                )

                self.create_provincias(region_obj)
            except Exception as e:
                raise CommandError(f"Fail to populate region - Exception: {e}")

        self.stdout.write(self.style.SUCCESS("Successfully populated DPA Chile"))

    def create_provincias(self, region):
        try:
            response = requests.get(
                f"{BASE_URL}regiones/{region.codigo}/provincias", headers=HEADERS
            )
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            raise CommandError(f"Failed to retrieve provincia - Exception: {e}")

        for provincia in data:
            try:
                self.stdout.write(
                    self.style.SUCCESS(f"Provincia: {provincia['nombre']}")
                )

                provincia_fields = {
                    "tipo": provincia["tipo"],
                    "nombre": provincia["nombre"],
                    "lat": str(provincia["lat"]),
                    "lng": str(provincia["lng"]),
                    "url": provincia["url"],
                    "region": region,
                }

                provincia_obj, provincia_created = Provincia.objects.update_or_create(
                    codigo=provincia["codigo"], defaults=provincia_fields
                )

                self.create_comunas(provincia_obj)
            except Exception as e:
                raise CommandError(f"Fail to populate provincia - Exception: {e}")

    def create_comunas(self, provincia):
        try:
            response = requests.get(
                f"{BASE_URL}regiones/{provincia.region.codigo}/provincias/{provincia.codigo}/comunas",
                headers=HEADERS,
            )
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            raise CommandError(f"Failed to retrieve comunas - Exception: {e}")

        for comuna in data:
            try:
                self.stdout.write(self.style.SUCCESS(f"Comuna: {comuna['nombre']}"))

                comuna_fields = {
                    "tipo": comuna["tipo"],
                    "nombre": comuna["nombre"],
                    "lat": str(comuna["lat"]),
                    "lng": str(comuna["lng"]),
                    "url": comuna["url"],
                    "region": provincia.region,
                    "provincia": provincia,
                }

                comuna_obj, comuna_created = Comuna.objects.update_or_create(
                    codigo=comuna["codigo"], defaults=comuna_fields
                )
            except Exception as e:
                raise CommandError(f"Fail to populate comunas - Exception: {e}")
