import numpy as npfile_dir = '/Users/shaique/Desktop/BioInf_IMP/BioInf_SS_2024/programming_course/project_pdfs/91_sample_txt.txt'data = dict()with open(file_dir, 'rt') as ftext:        lines = ftext.readlines()        lines = [i.strip('\n') for i in lines]    index_indices = [index for index, string in enumerate(lines) if '# index: ' in string]index_values = [lines[i] for i in index_indices]iIndex_indices = [index for index, string in enumerate(lines) if '# iIndex: ' in string]iIndex_values = [lines[i] for i in iIndex_indices]jIndex_indices = [index for index, string in enumerate(lines) if '# jIndex: ' in string]jIndex_values = [lines[i] for i in jIndex_indices]x_position_indices = [index for index, string in enumerate(lines) if ' xPosition: ' in string]x_position_values = [lines[i] for i in x_position_indices]y_position_indices = [index for index, string in enumerate(lines) if ' yPosition: ' in string]y_position_values = [lines[i] for i in y_position_indices]num_data_points_indices = [index for index, string in enumerate(lines) if '# recorded-num-points: ' in string]num_data_points_values = [lines[i] for i in num_data_points_indices]def find_non_hash_ranges(strings):        ranges = []        start_index = None    for i, string in enumerate(strings):                if not string.startswith('#'):                        if start_index is None:                                start_index = i        else:                        if start_index is not None:                                ranges.append((start_index, i - 1))                                start_index = None        # Check if there was a range that extended to the end of the list    if start_index is not None:                ranges.append((start_index, len(strings) - 1))    return rangesdef get_elements_in_ranges(strings):        ranges = find_non_hash_ranges(strings)        elements_in_ranges = []        for start, end in ranges:                elements_in_ranges.append(strings[start:end+1])            return elements_in_ranges# Example usagestrings = lineselements_in_ranges = get_elements_in_ranges(strings)outer_list = []for i in elements_in_ranges:        new_sublist = []        for j in i:                usable_elements = j.split(" ")                new_string = usable_elements[:2]                new_sublist.append(new_string)        outer_list.append(new_sublist)                #usable_elements_2 = usable_elements[:2]data_series_pattern = [0 , 1]*int((len(iIndex_indices)/2))#print(elements_in_ranges)# return a dict called 'data', such that# data[s, i, j] = (d, f),# where s is the series, i, j are the point coordinates;# d is a numpy array containing measured distances,# f is a numpy array containing measured forces.                    