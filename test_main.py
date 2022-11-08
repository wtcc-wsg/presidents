from main import query_ddg, query_presidents, known_presidents


def test_query_ddg():
    # Test that json was returned
    response = query_ddg("NC")
    assert isinstance(response, dict)


def test_query_presidents():
    # Tests that the results where filtered correctly
    presidents = query_presidents()
    for president in presidents:
        last_name = president["Text"].split(" - ")[0].lower().split(" ")[-1]
        assert last_name in known_presidents
