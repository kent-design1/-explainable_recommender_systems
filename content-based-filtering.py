import csv

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
data = pd.read_csv("data/csvData/finalDataset.csv")

# Create patient profiles based on diagnoses and test results
patient_profiles = data.pivot_table(index=['PatientID', 'AdmissionID'], columns='LabName', values='LabValue', fill_value=0)

# Calculate cosine similarity between patients
cosine_sim = cosine_similarity(patient_profiles)
print(len(cosine_sim[0]))
# Define a function to recommend treatments for a given patient
# def recommend_treatments(patient_id):
#     patient_index = patient_profiles.index.get_loc(patient_id)
#     # print(cosine_sim[patient_index])
#     sim_scores = list(enumerate(cosine_sim[patient_index]))
#     # print(sim_scores)
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:10]  # Get the top 10 similar patients (excluding the patient itself)
#     similar_patients = [i[0] for i in sim_scores]
#
#     # with open('sim_scores.csv', 'w', newline='') as csvfile:
#     #     fieldnames = ['PatientIndex', 'SimilarityScore']
#     #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     #
#     #     # Write the header
#     #     writer.writeheader()
#     #
#     #     # Write the data
#     #     for patient_index, similarity_score in sim_scores:
#     #         writer.writerow({'PatientIndex': patient_index, 'SimilarityScore': similarity_score})
#
#     # Recommend treatments based on similar patients
#     recommendations = data[data['PatientID'].isin(patient_profiles.index[similar_patients])]
#     return recommendations
#
# # Example: Recommend treatments for a specific patient
# patient_id = '1A8791E3-A61C-455A-8DEE-763EB90C9B2C'
# treatment_recommendations = recommend_treatments(patient_id)
# print(treatment_recommendations)
