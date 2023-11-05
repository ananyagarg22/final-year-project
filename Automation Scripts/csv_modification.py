import os
import csv
from datetime import datetime, timedelta
import pandas as pd


def folder_structure_creation(path):
    if not (int(input("Create folder structure in "+path+" ? (1/0): "))):
        print("Skipping folder structure creation !")
        return
    os.chdir(path)
    # os.system('cd '+path)
    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        try:
            folder_name = 'S'+str(_+2)
            if (os.path.isdir(folder_name)):
                print("Skipped S"+str(_+2)+"! Folder already exists!")
                continue
            else:
                os.system('mkdir '+folder_name)
                print("S"+str(_+2)+" created !")
        except:
            print("Error in command")
    print("Folder structure created !")
    if (int(input("Continue ? (1/0): "))):
        return
    else:
        print("Stopping the code ! Bye !")
        exit()


def timestamp_addition(csv_file):
    rows = []
    reader = csv.reader(open(csv_file, 'r', newline=''))
    for row in reader:
        rows.append(row)

    writer = csv.writer(open(csv_file, 'w', newline=''))
    start_of_time = datetime(1, 1, 1, 0, 0, 0, 0)
    begin_time = datetime(1, 1, 1, 0, 0, 0, 0)
    for i, row in enumerate(rows):
        if i == 0:
            # Add column header to header row
            row.insert(0, 'Begin Time - mm:ss.ms')
            # Add column header to header row
            row.insert(1, 'End Time - mm:ss.ms')
        else:
            # Calculate timestamp with 300ms difference
            end_time = start_of_time + timedelta(milliseconds=i*300)
            # Format timestamp as string and add to row
            row.insert(0, begin_time.strftime('%M:%S.%f'))
            row.insert(1, end_time.strftime('%M:%S.%f'))
            begin_time = end_time
        writer.writerow(row)

    print(f"Timestamps added in {csv_file} !")


def file_action(folder, action):
    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        sub_folder = folder + 'S' + str(_ + 2) + '/'

        for root, dir, files in os.walk(sub_folder):
            for input_file in files:
                # if (int(input(f"Wanna skip {input_file} ? (1/0): "))):
                #     continue
                action(sub_folder+input_file)
            # if not (int(input(f"Continue after {input_file} ? (1/0): "))):
            #     break


def single_csv_compilation_for_every_scenario(input_folder, output_folder):
    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        sub_folder = input_folder + 'S' + str(_ + 2) + '/'
        output_file_and_path = output_folder + 'S' + \
            str(_ + 2) + '_features' + '.csv'

        for root, dir, files in os.walk(sub_folder):
            dfs = []

            for input_file in files:
                # if (int(input(f"Wanna skip {input_file} ? (1/0): "))):
                #     continue
                # read the CSV file into a pandas dataframe
                if not input_file.endswith('.csv'):
                    continue

                print(f"Collecting data from {input_file}")
                df = pd.read_csv(sub_folder+input_file)
                # add a new column with the CSV file name
                df['Scenario'] = "Scenario "+str(_+2)
                # moving the column to the front
                cols = df.columns.tolist()
                cols = [cols[-1]] + cols[:-1]
                df = df[cols]
                df['Speaker'] = input_file[0:4]
                # moving the column to the front
                cols = df.columns.tolist()
                cols = [cols[-1]] + cols[:-1]
                df = df[cols]

                # append the dataframe to the list
                dfs.append(df)

        # concatenate all dataframes into one
        result = pd.concat(dfs)

        print(f"Printing compiled CSV into {output_file_and_path} ... ")
        # save the result as a new CSV file
        result.to_csv(output_file_and_path, index=False)

        # if not (int(input(f"Continue after {sub_folder} ? (1/0): "))):
        #     break

    print(
        f"CSV combined and added into {output_folder} with speaker column and scenario column addition for every scenario!")


