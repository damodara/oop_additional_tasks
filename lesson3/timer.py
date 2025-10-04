"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""


class Timer:
    def __enter__(self):
        self.count_start = 0
        self.elapsed_time = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        count_end = 0
        for _ in range(1000000):
            count_end += 1
        self.elapsed_time = count_end - self.count_start
        print(f"Приблизительное время выполнения: {self.elapsed_time / 1000000 : .6f} условных единиц.")


with Timer() as timer:
    # блок кода
    total_sum = 0
    for i in range(1_000_000):
        total_sum += i
    # код для проверки 
    print("Execution time:", timer.elapsed_time)
