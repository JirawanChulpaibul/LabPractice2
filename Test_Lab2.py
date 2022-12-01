import LabPractice.Lab2 as temp

def test_temp_average():
    inp =[1, 2, 3, 4, 5]
    test = 3.0
    result = temp.cal_average(inp)
    assert (result==test)

def test_temp_median():
    inp = [1, 2, 3, 4, 5]
    test = 3.0
    result = temp.calc_median_temperature(inp)
    assert (result == test)

def test_temp_min_min():
    inp = [2.0, 3.0, 4.0, 5.0]
    test = [2.0, 5.0]
    result = temp.find_min_max(inp)
    assert (result==test)