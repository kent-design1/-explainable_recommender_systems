import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
data = pd.read_csv("data/csvData/finalDataset.csv")  # Your dataset
input_data = pd.read_csv('data/csvData/patient_for_recommendation.csv')

# Concatenate the input data with the original dataset to ensure all columns are present
all_data = pd.concat([data, input_data], ignore_index=False, axis=0)

unique_values_LabName = all_data['LabName'].unique()

unique_values_PID_AID = pd.DataFrame(all_data)
unique_values_PID_AID = unique_values_PID_AID.drop_duplicates(subset=['PatientID', 'AdmissionID'])
x = unique_values_PID_AID['PatientID']
y = unique_values_PID_AID['AdmissionID']
matrix_i = [f'{pid}_{aid}' for pid, aid in zip(x, y)]

f_df = pd.DataFrame(index=matrix_i, columns=unique_values_LabName)

for index, row in all_data.iterrows():
    comb = f'{row["PatientID"]}_{row["AdmissionID"]}'
    labname = row['LabName']
    labvalue = row['LabValue']
    f_df.loc[comb, labname] = labvalue

f_df = f_df.fillna(0)

f_df.index.name = 'PatientInfo'  # Set the index name
f_df.reset_index(inplace=True)  # Reset the index to a regular column

# Calculate cosine similarity
cosine_sim = cosine_similarity(f_df.drop('PatientInfo', axis=1))

# Create a DataFrame for cosine similarity
cosine_sim_df = pd.DataFrame(cosine_sim, index=f_df['PatientInfo'], columns=f_df['PatientInfo'])

# Sort columns based on the cosine similarity of the last row (input patient)
sorted_columns = cosine_sim_df.iloc[-1, :-1].sort_values(ascending=False)

# Extract the top 10 column names
top_10_similarities = sorted_columns.head(10)
top_10 = top_10_similarities.index

# Filter the data DataFrame based on matching indices
filtered_data = data[data.apply(lambda row: f"{row['PatientID']}_{row['AdmissionID']}" in top_10, axis=1)]

# Extract the values of "dia" and "desc" columns
patient = filtered_data[['PatientID', 'AdmissionID']].drop_duplicates()
dia_values = filtered_data['PrimaryDiagnosisCode'].unique()
desc_values = filtered_data['PrimaryDiagnosisDescription'].unique()

# Convert integer values to strings
patient['PatientID'] = patient['PatientID'].astype(str)
patient['AdmissionID'] = patient['AdmissionID'].astype(str)

patient_dict = {'patient': patient['PatientID'] + '_' + patient['AdmissionID']}
dia_dict = {'desc': dia_values}
desc_dict = {'dia': desc_values}

top_10_scores_only = []

for i in range(len(top_10_similarities)):
    top_10_scores_only.append(top_10_similarities[i])

sim_score = {'sim_score': top_10_scores_only}

# Construct the DataFrame
result_df = pd.DataFrame({**patient_dict, **dia_dict, **desc_dict, **sim_score})
result_df.to_csv('final_recommendation.csv', index=False)
