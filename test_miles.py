def miles_to_km(miles):
    return miles * 1.60934

def test_miles_to_km():
    assert round(miles_to_km(5), 2) == 8.05

