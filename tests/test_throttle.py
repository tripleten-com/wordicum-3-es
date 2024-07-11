import pytest


@pytest.mark.parametrize(
    "default_class",
    [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ]
)
def test_rest_framework_throttle_classes(settings, default_class):
    setting_name = "REST_FRAMEWORK"
    rest_framework_setting = getattr(settings, setting_name, None)
    assert rest_framework_setting is not None, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto,"
        f"se haya agregado la configuración `{setting_name}`"
    )

    rest_framework_key = 'DEFAULT_THROTTLE_CLASSES'
    assert rest_framework_key in rest_framework_setting, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, `{setting_name}` "
        f"tenga la clave `{rest_framework_key}` agregada"
    )

    assert default_class in rest_framework_setting[rest_framework_key], (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, `{setting_name}` "
        f"tenga la clase `{default_class}` agregada a la clave `{rest_framework_key}`"
    )


@pytest.mark.parametrize(
    "rate_client, rate",
    [
        ('user', '100/minute'),
        ('anon', '10/minute')
    ]
)
def test_rest_framework_throttle_rates(settings, rate_client, rate):
    setting_name = "REST_FRAMEWORK"
    rest_framework_setting = getattr(settings, setting_name, None)
    assert rest_framework_setting is not None, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto,"
        f"se haya agregado la configuración `{setting_name}`"
    )

    rest_framework_key = 'DEFAULT_THROTTLE_RATES'
    assert rest_framework_key in rest_framework_setting, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, `{setting_name}` "
        f"tenga la clave `{rest_framework_key}` agregada"
    )

    throttle_rate = rest_framework_setting[rest_framework_key]
    assert isinstance(throttle_rate, dict), (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, `{setting_name}` "
        f"tenga un diccionario agregado a la clave `{rest_framework_key}`."
    )

    actual_rate = throttle_rate.get(rate_client, None)
    assert actual_rate is not None, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, `{setting_name}` "
        f"tenga una clave en `{rest_framework_key}` del diccionario `{rest_framework_key}` llamada `{rate_client}`."
    )

    assert actual_rate == rate, (
        f"Comprueba que en el archivo wordicum/settings.py en la configuración del proyecto, {setting_name} "
        f"tenga una clave en {rest_framework_key} llamada {rate_client} "
        f"con el límite establecido según la condición de la tarea."
    )
