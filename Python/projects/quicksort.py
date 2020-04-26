from random import randrange


def partition(array, lower, upper, pivot):
    array[pivot], array[upper] = array[upper], array[pivot]
    partition_index = lower
    for i in range(lower, upper):
        if array[i] < array[upper]:
            array[i], array[partition_index] = array[partition_index], array[i]
            partition_index += 1
    array[partition_index], array[upper] = array[upper], array[partition_index]
    return partition_index


def quick_sort(array, lower, upper):
    if lower >= upper:
        return array
    pivot = randrange(lower, upper + 1)  # + 1 bc range doesn't include upper
    new_pivot = partition(array, lower, upper, pivot)
    quick_sort(array, lower, new_pivot - 1)
    quick_sort(array, new_pivot + 1, upper)


def main():
    a = [3, 1, 5, 7, 9, 4, 8, 2, 6]
    print('unsorted: ', a)
    quick_sort(a, 0, len(a) - 1)
    print('sorted: ', a)


if __name__ == '__main__':
    main()
