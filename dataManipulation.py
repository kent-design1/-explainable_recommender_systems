import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Load data
diagnoses_data = pd.read_csv('data/csvData/AdmissionsDiagnosesCorePopulatedTable.csv')
labs_data = pd.read_csv('data/csvData/LabsCorePopulatedTable.csv')

# Handle missing values (if any)
diagnoses_data.fillna(0, inplace=True)
labs_data.fillna(0, inplace=True)

# Add a column called PrimaryDiagnosisSubCode to split PrimaryDiagnosisCode into main diagnosis and subType
sub_array = []
main_array = []
for i in diagnoses_data['PrimaryDiagnosisCode']:
    main_array.append(i.split(".")[0])
    if len(i.split(".")) > 1:
        sub_array.append(i.split(".")[1])
    else:
        sub_array.append('-')

diagnoses_data['PrimaryDiagnosisCode'] = main_array
diagnoses_data['PrimaryDiagnosisSubCode'] = sub_array

diagnoses_data.to_csv('data/csvData/AdmissionsDiagnosesCorePopulatedTableEdited.csv', index=False)

# Convert to dataframe

d = pd.DataFrame(diagnoses_data)
l = pd.DataFrame(labs_data)

l = l.drop('LabDateTime', axis=1)

final_df = l.copy()
primaryDiagnosisCode = [0] * len(l['PatientID'])
primaryDiagnosisSubCode = [0] * len(l['PatientID'])
primaryDiagnosisDescription = [0] * len(l['PatientID'])

for i in range(len(d)):
    for j in range(len(l)):
        if d['PatientID'][i] == l['PatientID'][j] and d['AdmissionID'][i] == l['AdmissionID'][j]:
            primaryDiagnosisCode[j] = d['PrimaryDiagnosisCode'][i]
            primaryDiagnosisSubCode[j] = d['PrimaryDiagnosisSubCode'][i]
            primaryDiagnosisDescription[j] = d['PrimaryDiagnosisDescription'][i]

final_df['PrimaryDiagnosisDescription'] = primaryDiagnosisDescription.copy()
final_df['PrimaryDiagnosisCode'] = primaryDiagnosisCode.copy()
final_df['PrimaryDiagnosisSubCode'] = primaryDiagnosisSubCode.copy()

final_df.to_csv('data/csvData/finalDataset.csv', index=False)