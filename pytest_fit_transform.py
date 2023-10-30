import pytest
from one_hot_encoder import fit_transform


def test_fit_transform_raise():
    with pytest.raises(TypeError):
        fit_transform()


def test_fit_transform_equal():
    transformed_cities = fit_transform(
        'Москва', 'Лондон', 'Нью-Йорк'
    )
    expected = [
        ('Москва', [0, 0, 1]),
        ('Лондон', [0, 1, 0]),
        ('Нью-Йорк', [1, 0, 0])
    ]
    assert transformed_cities == expected


def test_fit_transform_in():
    transformed_cities = fit_transform(
        'Москва', 'Лондон', 'Рим', 'Нью-Йорк'
    )
    expected_in = ('Рим', [0, 1, 0, 0])
    assert expected_in in transformed_cities


def test_fit_transform_not_in():
    transformed_cities = fit_transform(
        'Москва', 'Лондон', 'Рим', 'Нью-Йорк'
    )
    expected_not_in = ('Лиссабон', [0, 0, 0, 1])
    assert expected_not_in not in transformed_cities
