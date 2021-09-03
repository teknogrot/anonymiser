#!/usr/bin/env python3
# anonymiser.py - anonymisation script for 

# imports block begins #
import os                             # operating system functionality.
import sys, getopt                    # system and parameters functionality.
import argparse                       # CLI argument parser.
import csv                            # csv read/write functionality required for reading Amazon IP addresses.
import datetime                       # date functioanlity.
# imports block ends #

# global variable definition block begins #
schemaList = [27, 28]                 # an empty list to store the schema definition.
userResponse = None                   # user response variable for file header verification.
# global variable definition block ends #

# filename variable definition block begins #
inputFile = None
schemaFile = None
# filename variable definition block ends #

# main function begins #
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="target file to anonymise. Requires quotation marks if contains a space.", dest="inputFile", required=True)
    parser.add_argument("-s", help="saved anonymisation schema file. Requires quotation marks if contains a space.", dest="schemaFile")
    parser.add_argument("-o", help="output file name. Defaults to \"\filename_anonymised\". Requires quotation marks if contains a space.", dest="outputFile")
    args = parser.parse_args(argv)
    
    if headerCheck(args.inputFile):
        headerList = headerGrab(args.inputFile)
        print(headerList)
        print("Number of columns: " + str(len(headerList)))
        checkBox = True
    else:
        checkBox = False
    #schemaBuild(args.inputFile, schemaFile, schemaList, len(headerList))
    subjectList = dataSubjectListBuild(args.inputFile, schemaList, checkBox)
    print("Subjects: " + str(subjectList))
    anonymise(args.inputFile, subjectList)    
# main function ends #

# function to provide passed input prompt text and return true or false begins #
def yesNoPrompt(promptIn):
    while True:
        userResponse = input(promptIn).lower().strip()
        if userResponse.startswith("y"):
            return True
        elif userResponse.startswith("n"):
            return False
        else:
            print("Please enter only Y or N.")
# yesNoPrompt ends #

#function to check file headers begins#
def headerCheck(inputFileNameIn):
    if yesNoPrompt("Does the target file have a header line? (Y/N): "):
        # open file, read and print first line, close file #
        print("First line of file %s: " %inputFileNameIn)
        with open(str(inputFileNameIn), 'r') as sourceFile:
            headerLine = next(sourceFile)
            print(headerLine)
        # ask user to confirm if headers are as expected or not. Exit on negative. Loop recursively on other input. #
        if yesNoPrompt("Does the above contain the expected headers? (Y/N): "):
            print("Headers correct.")
            print("Header and three sample lines from %s: " %inputFileNameIn)
            with open(inputFileNameIn, 'r') as sourceFile:
                for i in range (4):
                    sampleLine = next(sourceFile)
                    print(sampleLine)
                testLine = next(sourceFile)
                columnsNumber = testLine.count(',') + 1
                return True
        else:
            print("Headers incorrect. Please verify input file is formatted as expected.")
            print("Exiting program.")
            sys.exit(5)
    else:
        print("No headers present.")
        print("Four sample lines from %s: " %inputFileNameIn)
        with open(inputFileNameIn, 'r') as sourceFile:
            for i in range (4):
                sampleLine = next(sourceFile)
                print(sampleLine)
            testLine = next(sourceFile)
            columnsNumber = testLine.count(',') + 1
            return False
# headerCheck ends #

def headerGrab(inputFileNameIn):
    with open(inputFileNameIn) as csvFile:
        sourceFile = csv.reader(csvFile, delimiter=',')
        headerList = next(sourceFile)
        return headerList
# headerGrab ends #

#function to build the anonymisation schema begins#
def schemaBuild(inputFileNameIn, schemaFileNameIn, schemaList, headerLength):
    if schemaFileNameIn != None:
        with open("./schemas/%s.csv" %schemaFileName, "wb") as schemaOutputFile:
            schemaString = ",".join(schemaList)
            schemaOutputFile.write(schemaString)
            print("Saved anonymisation schema to: ./schemas/%s.csv" %schemaFileName, "wb")
    else:
        print("Not saving anonymisation schema.")
# schemaBuild ends #

# function to build list of data subjects begins #
def dataSubjectListBuild(inputFileIn, schemaListIn, checkBox):
    subjectList = set()
    with open(inputFileIn, 'r') as sourceFile:
        csvReader = csv.reader(sourceFile)
        if checkBox:
            next(csvReader)
        for line in csvReader:
            for value in schemaListIn:
                subjectList.update([entry.strip() for entry in line[value].split(';') if entry.strip()])
    anonymisedSubjects = {}
    for position, subject in enumerate(subjectList):
        if subject.strip():
            anonymisedSubjects[subject] = "Subject{}".format(position)
    return anonymisedSubjects
# dataSubjectListBuild ends #

# function to run anonymisation begins #
def anonymise(inputFileIn, subjectListIn):
    startTime = datetime.datetime.now()
    runTimeString = startTime.strftime("%Y%m%d%H%M%S")
    print("Anonymisation of " + inputFileIn + " started at: " + startTime.strftime("%H:%M:%S, %d/%m/%Y"))
    with open(inputFileIn, 'r') as sourceFile:
        sourceFileContents = sourceFile.read()
        for subject, anonymisedSubject in subjectListIn.items():
                sourceFileContents = sourceFileContents.replace(subject, anonymisedSubject)
    outputFileName = os.path.splitext(inputFileIn)[0] + "_output.csv"
    with open(outputFileName, 'wb') as outputFile:
        outputFile.write(sourceFileContents.encode('utf-8'))

    completionTime = datetime.datetime.now()
    durationTaken = completionTime - startTime
    subjectCount = len(subjectListIn)
    print("Anonymisation of " + inputFileIn + " completed at: " + completionTime.strftime("%H:%M:%S, %d/%m/%Y"))
    print("Total number of data subjects: " + str(subjectCount))
    
    print("Total time taken: " + str((durationTaken.microseconds)) + " microseconds.")
    print("Calculate subjects time here whatever")
# anonymise ends #

# run main #
if __name__ == "__main__":
    main(sys.argv[1:])
# main ends#
