import time
import random


def find_duplicates(numbers):
    duplicates = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])

    return duplicates


numbers = [random.randint(1, 5000) for _ in range(10000)]
start = time.perf_counter()
result = find_duplicates(numbers)
end = time.perf_counter()
print("Number of elements:", len(numbers))
print("Execution time:", end - start, "seconds")