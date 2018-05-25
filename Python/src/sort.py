# -*- coding: utf-8 -*-

number_list = [45, 33, 12, 0, -5, 55555, 1, 444, 99, 66, 66, 12]


def bubble_sort(num_list):
    n_list = num_list[:]
    for i in range(0, len(n_list)):
        for j in range(0, len(n_list) - i - 1):
            if n_list[j] > n_list[j+1]:
                n_list[j], n_list[j+1] = n_list[j+1], n_list[j]
    return n_list


def cocktail_sort(num_list):
    n_list = num_list[:]
    left, right = 0, len(n_list)-1
    while left < right:
        # sort right half
        for i in range(left, right):
            if n_list[i] > n_list[i+1]:
                n_list[i], n_list[i+1] = n_list[i+1], n_list[i]
        right -= 1

        # sort left half
        for j in range(right, left, -1):
            if n_list[j] < n_list[j-1]:
                n_list[j], n_list[j-1] = n_list[j-1], n_list[j]
        left += 1
    return n_list


def selection_sort(num_list):
    n_list = num_list[:]
    for i in range(0, len(n_list)):
        min_index = i
        for j in range(i+1, len(n_list)):
            if n_list[j] < n_list[min_index]:
                min_index = j
        n_list[i], n_list[min_index] = n_list[min_index], n_list[i]
    return n_list


def insert_sort(num_list):
    n_list = num_list[:]
    length = len(number_list)
    for i in range(1, length):
        to_order_ele = n_list[i]
        # for j in range(i-1, -1, -1):
        #     if n_list[j] > to_order_ele:
        #         n_list[j+1] = n_list[j]
        #     else:
        #         break
        # if j == 0:
        #     n_list[j] = to_order_ele
        # else:
        #     n_list[j+1] = to_order_ele
        j = i - 1
        while j >= 0 and n_list[j] > to_order_ele:
            n_list[j+1] = n_list[j]
            j -= 1
        n_list[j+1] = to_order_ele
    return n_list


def insert_sort_with_dichotomy(num_list):
    n_list = number_list[:]
    length = len(n_list)

    # 假设最左边的数据都是有序的，针对之后的每个数字排序
    for i in range(1, length):
        to_sort_number = n_list[i]
        j = i - 1
        left = 0
        right = j

        # 二分找到该数字应该在的位置
        while left <= right:
            mid = (left + right) / 2
            if to_sort_number > n_list[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # 移动该位置右边的数据，并插入该数字
        for k in range(i-1, left-1, -1):
            n_list[k+1] = n_list[k]

        n_list[left] = to_sort_number
    return n_list


def merge(left, right):
    merged, left_to_merge, right_to_merge = [], left, right
    while left and right:
        merged.append(left_to_merge.pop(0) if left_to_merge[0] < right_to_merge[0] else right_to_merge.pop(0))
    merged.extend(left_to_merge if left_to_merge else right_to_merge)
    return merged


def merge_sort(num_list):
    n_list = num_list[:]

    if len(n_list) == 1:
        return n_list

    mid = len(n_list) / 2
    left = merge_sort(n_list[:mid])
    right = merge_sort(n_list[mid:])
    return merge(left, right)


# def merge_sort_iteration(num_list):
#     n_list = num_list[:]
#     i = 1
#     length = len(n_list)
#     left = 0
#     right = left + i
#
#     while left + i < length:
#         merge(n_list[left: i], n_list(i, right))


if __name__ == "__main__":
    sorted_list = number_list[:]
    sorted_list.sort()
    assert bubble_sort(number_list) == sorted_list
    assert cocktail_sort(number_list) == sorted_list
    assert selection_sort(number_list) == sorted_list
    assert insert_sort(number_list) == sorted_list
    assert insert_sort_with_dichotomy(number_list) == sorted_list
    assert merge_sort(number_list) == sorted_list