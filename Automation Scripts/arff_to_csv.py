import os
import arff
import csv
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


def convert_to_csv(input_folder, output_folder):

    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        input_sub_folder = input_folder + 'S' + str(_ + 2) + '/'
        output_sub_folder = output_folder + 'S' + str(_ + 2) + '/'

        for root, dir, files in os.walk(input_sub_folder):

            for input_file in files:

                output_file = input_file[:-5]+'.csv'

                # Open the ARFF file and load the data
                data = arff.load(open(input_sub_folder+input_file))

                # Extract the attribute names from the data
                attr_names = [attr[0] for attr in data['attributes']]

                # Extract the data instances from the data
                instances = data['data']

                # Open the CSV file for writing
                with open(output_sub_folder+output_file, 'w', newline='') as f:
                    writer = csv.writer(f)

                    # Write the attribute names as the header row
                    writer.writerow(attr_names)

                    # Write each instance as a row in the CSV file
                    for instance in instances:
                        writer.writerow(instance)

                print(output_file + ' generated !')

        if not (int(input("Continue ? (1/0): "))):
            break

        print("Convertion of ARFF files to CSV files done !")


def combine_csv(input_folder, output_folder):

    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        input_sub_folder = input_folder + 'S' + str(_ + 2) + '/'
        output_sub_folder = output_folder + 'S' + str(_ + 2) + '/'

        os.chdir(output_sub_folder)
        for root, dir, files in os.walk(input_sub_folder):
            df = pd.DataFrame()
            previous_file_name = ''
            for file in files:
                input_file = input_sub_folder+file
                print(f"Reading {input_file} !")
                limit_of_file_name = file.rfind('_')
                current_file_name = file[:limit_of_file_name]
                if (previous_file_name == current_file_name or previous_file_name == ''):
                    data = pd.read_csv(input_file)
                    df = pd.concat([df, data], axis=0)
                else:
                    csv_file = previous_file_name+'.csv'
                    print(
                        f"File name changed from {previous_file_name} to {current_file_name} !! Saving combined CSV to {csv_file}")
                    df.to_csv(csv_file, index=False)
                    df = pd.DataFrame()
                    print("-------------------------------------------------------")
                previous_file_name = current_file_name
            last_csv_of_folder = previous_file_name+'.csv'
            print(
                f"Last CSV of the folder generated !! Saving combined CSV to {last_csv_of_folder}")
            df.to_csv(last_csv_of_folder, index=False)
            os.chdir(output_folder)
            print("==========================================================")
        if not (int(input(f"Continue after {input_sub_folder}? (1/0): "))):
            break


if __name__ == '__main__':

    arff_folder = r"C:/PROJECT/Data/MONO_sliced_audio_features_in_arff/"

    multiple_csv_folder = r"C:/PROJECT/Data/MONO_sliced_audio_features_in_csv/"

    combined_csv_folder = r"C:/PROJECT/Data/MONO_features_csv/"

    # folder_structure_creation(multiple_csv_folder)

    # folder_structure_creation(combined_csv_folder)

    # convert_to_csv(input_folder = arff_folder, output_folder = multiple_csv_folder)

    # combine_csv(input_folder=multiple_csv_folder,
    #             output_folder=combined_csv_folder)
