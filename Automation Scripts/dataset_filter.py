import pandas as pd
import numpy as np


def dataset_gen(random_num):
    # Load CSV file into a Pandas DataFrame
    data = pd.read_csv(
        'C:\PROJECT\Data\FinalCSVs\\2. FinalCSV_without_useless_columns.csv')

    # Filter rows where the value in the 'laughter_type' column is 'mirthful' or 'discourse'
    mirthful_discourse_rows = data.loc[data['Laughter Type'].isin(
        ['Mirthful', 'Discourse'])]

    # Filter rows where the value in the 'laughter_type' column is not 'mirthful' or 'discourse'
    non_mirthful_discourse_rows = data.loc[data['Laughter Type'].isin(
        ['non-laugh'])]

    # Randomly select 50% of the non-laugh rows
    sampled_non_laugh_rows = non_mirthful_discourse_rows.sample(
        frac=0.016722, random_state=random_num)

    print(
        f"Number of rows of mirthful and discourse = {len(mirthful_discourse_rows)}")
    print(
        f"Number of rows of non-laugh = {len(sampled_non_laugh_rows)}")

    # Combine the mirthful/discourse rows with the randomly sampled non-laugh rows
    selected_rows = pd.concat(
        [mirthful_discourse_rows, sampled_non_laugh_rows])

    # Export the selected rows to a new CSV file
    selected_rows.to_csv(
        'C:\PROJECT\Data\FinalCSVs\\3. FinalCSV_filtered_'+str(random_num)+'.csv', index=False)


def dataset_gen_mirthful_discourse():
    # Load CSV file into a Pandas DataFrame
    data = pd.read_csv(
        'C:\PROJECT\Data\FinalCSVs\\2. FinalCSV_without_useless_columns.csv')

    # Filter rows where the value in the 'laughter_type' column is 'mirthful' or 'discourse'
    mirthful_discourse_rows = data.loc[data['Laughter Type'].isin(
        ['Mirthful', 'Discourse'])]

    print(
        f"Number of rows of mirthful and discourse = {len(mirthful_discourse_rows)}")

    # Export the selected rows to a new CSV file
    mirthful_discourse_rows.to_csv(
        'C:\PROJECT\Data\FinalCSVs\\3. FinalCSV_filtered_mirthful_discourse.csv', index=False)


if __name__ == '__main__':
    dataset_gen_mirthful_discourse()
    print(f"Dataset generation with only mirthful and discourse laughter completed !")
    random_states = [42, 52, 62]
    for num in random_states:
        print("===========================================================")
        dataset_gen(num)
        print(f"Dataset generation with random state = {num} completed !")
