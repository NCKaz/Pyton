numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = numbers.index(None)
full_numbers = [int(i) for i in numbers if i is not None]
average = sum(full_numbers)/len(numbers)
numbers[index] = average
print("Измененный список:", numbers)
