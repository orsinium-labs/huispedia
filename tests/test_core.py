import huispedia


def test_get_houses():
    infos = huispedia.get_houses()
    assert len(infos) == 1000
    for info in infos:
        assert 'bouwjaar' in info
        assert 'city_name' in info
