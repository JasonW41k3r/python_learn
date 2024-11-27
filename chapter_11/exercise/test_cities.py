from city_functions import city

def test_city_country():
    res = city('santiago', 'chile', 5000000)
    assert res == 'Santiago, Chile - 5000000'
