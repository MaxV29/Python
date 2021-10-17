def my_func(num_1, num_2, num_3):
    my_func = max(num_1, num_2, num_3) + max(min(num_1, num_2), min(num_1, num_3), min(num_3, num_2))
    return my_func

print(my_func(50, 20, 30))