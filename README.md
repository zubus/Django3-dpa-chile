[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

Django Political-Administrative Division of Chile
División Política-Administrativa de Chile para Django

=================================================

``Regiones - Provincias - Comunas``
=================================================

This fork was created to update the package to work with the latest versions of Django 3.2+ (4.1 included) and Python, as the [original developer](https://github.com/jupitercl/django-dpa-chile) appears to be inactive.

Information obtained from the api of Modernization and Digital Government Unit

https://apis.digital.gob.cl/dpa

Pypi
====

https://pypi.org/project/django3-dpa-chile/

Installation
------------

Install **django3-dpa-chile** using **pip**


    pip install django3-dpa-chile

Add **d3_dpa_chile** to **INSTALLED_APPS**

settings.py
-----------

    # ...

    INSTALLED_APPS =[
    ...
    'd3_dpa_chile',
    ]

    # ...

Populate
--------

    python manage.py migrate d3_dpa_chile

    python manage.py populate_dpa_chile

Use
---

    from d3_dpa_chile.models import Region, Provincia, Comuna
