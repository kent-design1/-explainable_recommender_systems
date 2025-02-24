import pandas as pd

# Load data
diagnoses_data = pd.read_csv('data/csvData/AdmissionsDiagnosesCorePopulatedTable.csv')
labs_data = pd.read_csv('data/csvData/LabsCorePopulatedTable.csv')

# Handle missing values (if any)
diagnoses_data.fillna(0, inplace=True)
labs_data.fillna(0, inplace=True)

diagnoses_data.to_csv('data/csvData/AdmissionsDiagnosesCorePopulatedTableEdited.csv', index=False)

# Convert to dataframe
d = pd.DataFrame(diagnoses_data)
labs_data = pd.DataFrame(labs_data).drop('LabDateTime', axis=1)

final_df = labs_data.copy()
primaryDiagnosisCode = [0] * len(labs_data['PatientID'])
primaryDiagnosisDescription = [0] * len(labs_data['PatientID'])

for i in range(len(d)):
    for j in range(len(labs_data)):
        if d['PatientID'][i] == labs_data['PatientID'][j] and d['AdmissionID'][i] == labs_data['AdmissionID'][j]:
            primaryDiagnosisCode[j] = d['PrimaryDiagnosisCode'][i]
            primaryDiagnosisDescription[j] = d['PrimaryDiagnosisDescription'][i]

final_df['PrimaryDiagnosisDescription'] = primaryDiagnosisDescription.copy()
final_df['PrimaryDiagnosisCode'] = primaryDiagnosisCode.copy()
final_df.to_csv('data/csvData/finalDataset.csv', index=False)
