def add(numbers):
    if is_empty_input(numbers):
        return handle_empty_input()
    
    if has_custom_delimiter(numbers):
        delimiter, numbers_section = extract_custom_delimiter(numbers)
        numbers_list = split_numbers(numbers_section, delimiter)
    else:
        numbers_list = split_numbers(numbers)
    
    return calculate_sum(numbers_list)

def is_empty_input(numbers):
    return numbers == ""

def handle_empty_input():
    return 0

def has_custom_delimiter(numbers):
    return numbers.startswith("//")

def extract_custom_delimiter(numbers):
    delimiter_section, numbers_section = numbers.split("\n", 1)
    delimiter = delimiter_section[2:]  # Get custom delimiter from input
    return delimiter, numbers_section

def split_numbers(numbers, delimiter=","):
    return numbers.replace("\n", delimiter).split(delimiter)

def calculate_sum(numbers_list):
    numbers_sum = 0
    for num in numbers_list:
        num_int = int(num)
        if num_int <= 1000:
            numbers_sum += num_int
    return numbers_sum
