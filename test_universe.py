import pytest

from universe import Universe

DEFAULT_SIZE=100
DEFAULT_POSITION=[0,0]

@pytest.mark.parametrize("size,figure_namme,figure_position", [
    (DEFAULT_SIZE, None, None),
    (80, '10_cells_row', [40,40]),
    (400, '10_cells_row', [20,20]),
    (DEFAULT_SIZE, '10_cells_row', DEFAULT_POSITION),
    (300, None, [25,25]),
])
def test_init_universe(size,figure_namme,figure_position):
    assert Universe(size,figure_namme,figure_position)