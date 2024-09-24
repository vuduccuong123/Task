def task2(array):
    if len(array) < 2:
        raise ValueError("Error: The array must contain at least two elements.")
    for i in array:
        if not isinstance(i, (int, float)):
            raise ValueError("Error: All elements in the array must be integers or floats.")
        
    count_number = []
    for i in array:
        count_number.append(i)
    count_number.sort(reverse=True)
    result = count_number[0] + count_number[1]
    return result

def test_task2():
    assert task2([1, 2, 3]) == 5          
    assert task2([1.5, 2.5, 3]) == 5.5    
    assert task2([1, 2, 3.3, 4.4]) == 7.7  
    assert task2([5, 1.5, 30.0]) == 35.0  
    assert task2([-5,-6.1,-7]) == -11.1
    try:
        task2([])  
    except ValueError as e:
        assert str(e) == "Error: The array must contain at least two elements."

    try:
        task2([1, 2, '3','hello']) 
    except ValueError as e:
        assert str(e) == "Error: All elements in the array must be integers or floats."
test_task2()