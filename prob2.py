import os
import math

def parse_input(input_str):
    parameters = input_str.split('\n')
    wafer_diameter = float(parameters[0].split(":")[1])
    die_size = tuple(map(int, parameters[1].split(":")[1].split('x')))
    die_shift_vector = tuple(map(int, parameters[2].split(":")[1].strip('()').split(',')))
    reference_die = tuple(map(float, parameters[3].split(":")[1].strip('()').split(',')))

    return wafer_diameter, die_size, die_shift_vector, reference_die

def calculate_die_indices(wafer_diameter, die_size):
    num_rows = math.ceil(wafer_diameter / die_size[1])
    num_cols = math.ceil(wafer_diameter / die_size[0])

    die_indices = []
    for row in range(num_rows):
        for col in range(num_cols):
            die_indices.append((row, col))

    return die_indices

def calculate_llc(die_index, die_size, die_shift_vector, reference_die):
    llc_x = die_index[1] * die_size[0] + die_shift_vector[0] + reference_die[0]
    llc_y = die_index[0] * die_size[1] + die_shift_vector[1] + reference_die[1]

    return llc_x, llc_y

def dfs_process_dies(die_indices, die_size, die_shift_vector, reference_die):
    for die_index in die_indices:
        llc = calculate_llc(die_index, die_size, die_shift_vector, reference_die)
        print(f"{die_index}:{llc}")

# Input
sample_input = """WaferDiameter:300
DieSize:30x30
DieShiftVector:(0,0)
ReferenceDie:(15,15)"""

# Parse input
wafer_diameter, die_size, die_shift_vector, reference_die = parse_input(sample_input)

# Calculate die indices
die_indices = calculate_die_indices(wafer_diameter, die_size)

# Process dies using DFS-inspired approach
dfs_process_dies(die_indices, die_size, die_shift_vector, reference_die)
