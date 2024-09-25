import time
import sys

def merge_dicts(dict1, dict2):
    start_time = time.time()
    merged_dict = {**dict1, **dict2}

    end_time = time.time()
    
    execution_time = end_time - start_time
    space_used = sys.getsizeof(merged_dict)
    
    print(f"Time taken to merge dictionaries: {execution_time:.6f} seconds")
    print(f"Space used by merged dictionary: {space_used} bytes")
    
    return merged_dict


def intersect_dicts(dict1, dict2):
    start_time = time.time()
    intersection = {key: dict1[key] for key in dict1 if key in dict2}
    
    end_time = time.time()
    
    execution_time = end_time - start_time
    space_used = sys.getsizeof(intersection)
    
    print(f"Time taken to find intersection: {execution_time:.6f} seconds")
    print(f"Space used by intersection dictionary: {space_used} bytes")
    
    return intersection


def word_frequency(word_list):
    start_time = time.time()
    
    frequency_dict = {}
    for word in word_list:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    
    end_time = time.time()
    
    execution_time = end_time - start_time
    space_used = sys.getsizeof(frequency_dict)
    
    print(f"Time taken to count word frequency: {execution_time:.6f} seconds")
    print(f"Space used by frequency dictionary: {space_used} bytes")
    
    return frequency_dict


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency_dict = word_frequency(words)
print(frequency_dict)



dict_x = {'a': 1, 'b': 2, 'c': 3}
dict_y = {'b': 4, 'c': 5, 'd': 6}
intersection_dict = intersect_dicts(dict_x, dict_y)
print(intersection_dict)


dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict_a, dict_b)
print(merged_dict)