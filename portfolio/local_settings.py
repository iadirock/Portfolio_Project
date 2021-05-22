SECRET_KEY = 'q_gd!*1qyu(b^wz0pgmuu*!x0j%v1o)kwj(^e)r=3)lnp8^51egggs('

ALLOWED_HOSTS = ['167.71.176.11','www.adityarana.in','adityarana.in']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER': 'portfoliouser',
        'PASSWORD': 'Bourne@007',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = False
