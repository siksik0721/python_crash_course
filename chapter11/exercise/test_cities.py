from city_functions import get_formatted_name


def test_city_country():
    formatted_name = get_formatted_name("santiago", "chile")
    assert formatted_name == "Santiago, Chile"


def test_city_country_population():
    formatted_name = get_formatted_name("santiago", "chile", 5000000)
    assert formatted_name == "Santiago, Chile - population 5000000"
