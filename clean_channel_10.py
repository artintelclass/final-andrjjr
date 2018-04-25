import os
import sys

def filter(filter, list_to_filter):
    process = []
    for entry in list_to_filter:
        if filter in entry and 'DS_Store' not in entry:
            process.append(entry)
        else:
            warning = '!! ' + entry + ' not a ' + filter + ' file !!'
            print(warning)
    return process

def clean(list_to_filter):
    cleaned = []
    for item in list_to_filter:
        if 'DS_Store' not in item:
            cleaned.append(item)
    return cleaned


# create list of filenames, in the input directory
items = os.listdir('./tech_dataset_x')
folders = clean(items)
print(items)
print(folders)

# for folder in folders:
#     folder.replace(' ', '\\ ')
# print(folders)

# Midi to CSV
for folder in folders:
    os.mkdir('./tech_dataset_x/' + folder + '/csvs')
    os.mkdir('./tech_dataset_x/' + folder + '/csvs/processed_csvs')

    files = os.listdir('./tech_dataset_x/' + folder)
    files_processed = filter('.mid', files)
    for f in files_processed:
        f.replace(' ', '\\ ')

    pathtomidi = './tech_dataset_x/' + folder + '/'
    pathforcsv = './tech_dataset_x/' + folder + '/csvs/'
    for object in files_processed:
        midi_to_csv = 'midicsv ' + pathtomidi + object + ' ' + pathforcsv + object.replace('.mid', '.csv')
        os.system(midi_to_csv)
    print('Converted ' + str(len(files_processed)) + ' MIDI files to CSVs')

# CSV processing
for folder in folders:
    unprocessed_csvs = os.listdir('./tech_dataset_x/' + folder + '/csvs/')
    filtered_csvs = filter('.csv', unprocessed_csvs)

    for csv in filtered_csvs:                           # for each csv file in /csvs/
        fp = open('./tech_dataset_x/' + folder + '/csvs/' + csv)           # open csv as file object
        fp_ls = []
        for line in fp:                                         # read each line into a list
            fp_ls.append(line)
        fp.close

        for i in range(len(fp_ls)):                             # for the length of the list
            if 'Time_signature' in fp_ls[i]:                    # if the row contains a time_sig event,
                # print('Time sig entry!')
                fp_ls.pop(i)                                        # pop it
                break                                               # break the loop

        ## change the channel to channel 10 for all note_on/off events
        for i in range(len(fp_ls)):
            string = fp_ls[i]
            if 'Note_on_c' in string or 'Note_off_c' in string:
                elements = string.split(', ')
                elements.pop(3)
                elements.insert(3, '9')
                new_string = ', '.join(elements)
                fp_ls.pop(i)
                fp_ls.insert(i, new_string)


        # create new file to write the processed .csv
        fp_processed = open('./tech_dataset_x/' + folder + '/csvs/processed_csvs/' + csv, 'w')
        for line in fp_ls:
            fp_processed.write(line)
        fp_processed.close()

# re-encode as midi
for folder in folders:
    csv_files = os.listdir('./tech_dataset_x/' + folder + '/csvs/processed_csvs')
    csv_files_processed = filter('.csv', csv_files)

    pathtocsv = './tech_dataset_x/' + folder + '/csvs/processed_csvs/'
    pathformidi = './processed_dataset/'
    for object in csv_files_processed:
        csv_to_midi = 'csvmidi ' + pathtocsv + object + ' ' + pathformidi + object.replace('.csv', '.mid')
        os.system(csv_to_midi)

    print('Reverted ' + str(len(files_processed)) + ' CSV files back to MIDI')
