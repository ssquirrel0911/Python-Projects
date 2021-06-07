#Samantha Squirrel
#samantha.squirrel001@albright.edu

#Assignment 20 Chapter 10 Programming Exercise 6; Patient Charges

import time

from SamanthaSquirrelAssignment20PatientClass import Patient
from SamanthaSquirrelAssignment20ProcedureClass import Procedure

def main():
    patient = makePatientList()
    procedure = makeProcedureList()

def makePatientList():
    #Creates empty list
    patientChart = []

    #Adds 3 Patient objects to the list
    #User will input data for all 3 patients
    for count in range(1, 4):
        #Get patient data
        print("Patient " + str(count) + ":")
        patientFullName = input("Enter the patient's full name: ")
        patientFullAddress = input("Enter the patient's full address: ")
        patientPhoneNumber = int(input("Enter patient's phone number: "))
        patientEmergencyContact = input("Enter patients emerhency contact with name/number: ")
        print()

        #Creates a new Patient object in memory
        #Assigns to patient variable
        patient = Patient(fullName, fullAddress, phoneNumber, emergencyContact)

        #Adds objects to the list
        patientChart.append(patient)

        #returns list
        return patientChart

def makeProcedureList(patient, ):
    #Creates empty list
    procedureChart = []

    #Adds the Procedures to the list
    #User will input for all 3 patients and procedures
    for count in range(1, 4):
        #Get procedure data
        print("Procedure " + str(count) + ":")
        procedureProcedureName = input("Enter the name of procedure: ") 
        procedureDateOfProcedure = input("Enter the patient's procedure date: ")
        procedurePractitioner = input("Enter the patient's practitioner: ")
        procedureCharge = float(input("Enter the cost of the procedure: $ "))

        #creates a new Procedure object in memory
        #Assigns procedure variable
        procedure = Procedure(procedureName, dateOfProcedure, practitioner, charge)

        #Adds objects to the list
        procedureChart.append(procedure)

        #returns list
        return procedureChart
        
#The display list function accepts a list containing all the objects as an argument
#and displays stored data    
def displayList(patientChart, procedureChart):
    for item in patientChart:
        print(item.getFullName())
        print(item.getFullAddress())
        print(item.getPhoneNumber())
        print(item.getEmergencyContact())
        print()

    for items in procedureChart:
        print(items.getProcedureName())
        print(items.getDateOfProcedureName())
        print(items.getPractitioner())
        print(items.getCharge())
        print()

main()
        
time.sleep(3)
