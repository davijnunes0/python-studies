from .app import conversion

def test_():
    assert conversion(32) == 0.0
    assert conversion(-40) == -40.0

    # Isso resultára em um AssertionError, pois, essa afirmação é algo irreal.
    assert conversion(0) == 1
