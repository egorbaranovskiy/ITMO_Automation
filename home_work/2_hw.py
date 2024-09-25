def task_1() -> None:
    my_int = 42
    my_float = 3.14
    my_str = "Привет, мир!"
    my_list = [1, 2, 3, 4, 5]
    my_bool = True

    print(type(my_int))
    print(type(my_float))
    print(type(my_str))
    print(type(my_list))
    print(type(my_bool))

task_1()


def task_2() -> None:

    a = [1, 2, 3, 5, 8, 13, 21] #последовательность Фибоначи

    print(a[0:3])


task_2()



def task_3(number: int) -> int:
    return number ** 2

result = task_3(5)
print(result)