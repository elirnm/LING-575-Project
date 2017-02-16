'''
Contains the top-level code for classifying a patient's histological grade.
Makes calls to other more specific programs; manages and outputs what they return.
'''

# USAGE: python3 main.py test_dir

import sys
import patient_splitter
import record

test_dir = sys.argv[1]

# call patient_splitter to get a list of patient records 
patients = patient_splitter.get_patients()

for patient in patients:
    # do whatever to classify the patient
    # python programs should preferably have a callable function which returns the data we need
    # non-python programs should print output to standard out and can be called from the command line with subprocess.check_output(["param1", "param2"], universal_newlines=True)
    # e.g. subprocess.check_output(["java", "MyProgram", "needed_directory"], universal_newlines=True)    

    # output classification to whatever format we're going to use