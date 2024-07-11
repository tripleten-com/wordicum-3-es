import pytest
from rest_framework import filters

try:
    from api.views import PostModelViewSet
except ImportError:
    raise AssertionError(
        "Al importar desde el archivo `api/views.py`,"
        "se produjo un error en la salida de `PostModelViewSet`."
    )


@pytest.mark.parametrize(
    "filter_, fields_attr, field",
    [
        (filters.SearchFilter, "search_fields", "text",),
        (filters.OrderingFilter, "ordering_fields", "pub_date",),
    ]
)
def test_filtering(filter_, fields_attr, field):
    assert filter_ in PostModelViewSet.filter_backends, (
        "Comprueba que en el archivo `api/views.py`, en la vista `PostModelViewSet`, el atributo"
        "`filter_backends` tenga la clase de backend requerida especificada según la tarea."
    )

    fields = getattr(PostModelViewSet, fields_attr)
    for actual_field in fields:
        # Comprobar un substring en un string al comprobar el uso de caracteres especiales
        assert field in actual_field, (
            f"Comprueba que en el archivo `api/views.py`, en la vista `PostModelViewSet`, el atributo"
            f"`{fields_attr}` tenga el campo especificado según la tarea."
        )
