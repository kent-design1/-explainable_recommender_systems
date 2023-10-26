# -explainable_recommender_systems

This project was created using the [EMRBots](http://www.emrbots.org/) dataset to create an Explainable Recommender System capable recommending diagnosis to be looked out for, for patients based on their test results.

## File Description

Here you'll find a description of each file and the order of which to view them, as well as the order the system uses to serve its purpose

1. **README.md:** Hopefully self-explanatory

2. **Data:** contains the original txt files of the dataset and the csv version after conversion
   * *txtData* : Folder containing the original txt file from the dataset
   * *convert_txt_csv.py*: the file used to convert the txt data into csv
   * *csvData*: Contains the datasets after conversion to csv:
     * AdmissionsDiagnosesCorePopulatedTable.csv and LabsCorePopulatedTable.csv are the original txt files converted to csv
     * AdmissionsDiagnosesCorePopulatedTableEdited.csv is the AdmissionsDiagnosesCorePopulatedTable.csv without time (which was deemed irrelevant) that was created in dataManipulation.py
     * patient_for_recommendation.csv is the input, meaning it is the patient's data that we're using recommendations
     * finalDataset.csv is the combination of the two datasets that is created in dataManipulation.py and used to calculate the cosine similarity

3. **dataManipulation.py:** a python file that manipulates AdmissionsDiagnosesCorePopulatedTable.csv and creates AdmissionsDiagnosesCorePopulatedTableEdited.csv and finalDataset.csv
4. **main.py:** This is where the magic happens. finalDataset.csv is used together with patient_for_recommendation.csv to calculate cosine similarity and recommend diagnosis to be tested
5. **final_recommendation.csv:** Is where you'll find the final output