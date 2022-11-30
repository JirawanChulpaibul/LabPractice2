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