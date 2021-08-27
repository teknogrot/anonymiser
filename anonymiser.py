#!/usr/bin/env python3
# anonymiser.py - anonymisation script for 

# imports block begins #
import os                             # operating system functionality.
import sys, getopt                    # system and parameters functionality.
import argparse                       # CLI argument parser.
import csv                            # csv read/write functionality required for reading Amazon IP addresses.
import pandas                         # import pandas
import time                           # time functionality.
import datetime                       # date functioanlity.
# imports block ends #

# global variable definition block begins #
linesAnonymised = 0                   # set the number of lines processed to zero.
columnList = ()                       # an empty list to contain all the sourcefile columns.
schemaList = []                       # an empty list to store the schema definition.
loopControl = None                    # loop control variable for replacements.
userResponse = None                   # user response variable for file header verification.
hasHeaders = None                     # header presence control variable.
headersCorrect = None                 # header correctness control variable.
# global variable definition block ends #

# string variable definition block ends #
csvFileType = ".csv"
datFileType = ".dat"
excelFileType = ".xlsx"
checkString = None
# string variable definition block ends #

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
    
    #fileTypeCheck(args.inputFile.lower().strip(), checkString)
    schemaBuild(args.inputFile, schemaFile, schemaList, len(headerList))
    subjectList = dataSubjectListBuild(args.inputFile, schemaList, len(headerList))
    print("Subjects: " + str(subjectList))
    
    #anonymise(inputFile)
        
# main function ends #

# function to check if file is CSV format  begins#
def csvCheck(inputFileNameIn):
    if inputFileNameIn.endswith(csvFileType):
            return True
    else:
        return False
# csvCheck ends #

# function to check if file is DAT format  begins#
def datCheck(inputFileNameIn):
    if inputFileNameIn.endswith(datFileType):
            return True
    else:
        return False
# csvCheck ends #

# function to check if file is Excel format begins#
def excelCheck(inputFileNameIn):
    if inputFileNameIn.endswith(excelFileType):
        return True
    else:
        return False
# excelCheck ends #

# function to check if filetype is supported format begins#
def fileTypeCheck(inputFileNameIn, checkString):
    if datCheck(inputFileNameIn):
        checkString = "dat"
        return checkString
    elif csvCheck(inputFileNameIn):
        checkString = "csv"
        return checkString
    elif excelCheck(inputFileNameIn):
        checkString = "excel"
        return checkString
    else:
        checkString = "error"
        return checkString
# fileTypeCheck ends #

# function read in file begins#
def readFile(inputFileNameIn, checkString, fileReader):
    if checkString =="dat":
        with open(inputFileNameIn) as datFile:
            fileReader = csv.reader(datFile, delimiter=',')
            return fileReader        
    elif checkString == "csv":
        with open(inputFileNameIn) as csvFile:
            fileReader = csv.reader(csvFile, delimiter=',')
            return fileReader        
    elif checkstring == "excel":
        with open(inputFileNameIn) as excelFile:
            fileReader = csv.reader(excelFile, delimiter=',')
            return fileReader
    else:
        print("Filetype unsupported. Please use supported filetype.")
        sys.exit(3)
# fileTypeCheck ends #

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
            print("Headers correct. Continuing to column check.")
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
        print("No headers present. Continuing to column check.")
        print("Four sample lines from %s: " %inputFileNameIn)
        with open(inputFileNameIn, 'r') as sourceFile:
            for i in range (4):
                sampleLine = next(sourceFile)
                print(sampleLine)
            testLine = next(sourceFile)
            columnsNumber = testLine.count(',') + 1
            return False
# headerCheck ends #

# function to grab headers and parse to list begins #
def headerGrab(inputFileNameIn):
    with open(inputFileNameIn) as csvFile:
        sourceFile = csv.reader(csvFile, delimiter=',')
        headerList = next(sourceFile)
        return headerList
# headerGrab ends #

# function to evaluate columns begins #
def columnCheck(columnsNumberIn):
    while index > columnsNumberIn:
        schemaList.add("I")
    userResponse = 0
    while userResponse < 1 or userResponse >= columnsNumberIn:
        userResponse = input("Please enter the number of values to anonymise: ")
        while i < userResponse:
            columnValue = input("Enter the index of the next element to anonymise (" + userResponse - i + " remaining): " )
            schemaList[i] = "A"
    userResponse = userResponse = input("Enter the number of values to draw from: ")
    while i < userResponse:
        columnValue = input("Enter the ranked index of the next source element (" + userResponse - i + " remaining): " )
        elementString = ("S%s" %columnValue)
        schemaList[i] = elementString
# function to evaluate columns ends #

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

# function to strip un-used columns begins #
def columnStrip(inputFileIn, delimiterIn, columnsListIn):
    for line in inputFile.splitlines():
        currentLine
        subjectList.update({currentLine.strip().lower() for subject in subjects.split(delimiterIn)})
    return columnList
# columnStrip ends #

# function to build list of data subjects begins #
def dataSubjectListBuild(inputFileIn, schemaListIn, headerLength):
    subjectList = set()
    with open(inputFileIn, 'r') as sourceFile:
        lines = sourceFile.readlines()
    for line in lines:
        subjectList.update({line.strip().lower() for subject in line.split(",")})
    return subjectList
# dataSubjectListBuild ends #

# function to run anonymisation begins #
#def anonymise(fileIn):
 #   startTime = datetime.datetime.now()
  #  runTimeString = startTime.strftime("%Y%m%d%H%M%S")
   # print("Anonymisation of " + inputFile + " started at: " + startTime.strftime("%H:%M:%S, %d/%m/%Y"))
    #while (not EOF):
     #   currentLine = fileIn.readLine()
      #  currentLine.parseCSV()
       # loopControl = None
        #for (identifier in currentLine):
         #  if loopControl is not None
          #      for (replacement in tuple):
           #         if replacement is not None:
            #            element = replacement
             #           loopControl = "True"
              #          break
               #     if loopControl != "True"
                #    replacement = "subject" + subjectList.indexOf(replacement)
#        linesAnonymised+=1
 #   completionTime = datetime.datetime.now()
  #  durationTaken = completionTime - startTime
#    print("Anonymisation of " + inputFile + " completed at: " + completionTime.strftime("%H:%M:%S, %d/%m/%Y"))
 #   print("Total time taken: " durationTaken.strftime("%H:%M:%S, %d/%m/%Y")
  #  print("Number of lines anonymised: " + linesAnonymised)
# anonymise ends #

# run main #
if __name__ == "__main__":
    main(sys.argv[1:])
# main ends#
