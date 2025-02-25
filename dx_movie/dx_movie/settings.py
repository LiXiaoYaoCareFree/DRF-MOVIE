"""
Django settings for dx_movie project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!7dy%-0_04)8xfw58p3cnhgm^#4yo=_1dlhz#8am=jp09p4$9i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'django_filters',
    'movie',
    'account',
    'trade',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dx_movie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dx_movie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dx_movie',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans' 

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# DRF设置
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}



SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # 设置访问令牌的生命周期
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),   # 设置刷新令牌的生命周期

    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=2),  # 设置访问令牌的生命周期
    # 'REFRESH_TOKEN_LIFETIME': timedelta(minutes=4),   # 设置刷新令牌的生命周期
}


# 邮箱配置
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'LiXiaoYaoCareFree@163.com'  
EMAIL_HOST_PASSWORD = 'RMtap33RqBzKcNrp'
DEFAULT_FROM_EMAIL = 'LiXiaoYaoCareFree@163.com'
EMAIL_USE_TLS = True

# 配置djoser使用的User模型
DJOSER = {
    'USERNAME_FIELD': 'username',
    'LOGIN_FIELD': 'email',
    # 'USER_CREATE_PASSWORD_RETYPE': True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    # 'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    # 'PASSWORD_RESET_CONFIRM_URL': '/password/reset/confirm/{uid}/{token}',
    # 'SET_PASSWORD_RETYPE': True,
    # 'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'SERIALIZERS': {
        'user_create': 'account.serializers.CustomUserCreateSerializer', 
        # 'set_password': 'account.serializers.CustomSetPasswordSerializer',
    },

}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')  
]

# 支付宝相关配置
# ALIPAY_SERVER_URL = 'https://openapi.alipaydev.com/gateway.do'
ALIPAY_SERVER_URL = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do'
# ALIPAY_APP_ID = '2021000121621726'
ALIPAY_APP_ID = '9021000126620710'
# ALIPAY_APP_PRIVATE_KEY = 'MIIEowIBAAKCAQEAzWs2eC9026rMxG1C7tK3SqrulpvS/c4XAnctjiY/NlUSAXfmXNGJQe+eTt1+WrGWWWXSU5qotWjF5MKC0O5l7R9jl5iKVZoCj4NvPNhuAWVYqbZBGHuub9YJF2y1oTZt2rOPKXp+cuR4zEKSd/YhUM1q1s+v/WxCbuM17WKRx3WmVVB93x3/395S1VCcQERvrNUX3rEg39J4jcYxn5LEKOeYRsq0l2t295tI9UKPC/Ejm+fSB/770BJZF/nk5un1OecCYPfIEBJe8DQDoP3WoSVbO2NeBE/qIY5tFUewW+6anKFXbDVzUdHy4O6ZM0r9n9+ATe0Ac+JZvKd31v2phQIDAQABAoIBAGJwVGP36foyuXoQGhk0pV2E2F0YQ14ZWvF1h0EtlvFEhyJpAN3OFAai+6wzfI+dtr0UjFxAK0Tz9pGPnPzeob2mYyWMlg47haqcg7wWw3CrzndVvZAsBQXW/fhZwhiFatN5ZMutxdbtIe5QoLwYGRMNvXs/f8jkDlnxTDB8IfwAy1J43MUQp1me3obiZneU+rcU4DZD4L6G+tXiE+UU38QJJfLnV/o+YRMWX8UfMx57ma71jYIKhnBPp9/nvrj8cfSXXmuJRHa1oYUeJngfuuHhgYZNrnwOA+BO81CIH6LSs4Hfl6M/GBbcnwNwC76PJyiekQBlYQVk8iN1iU3SmUECgYEA7Qrya4Vi8D5we+drKfqiEEwH+0ph3p+4Vgo8sqgGgmOzAwv9VNZZvJBVhdNFsxuxOQ8qh/e0ZlGSonCG4a5E38AYsR/Al1Z+6W4crPgP+UQ+IlnBs9N9O2e4bLvU4tK6/DCABrOSH17VUOSWvFtvaSG/mzVdCaSYx1E+E5VMwmkCgYEA3djRd8DdorG62hgQR1TAVZiXlGDCjxj+jlURM2UYXvoqR6D5/LPtKruYGYpuQhfgHuSViis5FlwIzPnYhhvo/i/tj6+3n1Jx49q/W03LwF0cqsG3qrsZAzhBiVgynjv9XGy5cGPwn8G27Hz6gRZORXFxgkcm8og5fC30FowY0r0CgYBMAKeLq//2Eb8VKzUkB5Vw7j/c5ZONwt5iz/N4QQGdSwQ5pN18FyI8oHabaws9C1L+fYtgfx6bc+o1JSlKMQsqRrhkCk9A9t3IUKLnHr5YaPYXI3pFAzlzE6WBT5RJidGkTJSwEWF3p3tz7WcbS6HkLor1491J2zmVJsplkwhCiQKBgQCnFxQFv2Tvki+q7m7sWuAWWDzqy8oeX3PzHg07iYxGlONdWdiPxbD++5Y+vm33J+ZtPjuHerCfr6gNQq0brU/ai5zBGVcTD9SqCmsQSNMKyta5ofhFBnB7ZVavLJfLaGGWyGkPRqbInO26xxMiQPupAB2/QvoJuCKb7jym8tQLfQKBgH7QdCOE0KHUvUF1fJaXald76GvJqghi3siU2gHVVrMHIYI4ucs4jCo9IWMzvSQDr4HqiUP6JJmPByzaTQBKR2p8sZ6RD3DsSS+AG+s0R8di+Rj6BAq2tznTnJW1koQPbhwaHfqRqdSxoYKUk7u2EvbU4YWmnOAdX56l0b9hvcmE'
ALIPAY_APP_PRIVATE_KEY = 'MIIEpQIBAAKCAQEAtJ8WH+1FLRiGLOB6hiYHJV2L3FJ57eYdu4kZXxxYwJ2JJriC5xUDu1601yhVlc4UCn7tbEgq6+e50PbyyHvrF8XKNf7nSz+M5QgXKYTleof7E66+IkQM/6SrtkJ/hGOsyHI9vynuDWQ7Vzcj6liihlpXtqC8iaygzX+3ibecWeuGfPnH3msjRQtsuTIQcLqqVu3rOkXM4mTwtY/r7Kgce+hsFnW6j42LzJgmcL2OnHeTcbM+2Njxz+ZSg2xUhzP5pMPiCfahVpwkiQxtcQCKeAuFC9UM3pg3CVN/T+p7dpN3K0kV+ASMfgCagVK6lxpdGeZwhLq1SbKqoRiJE1MW5wIDAQABAoIBAQCFsR9SQHCsoXNnMjzeoLU3XheQ2+duRJ8LWb5S3QuAftqus3IJE0/w13fprewzdxb0ceDQ/lXuyVWLq84mwTpRHVDASM3wr7hdKnDihYDKAm7Asd4ARPiOHNgQjwYN+y1ALPcxURroBKG7u4+0/ShHZAV6o10KVqGrmfZDVInBL8omKWCjhYS1RMBAyliJd+8cdQqB8e0L5Zf6EMH3WmmljkZkPt1v/dcZM9+fPy+FXJVRTXFD9x6qCN+lN9wuQ69FJt2dVlHFgXQEUAIf3gF3/wtXeGaLSNWLrgzfkAHi1u9a98YJll8qm9qtrQUr3nOMd58U846VHBzKUQZbhOjZAoGBAOT2rcZlboqqWcvEAetPrUkpE85gbCKFHbCrDNT6/t8AvUjkvDoWVuHNvB6fYjFroq6985GqDNGrZjnKBjFGVsopzIahRIZCJhx6wQVC2zKaHnieonPzllxqtb7XJw+MQNsIyj8W3PceKSAAPc2TRypcKIZfEkG45GeX58GUYlS9AoGBAMnzE5ot3Mx6B6BDeYZwhY7hC1nLTFp165aSFXfIfYW9MwsS61PCUyPoajxKQdgI1XhlL48djzdR6iLw0xTnTscvPDkD6KmkzR8E17gqLTXDt0Enw77+8sxtEFd9tCAXQq0uYSINwxfUwwLpMf/rSCyZR5PGTZfoSlFLCDFXWn5zAoGBAIDPnrgM/IGakOYoIYRG0RBlwbTLXkqVZTytHoz7oEPJYLQPqy1qv/pNClaYCGARU/bG+q6qYofay6obVByIm+8kUOI0/B4kPNis3sac9ECloBrv9CkTkzXu+sygsmL23s3bRhz0Od/04eIVALAU+WaFbm8aMWU0JZt6RHINjrxpAoGBALe+iA5XPjd5rGigG/k7dfmrPvWjaMRB2Gm2XvwOmk7N95xSyXT7MURRmh9i/Qe/+eLCRgR0Q7N0v5CtB5FUaDQJAUVrDg0UWmGnuVLiZSIvAhSxRoQIWgewEBda00IDh/IkadJfLSwItKp4XLraa1/Q0vRckIrvmnbeywSB01+LAoGAHWhNR1e8QNDgfEemLfWm8bF6+zLePMIIhkhCCCsXtjdE4+JI8E+wb2UiiV70xlJbglKz7+6Y/RjFFSQK95IYtsAXdXZtQbhHD3riq30R5q1AKJxfBwqLdfaMOrxVAiBJomMPw+0pEzCTmHgZ5HcBQBJM+KC1rn1C/YAnhre/l04='
# ALIPAY_PUBLIC_KEY = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqoScxHotPzMFjQADRBn25moNQlCFLXpmPiHf4YvdVH1UuwowZz3dB1bMsaFzFTQXX1He0esJrUmkAgafVPHimT9Bd/hVHKGO1T2IkrDyP7Byg82jsto1N+5eOBkInhAHDmyxQKSGAAbTBoEXBuscvSVmGfpbNOT2YJHDiHQireETEpnFjB8O8QOrLHaqpbYT3m/sCK8dvZGcGH4u8AqSiy1sXmY4amxiSfZNEOpeh+rG7lX88T+1BGegkM+IimiDAk3Xuzi+tCstemjhGdpIPuwyAnJX+lkM+MFhWRhd4eNnyVXK5+bG2k+VKMI+Hdt4GSAmxfoE6madjUmNeXdeTwIDAQAB'
ALIPAY_PUBLIC_KEY = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr8yFq5xNRulIA/4vM2jDLgpdnNWMiqV0lwalhgrL3/XI+MQ3a4Sa37YNorc3+LYcvf+BPlrmmNlkgTr45TpHh2pjvqlE+7OpMhJ/1hLOdhU3SZUeVkoixkMZM4/cSsvZMhkG4xp2a6WagQb+rn13NwiuPIguYTDyeveOvqPYPoDkKXYeg4pvWxEn9+TGunm810rnl9nsb/E6XPydGBJyIyQ94vn9HxzpySIMNS6Ln3rd+Nat+IrghbE604WpBI+FeC6E2pba7uNlQoU81kbgqNlhXunbSI95vAG2rwWMsM8oihImoNiFed0h01vvpoxAPBsn81Qym0iqQT3kIpv8TQIDAQAB'

ALIPAY_RETURN_URL = 'https://a346-36-48-46-105.ngrok-free.app/order_list/'
ALIPAY_NOTIFY_URL = 'https://a346-36-48-46-105.ngrok-free.app/callback/'
