arr = [2, 3, 11, 11, -3]
max_value = 0
for index, value in enumerate(arr):
    if value > max_value:
        max_value = value

# print(max_value)
print(arr.count(max_value))


def test_find_count_of_largest_numner_in_array():
    assert arr.count(max_value)
