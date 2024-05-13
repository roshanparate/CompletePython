import function_in_python

def test_calculate_total():
    val_list = [12, 13, 45, 46, 78, 79, 10]
    total = function_in_python.calculate_total(val_list)
    assert total == 283