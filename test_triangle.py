from triangle import Triangle
import pytest


@pytest.mark.parametrize("test_input", [(4, 4, 4), (5, 5, 5), (6, 6, 6)])
def test_for_equilateral(test_input):
    triangle = Triangle(*test_input)
    assert triangle.get_triangle_type() == "Equilateral"


@pytest.mark.parametrize("test_input", [(4, 4, 3), (7, 7, 5), (6, 6, 8)])
def test_for_isosceles(test_input):
    triangle = Triangle(*test_input)
    assert triangle.get_triangle_type() == "Isosceles"


@pytest.mark.parametrize("test_input", [(12, 13, 14), (5, 6, 7), (7, 6, 5)])
def test_for_scalene(test_input):
    triangle = Triangle(*test_input)
    assert triangle.get_triangle_type() == "Scalene"


@pytest.mark.parametrize("test_input", [(-12, 13, 14), (5, -6, 7), (7, 6, -5)])
def test_for_negative_inputs(test_input):
    with pytest.raises(ValueError) as exp:
        Triangle(*test_input)
    assert str(exp.value) == "Negative input"


@pytest.mark.parametrize("test_input", [(12, 13, 140), (1, 1, 2), (7, 6, 100)])
def test_for_invalid_inputs(test_input):
    with pytest.raises(ValueError) as exp:
        Triangle(*test_input)
    assert str(exp.value) == "Given inputs can not be triangle"
