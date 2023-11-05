import os
import arff
import csv
import pandas as pd


def convert_to_arff(input_folder, output_folder):

    for _ in range(22):
        if _ == 4 or _ == 10 or _ == 13 or _ == 14:
            print("Skipped S"+str(_+2)+"!")
            continue
        input_sub_folder = input_folder + 'S' + str(_ + 2) + '/'
        output_sub_folder = output_folder + 'S' + str(_ + 2) + '/'

        for root, dir, files in os.walk(input_sub_folder):

            print(input_sub_folder)

            for input_file in files:

                output_file = input_file[:-4]+'.arff'

                # Open the CSV file in read mode and the ARFF file in write mode
                with open(input_sub_folder+input_file, "r") as csv_file, open(output_sub_folder+output_file, "w") as arff_file:

                    # Create a CSV reader object
                    csv_reader = csv.reader(csv_file)

                    # Write the relation name to the ARFF file
                    arff_file.write("@relation " + input_file[:-4] + "\n\n")

                    # Get the header row from the CSV file
                    header_row = next(csv_reader)

                    # Write the attribute names to the ARFF file
                    for attr_name in header_row:
                        arff_file.write(
                            "@attribute " + attr_name + " numeric\n")

                    # Write the data to the ARFF file
                    arff_file.write("\n@data\n")
                    for row in csv_reader:
                        arff_file.write(",".join(row) + "\n")

                print(output_file + ' generated !')

        # if not (int(input("Continue ? (1/0): "))):
        #     break

    print("Convertion of ARFF files to CSV files done !")


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


if __name__ == '__main__':

    csv_folder = r"C:/PROJECT/Data/MONO_features_csv_without_timestamps/"

    arff_folder = r"C:/PROJECT/Data/Combined_arff_discontinued/"

    folder_structure_creation(arff_folder)

    convert_to_arff(input_folder=csv_folder, output_folder=arff_folder)
