def optimized_compute(data):
    from itertools import accumulate
    
    # Using accumulate to improve performance over manual loops
    return list(accumulate(data))


def filter_even_numbers(nums):
    return (num for num in nums if num % 2 == 0)


def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]  


def batch_process(data, batch_size=10):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]


def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0.0


def compute_statistics(data):
    mean_val = calculate_mean(data)
    filtered_data = list(filter_even_numbers(data))
    return mean_val, filtered_data
