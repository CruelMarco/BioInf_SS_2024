from collections import Counter
from itertools import islice
from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt


def extract_data_points(fname):
    # return a dict called 'data', such that
    # data[s, i, j] = (d, f),
    # where s is the series, i, j are the point coordinates;
    # d is a numpy array containing measured distances,
    # f is a numpy array containing measured forces.
    data = dict()

    with open(fname, 'rt') as ftext:
        lines = ftext.readlines()
        lines = [i.strip('\n') for i in lines]

    # Helper functions to find ranges and get elements in ranges
    def find_non_hash_ranges(strings):
        ranges = []
        start_index = None

        for i, string in enumerate(strings):
            if not string.startswith('#'):
                if start_index is None:
                    start_index = i
            else:
                if start_index is not None:
                    ranges.append((start_index, i - 1))
                    start_index = None

        if start_index is not None:
            ranges.append((start_index, len(strings) - 1))

        return ranges

    def get_elements_in_ranges(strings):
        ranges = find_non_hash_ranges(strings)
        elements_in_ranges = []
        for start, end in ranges:
            elements_in_ranges.append(strings[start:end + 1])
        return elements_in_ranges

    # Extract index, iIndex, and jIndex values
    index_indices = [index for index, string in enumerate(lines) if '# index: ' in string]
    index_values = [lines[i].split(': ')[1] for i in index_indices]

    iIndex_indices = [index for index, string in enumerate(lines) if '# iIndex: ' in string]
    iIndex_values = [lines[i].split(': ')[1] for i in iIndex_indices]

    jIndex_indices = [index for index, string in enumerate(lines) if '# jIndex: ' in string]
    jIndex_values = [lines[i].split(': ')[1] for i in jIndex_indices]

    # Extract the data series pattern (assumes alternating 0, 1 pattern)
    data_series_pattern = [0, 1] * int(len(iIndex_indices) / 2)

    # Get the elements in the ranges where data points are located
    elements_in_ranges = get_elements_in_ranges(lines)

    # Process and structure data into the dictionary
    for s, (i_val, j_val, data_range) in enumerate(zip(iIndex_values, jIndex_values, elements_in_ranges)):
        i = int(i_val)
        j = int(j_val)

        # Extract distances (d) and forces (f) from the data range
        distances = []
        forces = []

        for data_point in data_range:
            elements = data_point.split()
            if len(elements) >= 2:  # Ensure there are at least 2 elements to unpack
                distance, force = map(float, elements[:2])
                distances.append(distance)
                forces.append(force)

        d = np.array(distances)
        f = np.array(forces)

        # Assign to the dictionary
        data[(data_series_pattern[s], i, j)] = (d, f)

    return data


def raw_plot(point, curve, save=None, show=True):
    """plot one raw distance-force curve"""
    # point is the triple (s, i, j) with series s, iIndex i, jIndex j
    # curve is the pair (d, f) of two numpy arrays with distances and forces
    s, i, j = point
    d, f = curve
    plt.figure(figsize=[9, 6])
    plt.plot(d, f, label=f'Series {s}, iIndex {i}, jIndex {j}')
    plt.xlabel('Distance')
    plt.ylabel('Force')
    plt.title(f'Distance-Force Curve (Series {s}, iIndex {i}, jIndex {j})')
    #plt.legend()
    plt.grid()
    if save is not None:
        plt.savefig(save, dpi=200, bbox_inches='tight')
    if show:
        plt.show()
    plt.close()


def do_raw_plots(data, show, plotprefix):
    for point, curve in data.items():
        s, i, j = point
        print(f"plotting curve at {point}")
        fname = f'{plotprefix}-{s:01d}-{i:03d}-{j:03d}.png' if plotprefix is not None else None
        raw_plot(point, curve, show=show, save=fname)


def main(args):
    fname = args.textfile
    print(f"parsing {fname}...")
    full_data = extract_data_points(fname)
    if args.first is not None:
        data = dict((k, v) for k, v in islice(full_data.items(), args.first))
    else:
        data = full_data
    do_raw_plots(data, args.show, args.plotprefix)


def get_argument_parser():
    p = ArgumentParser()
    p.add_argument("--textfile", "-t", required=True,
                   help="name of the data file containing AFM curves for many points")
    p.add_argument("--first", type=int,
                   help="number of curves to extract and plot")
    p.add_argument("--plotprefix", default="curve",
                   help="non-empty path prefix of plot files (PNGs); do not save plots if not given")
    p.add_argument("--show", action="store_true",
                   help="show each plot")
    return p


if __name__ == "__main__":
    p = get_argument_parser()
    args = p.parse_args()
    main(args)
