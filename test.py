from universe import Universe


def test_init_universe():
    assert Universe()
    assert Universe((60,60),'10_cells_row',(40,40))