import os
import sys

def clean(list_to_filter):
    cleaned = []
    for item in list_to_filter:
        if 'DS_Store' not in item:
            cleaned.append(item)
    return cleaned

def filter(filter, list_to_filter):
    process = []
    for entry in list_to_filter:
        if filter in entry and 'DS_Store' not in entry:
            process.append(entry)
        else:
            warning = '!! ' + entry + ' not a ' + filter + ' file !!'
            print(warning)
    return process


items = os.listdir('./tech_dataset_x')
folders = clean(items)

for folder in folders:
    #file ops
    folder_pf = folder.replace(' ', ' ')
    files = filter('.mid', clean(os.listdir('./tech_dataset_x/' + folder_pf)))

    for file in files:
        src = './tech_dataset_x/' + folder_pf + '/' + file
        dst = './tech_dataset_x/' + folder_pf + '/' + file.replace(' ', '_')
        os.rename(src, dst)

    folder_src = './tech_dataset_x/' + folder_pf
    folder_dst = './tech_dataset_x/' + folder.replace(' ', '_')
    os.rename(folder_src, folder_dst)
