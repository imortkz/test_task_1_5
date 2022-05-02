# Test task

1.5 Функция input()
Напишите программу, которая вычисляет длину отрезка (т.е. расстояние между двумя точками), заданного двумя значениями x1 и x2 (вещественные числа).

## Run program

```
$ python3 task.py
Type in `x` value, please: 3.14159
Type in `y` value, please: -3.14159
The length between `x` and `y` is 6.28318
```

## Tests

### Requirements

`pip3 install -r requirements.txt`

### Run tests

```$pytest -v

=============================================================================================================== test session starts =========================================================================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- ~/.venv/bin/python3
cachedir: .pytest_cache
rootdir: ./test_task_1_5
plugins: requests-mock-1.9.3, mock-3.6.1, repeat-0.9.1
collected 3 items                                                                                                                                                                                            

test_task.py::test_read_input_float_invalid PASSED                                                                                                                                                      
test_task.py::test_read_input_float_valid PASSED
test_task.py::test_calculate PASSED

================================================================================================================ 3 passed in 0.04s ==========================================================================
```
