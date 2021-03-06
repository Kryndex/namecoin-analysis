from collections import Counter
from random import choice

def load_name_length():
    histogram = Counter()
    with open("plotNameLength.txt", "r") as histogram_file:
        for line in histogram_file:
            line = line.replace("\n", "")
            length, count = line.split(" ")
            length = int(length)
            count = int(count)
            histogram[length] = count
    return histogram

def sample_from_histogram(histogram, num_samples):
    elements = histogram.elements()
    return [choice(elements) for _ in range(num_samples)]

def namelength_cost(length, base_price = 10):
    if length <= 3:
        return 5 * base_price
    elif length <= 6:
        return 2 * base_price
    elif length <= 14:
        return 0.5 * base_price
    else:
        return 0.02
