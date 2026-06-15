from data_store import cities_data


def test_data_schema():
    """Starts a unit test ensuring fields match the expected schema"""

    # Set of keys the data must contain
    required_keys = {"name", "lat", "lng", "pop"}

    # Validate structure and types for each city
    for city in cities_data:
        assert required_keys.issubset(
            city.keys()
        ), f"Missing keys in {city['name']}"
        assert isinstance(city["lat"], (int, float))
