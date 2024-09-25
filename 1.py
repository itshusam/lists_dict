import time
import sys

def squares(n):
    start_time = time.time()
    squares_list = [x**2 for x in range(1, n + 1)]
    end_time = time.time()
    
    execution_time = end_time - start_time
    space_used = sys.getsizeof(squares_list)
    
    print(f"Time taken to create squares list: {execution_time:.6f} seconds")
    print(f"Space used by squares list: {space_used} bytes")
    
    return squares_list




def reverse_sublist(lst, i, j):
    if i < 0 or j >= len(lst) or i >= j:
        return lst

    start_time = time.time()
    lst[i:j + 1] = lst[i:j + 1][::-1]
    end_time = time.time()
    
    execution_time = end_time - start_time
    space_used = sys.getsizeof(lst)
    
    print(f"Time taken to reverse sublist: {execution_time:.6f} seconds")
    print(f"Space used by list after reversing: {space_used} bytes")
    
    return lst


def merge_sorted_lists(list1, list2):
    start_time = time.time()
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    end_time = time.time()
    
    execution_time = end_time - start_time
    space_used = sys.getsizeof(merged_list)
    
    print(f"Time taken to merge lists: {execution_time:.6f} seconds")
    print(f"Space used by merged list: {space_used} bytes")
    
    return merged_list




n = 10
squares_list = squares(n)
print(squares_list)


example_list = [1, 2, 3, 4, 5]
reversed_list = reverse_sublist(example_list, 1, 3)
print(reversed_list)

sorted_list1 = [1, 3, 5]
sorted_list2 = [2, 4, 6]
merged_list = merge_sorted_lists(sorted_list1, sorted_list2)
print(merged_list)