def annotation_and_features_combo1(annotations_folder, features_folder, final_folder):

    # paths to the CSV files
    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        file_name = 'S' + str(_+2)
        features_csv_file = file_name + '_features.csv'
        features_csv_path = features_folder + features_csv_file
        annotations_csv_file = file_name + '_annotations.csv'
        annotations_csv_path = annotations_folder + annotations_csv_file
        print(
            f"Combining {features_csv_file} and {annotations_csv_file} logically into {file_name}_final.csv ...")

        # open the features csv in read mode
        with open(features_csv_path, mode='r') as features_csv:
            # also open the annotations csv in read mode
            with open(annotations_csv_path, mode='r') as annotations_csv:
                # open the output CSV file in write mode
                with open(final_folder + file_name + '.csv', mode='w', newline='') as final_csv:

                    # rows_count and array creation
                    features_row_count = 0
                    annotations_row_count = 0
                    csv_reader_annotations = []
                    csv_reader_features = []
                    # create a reader object and save the whole csv in an array from the input CSV file
                    reader = csv.reader(annotations_csv)
                    for row in reader:
                        annotations_row_count += 1
                        csv_reader_annotations.append(row)
                    # create a reader object and save the whole csv in an array from the input CSV file
                    reader = csv.reader(features_csv)
                    for row in reader:
                        features_row_count += 1
                        csv_reader_features.append(row)
                    # create a writer object for the output CSV file
                    csv_writer_final = csv.writer(final_csv)

                    annotations_row_number = 1
                    features_row_number = 1

                    # writing the columns to the final CSV
                    features_column = csv_reader_features[0]
                    final_columns = features_column
                    final_columns.insert(4, "Laughter Type")
                    # if not (int(input(f"Continue to add {final_columns} to csv ? (1/0): "))):
                    #     exit()
                    csv_writer_final.writerow(final_columns)

                    # iterate over each row in the input CSV file
                    while True:

                        if annotations_row_number == annotations_row_count:
                            annotations_row_number = 1
                            features_row_number += 1
                            if features_row_number >= features_row_count:
                                break
                            # print(
                            #     f"Annotation: {csv_reader_annotations[annotations_row_number]}")
                            # print(
                            #     f"Features: {csv_reader_features[features_row_number]}")
                            # if not (int(input(f"Continue ? (1/0): "))):
                            #     break
                        if features_row_number == features_row_count:
                            break
                        annotation_row = csv_reader_annotations[annotations_row_number]
                        features_row = csv_reader_features[features_row_number]

                        annotation_start_time = datetime.strptime(
                            annotation_row[0], '%M:%S.%f').strftime('%M:%S.%f')
                        annotation_end_time = datetime.strptime(
                            annotation_row[1], '%M:%S.%f').strftime('%M:%S.%f')

                        # print(annotation_start_time)
                        # print(annotation_end_time)
                        # print(annotation_non_laughter_state)
                        # print(annotation_laughters)
                        # print('<<<<<<<<<>>>>>>>>>>>>')

                        try:
                            features_start_time = datetime.strptime(
                                features_row[2], '%M:%S.%f').strftime('%M:%S.%f')
                            features_end_time = datetime.strptime(
                                features_row[3], '%M:%S.%f').strftime('%M:%S.%f')
                        except:
                            print(f"{features_row}")
                            exit()

                        # Row to be added to the new csv
                        speaker = features_row[0]
                        laughter_type = ''
                        for i in range(0, len(annotation_row)):
                            # print(
                            #     f"Speaker is {speaker} and i is {i} so annotation row ({annotation_row}) at i is {annotation_row[i]} which is laughter_type now")
                            if csv_reader_annotations[0][i] == speaker:
                                # print(f"First column is {csv_reader_annotations[0]} and the speaker {speaker} and we chose i={i}")
                                laughter_type = annotation_row[i]
                        if laughter_type == '':
                            laughter_type = 'non_laugh'

                        new_row = features_row.copy()

                        # if not (int(input(f"Continue ? (1/0): "))):
                        #     break

                        # feature within annotation time period
                        if features_start_time >= annotation_start_time and features_end_time < annotation_end_time:
                            print(
                                f"Feature lies within the annotation time frame:\nFeature start time ({features_start_time}) >= Annotation start time ({annotation_start_time}) and Feature end time ({features_end_time}) < Annotation end time ({annotation_end_time})")
                            # data copy processing###########
                            # no need to change time stamps, just add laughter type from annotations and write it to csv
                            ################################
                            features_row_number += 1
                        # feature ends after annotation ends
                        elif features_end_time > annotation_end_time:
                            print(
                                f"Annotation finish before the end of feature time frame:\nFeature end time ({features_end_time}) > Annotation end time ({annotation_end_time})")
                            # data copy processing###########
                            new_row[3] = annotation_end_time
                            ################################
                            annotations_row_number += 1
                        # feature starts before annotation starts
                        elif features_start_time < annotation_start_time:
                            print(
                                f"Feature finish before the start of annotation time frame:\nFeature start time ({features_start_time}) < Annotation start time ({annotation_start_time})")
                            # data copy processing###########
                            # setting the end time timestamp to annotation start time
                            new_row[2] = annotation_start_time
                            new_row[3] = features_end_time
                            features_row_number += 1
                            ################################
                        # feature and annotation end at the same time
                        elif features_end_time == annotation_end_time:
                            print(
                                f"Annotation finish with the end of feature time frame:\nFeature end time ({features_end_time}) = Annotation end time ({annotation_end_time})")
                            # data copy processing###########
                            new_row[3] = annotation_end_time
                            ################################
                            annotations_row_number += 1
                            features_row_number += 1
                        else:
                            print(
                                f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\nFeature start time ({features_start_time})\nAnnotation start time ({annotation_start_time})\nFeature end time ({features_end_time})\nAnnotation end time ({annotation_end_time})")
                            if not (int(input(f"Continue ? (1/0): "))):
                                continue
                        # if not (int(input(f"Continue adding {new_row} ? (1/0): "))):
                        #     exit()
                        new_row.insert(4, laughter_type)
                        csv_writer_final.writerow(new_row)
                    print("----------------------------------")
                    # print(columns)
        # if not (int(input(f"Continue after S{_+2} ? (1/0): "))):
        #     break


def annotation_and_features_combo2(annotations_folder, features_folder, final_folder):
    for _ in range(22):
        sub_folder = "S"+str(_+2)
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped "+sub_folder+"!")
            continue
        print(f"Inside {sub_folder}")
        annotations_sub_folder = annotations_folder + sub_folder + '/'
        features_sub_folder = features_folder + sub_folder + '/'
        final_sub_folder = final_folder + sub_folder + '/'
        for root, dir, files in os.walk(features_sub_folder):
            print(f"Found {files}")
            for i in range(len(files)):
                input_file = files[i]
                if input_file[-4:] == ".csv":
                    print(f"{input_file} being used !")
                    feature_file = features_sub_folder + input_file
                    speaker = input_file[0:4]
                    annotation_file = annotations_sub_folder + speaker + ".csv"
                    output_folder = final_sub_folder
                    session = sub_folder
                    print(f"Feature file: {feature_file}")
                    print(f"Annotation file: {annotation_file}")
                    print(f"Output file name/ Speaker: {speaker}")
                    print(f"Session: {session}")
                    sub_action_combine_feature_and_annotation(
                        annotations_csv_file=annotation_file,
                        features_csv_file=feature_file,
                        final_folder=final_sub_folder,
                        output_file_name=speaker+'-final',
                        session=session,
                        speaker=speaker
                    )
                    if (int(input(f"Continue after {input_file} ? (1/0): "))):
                        continue
                else:
                    print(f"{input_file[:-4]} != .csv")


def sub_action_combine_feature_and_annotation(annotations_csv_file, features_csv_file, final_folder, output_file_name, session, speaker):

    with open(features_csv_file, mode='r') as features_csv:
        # also open the annotations csv in read mode
        with open(annotations_csv_file, mode='r') as annotations_csv:
            # open the output CSV file in write mode
            with open(final_folder + output_file_name + '.csv', mode='w', newline='') as final_csv:
                features_row_count = 0
                annotations_row_count = 0
                csv_reader_annotations = []
                csv_reader_features = []
                # create a reader object and save the whole csv in an array from the input CSV file
                reader = csv.reader(annotations_csv)
                for row in reader:
                    annotations_row_count += 1
                    csv_reader_annotations.append(row)
                # create a reader object and save the whole csv in an array from the input CSV file
                reader = csv.reader(features_csv)
                for row in reader:
                    features_row_count += 1
                    csv_reader_features.append(row)
                # create a writer object for the output CSV file
                csv_writer_final = csv.writer(final_csv)
                annotations_row_number = 1
                features_row_number = 1

                # writing the columns to the final CSV
                features_column = csv_reader_features[0]
                final_columns = features_column
                final_columns.insert(2, "Speaker")
                final_columns.insert(3, "Session")
                final_columns.insert(4, "Laughter Type")
                csv_writer_final.writerow(final_columns)

                while True:
                    if features_row_number == features_row_count:
                        break
                    if annotations_row_number >= annotations_row_count:
                        annotations_row_number = annotations_row_count - 1
                    annotation_row = csv_reader_annotations[annotations_row_number]
                    features_row = csv_reader_features[features_row_number]

                    annotation_start_time = datetime.strptime(
                        annotation_row[0], '%M:%S.%f').strftime('%M:%S.%f')
                    annotation_end_time = datetime.strptime(
                        annotation_row[1], '%M:%S.%f').strftime('%M:%S.%f')

                    features_start_time = datetime.strptime(
                        features_row[0], '%M:%S.%f').strftime('%M:%S.%f')
                    features_end_time = datetime.strptime(
                        features_row[1], '%M:%S.%f').strftime('%M:%S.%f')

                    laughter_type = "non-laugh"

                    new_row = features_row.copy()

                    # ================TESTING=================
                    if features_start_time >= annotation_start_time and features_end_time < annotation_end_time:
                        print(
                            f"1) Feature lies within the annotation time frame:\nFeature start time ({features_start_time}) >= Annotation start time ({annotation_start_time})\nFeature end time ({features_end_time}) < Annotation end time ({annotation_end_time})")
                        # data copy processing###########
                        # no need to change time stamps, just add laughter type from annotations and write it to csv
                        ################################
                        features_row_number += 1
                        laughter_type = annotation_row[2]
                    # feature ends after annotation ends
                    elif (features_start_time < annotation_start_time and features_end_time <= annotation_start_time) or (features_start_time >= annotation_end_time and features_end_time > annotation_end_time):
                        print(
                            f"NaN) Feature does lie in Annotation time frame: \nFeature start time ({features_start_time}), Annotation start time ({annotation_start_time})\nFeature end time ({features_end_time}), Annotation end time ({annotation_end_time})")
                        features_row_number += 1
                    elif features_end_time > annotation_end_time and features_start_time < annotation_end_time:
                        print(
                            f"3) Annotation finish before the end of feature time frame:\nFeature end time ({features_end_time}) > Annotation end time ({annotation_end_time})")
                        # data copy processing###########
                        new_row[1] = annotation_end_time
                        ################################
                        annotations_row_number += 1
                        features_row_number += 1
                        laughter_type = annotation_row[2]
                    # feature starts before annotation starts
                    elif features_start_time < annotation_start_time and features_end_time > annotation_start_time:
                        print(
                            f"4) Feature finish before the start of annotation time frame:\nFeature start time ({features_start_time}) < Annotation start time ({annotation_start_time})")
                        # data copy processing###########
                        # setting the end time timestamp to annotation start time
                        new_row[0] = annotation_start_time
                        new_row[1] = features_end_time
                        features_row_number += 1
                        laughter_type = annotation_row[2]
                        ################################
                    # feature and annotation end at the same time
                    elif features_end_time == annotation_end_time:
                        print(
                            f"5) Annotation finish with the end of feature time frame:\nFeature end time ({features_end_time}) = Annotation end time ({annotation_end_time})")
                        # data copy processing###########
                        new_row[1] = annotation_end_time
                        ################################
                        annotations_row_number += 1
                        features_row_number += 1
                        laughter_type = annotation_row[2]
                    else:
                        print(
                            f"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\nFeature start time ({features_start_time})\nAnnotation start time ({annotation_start_time})\nFeature end time ({features_end_time})\nAnnotation end time ({annotation_end_time})")
                    # ========================================

                    # if features_start_time >= annotation_start_time and features_end_time <= annotation_end_time:
                    #     print(
                    #         f"1) Feature lies within the annotation time frame:\nFeature start time ({features_start_time}) >= Annotation start time ({annotation_start_time}) and Feature end time ({features_end_time}) <= Annotation end time ({annotation_end_time})")
                    #     laughter_type = annotation_row[2]
                    #     features_row_number += 1
                    # elif features_start_time < annotation_start_time and features_end_time < annotation_start_time:
                    #     print(
                    #         f"2) Both features start and end time are before annotation start time: \nFeature start time ({features_start_time}) < Annotation start time ({annotation_start_time}) and Feature end time ({features_end_time}) < Annotation start time ({annotation_start_time})")
                    #     features_row_number += 1

                    # elif features_start_time > annotation_end_time:
                    #     print(
                    #         f"3) Features do not lie in the annotations time frame: \nFeature start time ({features_start_time}) > Annotation end time ({annotation_end_time})")
                    #     annotations_row_number += 1
                    #     continue
                    # elif features_end_time > annotation_end_time:
                    #     print(
                    #         f"4) Annotation finish before the end of feature time frame:\nFeature end time ({features_end_time}) > Annotation end time ({annotation_end_time})")
                    #     new_row[0] = features_start_time
                    #     new_row[1] = annotation_end_time
                    #     annotations_row_number += 1
                    #     features_row_number += 1
                    #     laughter_type = annotation_row[2]
                    # elif features_start_time < annotation_start_time:
                    #     print(
                    #         f"5) Features start before the annotation start frame:\nFeature start time ({features_start_time}) < Annotation start time ({annotation_start_time})")
                    #     new_row[0] = annotation_start_time
                    #     new_row[1] = features_end_time
                    #     features_row_number += 1
                    # elif features_end_time == annotation_end_time:
                    #     print(
                    #         f"6) Features end with the annotation end frame:\nFeature end time ({features_end_time}) == Annotation end time ({annotation_end_time})")
                    #     new_row[1] = annotation_end_time
                    #     annotations_row_number += 1
                    #     features_row_number += 1

                    new_row.insert(2, speaker)
                    new_row.insert(3, session)
                    new_row.insert(4, laughter_type)
                    csv_writer_final.writerow(new_row)


def combine_into_one(folder, output_folder):
    # open the output CSV file in write mode
    with open(output_folder + '1. FinalCSV.csv', mode='w', newline='') as final_csv:
        csv_writer_final = csv.writer(final_csv)
        for _ in range(22):
            sub_folder = "S"+str(_+2)
            if _ == 4 or _ == 10 or _ == 13 or _ == 14:
                print("Skipped "+sub_folder+"!")
                continue
            print(f"Inside {sub_folder}")

            sub_folder = folder + sub_folder + '/'

            for root, dir, files in os.walk(sub_folder):
                for file in files:
                    if file[-4:] == '.csv':
                        first_row = True
                        print(f"{file} being used !")
                        with open(sub_folder + file, mode='r') as current_csv:
                            reader = csv.reader(current_csv)
                            for row in reader:
                                if first_row:
                                    first_row = False
                                    continue
                                else:
                                    # print("Writing row!")
                                    csv_writer_final.writerow(row)


if __name__ == '__main__':

    csv_folder_without_timestamp = r"C:/PROJECT/Data/5.MONO_features_csv_without_timestamps/"
    csv_folder_processed = r"C:/PROJECT/Data/6.MONO_features_csv/"
    csv_folder_features1 = r"C:/PROJECT/Data/scenario_audio_features_csv/"
    csv_folder_annotation1 = r"C:/PROJECT/Data/scenario_annotations_csv/"
    csv_folder_final1 = r"C:/PROJECT/Data/FINAL_CSVs_Method1_redundant/"

    csv_folder_features2 = r"C:/PROJECT/Data/6.MONO_features_csv/"
    csv_folder_annotation2 = r"C:/PROJECT/Data/Individual-Annotations-CSV/"
    csv_folder_final2 = r"C:/PROJECT/Data/FINAL_CSVs_Method2_chosen/"

    project_folder = r"C:/PROJECT/Data/FinalCSVs/"
    # file_action(csv_folder_processed, timestamp_addition)
    # single_csv_compilation_for_every_scenario(
    #     csv_folder_processed, csv_folder_features)
    # annotation_and_features_combo1(
    #     csv_folder_annotation1, csv_folder_features1, csv_folder_final1)
    # folder_structure_creation(csv_folder_final2)
    # annotation_and_features_combo2(
    #     csv_folder_annotation2, csv_folder_features2, csv_folder_final2)
    combine_into_one(csv_folder_final2, project_folder)
