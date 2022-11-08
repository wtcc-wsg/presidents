from main import query_ddg, query_presidents, known_presidents


def test_query_ddg():
    # Test that json was returned
    response = query_ddg("NC")
    assert isinstance(response, dict)


def test_query_presidents():
    # Tests that all presidents where in response
    presidents_dict = query_presidents()
    seen = known_presidents.copy()
    for president in presidents_dict:
        last_name = president["Text"].split(" - ")[0].lower().split(" ")[-1]
        if last_name in seen:
            seen.remove(last_name)

    assert seen == []
