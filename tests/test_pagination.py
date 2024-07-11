import pytest


@pytest.mark.parametrize(
    "rest_framework_key, expected_value",
    [
        ('DEFAULT_PAGINATION_CLASS', 'rest_framework.pagination.PageNumberPagination'),
        ('PAGE_SIZE', 10)
    ]
)
def test_rest_framework_pagination(settings, rest_framework_key, expected_value):
    setting_name = "REST_FRAMEWORK"
    rest_framework_setting = getattr(settings, setting_name, None)
    assert rest_framework_setting is not None, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto,"
        f"se haya agregado la configuración `{setting_name}`"
    )

    assert rest_framework_key in rest_framework_setting, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, `{setting_name}` "
        f"tenga la clave `{rest_framework_key}` agregada"
    )

    actual_value = rest_framework_setting[rest_framework_key]
    assert actual_value == expected_value, (
        f"Comprueba que en el archivo `wordicum/settings.py` con la configuración del proyecto, `{setting_name}` "
        f"tenga la clave `{rest_framework_key}` con el valor especificado en las condiciones de la tarea."
    )
