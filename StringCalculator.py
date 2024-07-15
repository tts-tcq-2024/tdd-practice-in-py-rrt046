def add(numbers):
    if is_empty(numbers):
        return handle_empty_input(numbers)
    
    if is_single_number(numbers):
        return handle_single_number(numbers)
    
    if has_custom_delimiter(numbers):
        delimiter, numbers_section = extract_custom_delimiter(numbers)
        return handle_numbers(numbers_section, delimiter)
    
    return handle_numbers(numbers, ",")

def is_empty(numbers):
    return numbers == ""

def handle_empty_input(numbers):
    return 0

def is_single_number(numbers):
    return numbers.isdigit()

def handle_single_number(numbers):
    return int(numbers)

def has_custom_delimiter(numbers):
    return numbers.startswith("//")

def extract_custom_delimiter(numbers):
    delimiter_section, numbers_section = numbers.split("\n", 1)
    delimiter = delimiter_section[2:]  # Get custom delimiter from input
    return delimiter, numbers_section

def handle_numbers(numbers, delimiter):
    numbers_list = numbers.split(delimiter)
    numbers_sum = 0
    
    for num in numbers_list:
        num_int = int(num)
        if num_int <= 1000:
            numbers_sum += num_int
    
    return numbers_sum

