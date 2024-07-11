def test_add_corsheaders_app(settings):
    installed_app = "corsheaders"
    assert installed_app in settings.INSTALLED_APPS, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, se haya agregado en `INSTALLED_APPS` "
        f"la aplicación ` {installed_app}`"
    )


def test_cors_middleware(settings):
    cors_middleware = "corsheaders.middleware.CorsMiddleware"
    assert cors_middleware in settings.MIDDLEWARE, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, se haya agregado en `MIDDLEWARE`"
        f"el middleware `{cors_middleware}`"
    )

    django_common_middleware = "django.middleware.common.CommonMiddleware"
    django_common_middleware_index = settings.MIDDLEWARE.index(django_common_middleware)
    cors_middleware_index = settings.MIDDLEWARE.index(cors_middleware)
    assert cors_middleware_index < django_common_middleware_index, (
        "Comprueba que en el archivo `wordicum/settings.py`, esté en la lista `MIDDLEWARE`"
        f"el controlador `{cors_middleware}` y esté colocado antes de `{django_common_middleware}`."
    )


def test_cors_allowed_origins(settings):
    setting_name = "CORS_ALLOWED_ORIGINS"
    assert hasattr(settings, setting_name), (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto,"
        f"se haya agregado la lista `{setting_name}`"
    )

    expected_host = "http://localhost:3000"
    assert expected_host in settings.CORS_ALLOWED_ORIGINS, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto,"
        f"la lista `{setting_name}` incluya el host `{expected_host}`."
    )


def test_disable_cors_origin_allow_all(settings):
    setting_name = "CORS_ORIGIN_ALLOW_ALL"
    actual_value = getattr(settings, setting_name, None)
    assert actual_value is None or actual_value is False, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto,"
        f"el parámetro `{setting_name}` no esté allí, o su valor sea igual a `False`"
    )
