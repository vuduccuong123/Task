def task1(array):
    count_number = []
    for i in array:
        a = len(i)
        count_number.append(a)

    def most_frequent(count_number):
        return max(set(count_number), key=count_number.count)

    most_appear = [i for i in array if len(i) == most_frequent(count_number)]
    return most_appear

def test_task1():
    assert task1(['a', 'ab', 'abc', 'cd', 'def', 'gh']) == ['ab', 'cd', 'gh']
    assert task1(['a', 'ab', 'abc', "-1", "-2"]) == ['ab', '-1', '-2']
    assert task1(['a', 'b', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert task1(['a','b','-1','-ab']) ==['a','b'] 
test_task1()
