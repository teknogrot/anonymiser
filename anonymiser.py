#!/usr/bin/env python3
# anonymiser.py - anonymisation script for 

# imports block begins #
import os							# operating system functionality.
import sys, getopt					# system and parameters functionality.
import argparse                     # CLI argument parser.
import csv							# csv read/write functionality required for reading Amazon IP addresses.
import pandas						# import pandas
import time						 	# time functionality.
import datetime						# date functioanlity.
# imports block ends #

# global variable definition block begins #
maxArgs = 5							# temporary placeholder value for maximum number of args - replaced with argparse #
#TODO: calculate maximum number of args - replaced with argparse#
linesAnonymised = 0						# set the number of lines processed to zero.
columnList = ()							# an empty list to contain all the sourcefile columns.
subjectList = []						# an empty list of data subjects.
schemaList = []							# an empty list to store the schema definition.
loopControl = null						# loop control variable for replacements.
userResponse = null						# user response variable for file header verification.
hasHeaders = null						# header presence control variable.
headersCorrect = null						# header correctness control variable.
# global variable definition block ends #

# string variable definition block ends #
csvFileType = ".csv"
datFileType = ".dat"
excelFileType = ".xlsx"
checkString = "null"
# string variable definition block ends #

# filename variable definition block begins #
inputFile = None
schemaFile = None

# filename variable definition block ends #
# main function begins #
 
def main(argv):
	for opt, arg in opts:
		if opt in ('-h', '--help'):
      			usage()
      			sys.exit(2)
		elif opt in('-s'):
			schemaFile = sys.argv[indexOf -s + 1]
	elif (len(sys.argv)<2 OR len(sys.argv) > maxArgs):
		usage()
		sys.exit(1)
	elif (args.length() <3):
		## TODO: do check for flags - replace with argparse## 
		 
	inputFile = str(sys.argv[1])
	fileTypeCheck(inputFile, checkString)
	schemaBuild(inputFile, schemaFile, schemaList)
	dataSubjectLisBuild(inputFile, schemaList)
	anonymise(inputFile)
		
	sys.exit(0)
# main function ends #

# usage function begins #
def usage()
	print("Usage: python " + sys.argv[0] + " -f \"<filename>\" -s \"savedschema\"")
	print("Flags: 
	print("-f 		target file to anonymise. Requires quotation marks if contains a space.")
	print("-h, --help 	prints this message")
	print("-s 		[option] saved anonymisation schema file. Requires quotation marks if contains a space.")
	print("-o 		[option] output file name. Defaults to \"filename_anonymised\". Requires quotation marks if contains a space.")

# usage ends #

# function to check if file is CSV format  begins#
def csvCheck(inputFileNameIn)
	if inputFileNameIn.endswith(csvFileType).lower().strip():
			return true
	else:
		return false
# csvCheck ends #

# function to check if file is DAT format  begins#
def csvCheck(inputFileNameIn)
	if inputFileNameIn.endswith(datFileType).lower().strip():
			return true
	else:
		return false
# csvCheck ends #

# function to check if file is Excel format begins#
def excelCheck(inputFileNameIn)
	if inputFileNameIn.endswith(excelFileType).lower().strip():
		return true
	else:
		return false
# excelCheck ends #

# function to check if filetype is supported format begins#
def fileTypeCheck(inputFileNameIn, checkString)
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
def readFile(inputFileNameIn, checkString, fileReader)
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
			fileReader = csv.reader(excelFile:, delimiter=',')
			return fileReader
	else:
		print("Filetype unsupported. Please use supported filetype.")
		system.exit(3)
# fileTypeCheck ends #

#function to check if file headers exist begins #
def headerPresentCheck(inputFileNameIn, hasHeadersIn)
# ask user if file expects headers #
	while headers print("Does the target file have a header line? (Y/N): ").lower().strip()
		if userResponse == "y":
			hasHeadersIn = "true"
			return hasHeadersIn
		elif userResponse == "n":
			hasHeadersIn = "false"
			return hasHeadersIn
		except Exception as error:
        		print("Please enter only Y or N.")
        		print(error)
        		return headerPresentCheck(inputFileNameIn, hasHeadersIn)
# headerPresentCheck ends #

#function to check file headers are correct begins #
def headerCorrectCheck(inputFileNameIn, hasHeadersIn)
	# open file, read and print first line, close file #
	print("First line of file " + inputFileNameIn + ": ")
	with open(inputFileNameIn, 'r') as sourceFile:
		headerLine = sourceFile.readLine())
		print(headerLine)
	# ask user to confirm if headers are as expected or not. Exit on negative. Loop recursively on other input. #
	while userResponse 
		userResponse = input("Does the above contain the expected headers? (Y/N): ").lower().strip()
		try:
			if userResponse == "y":
				print("Headers correct. Continuing to column check.")
				return true
			elif userResponse == "n":
				print("Headers incorrect. Please verify input file is formatted as expected.")
				print("Exiting program.")
				sys.exit(5)
		except Exception as error:
        		print("Please enter only Y or N.")
        		print(error)
        		return headerCorrectCheck(inputFileNameIn, hasHeadersIn)
# headerCorrecCheck ends #

#function to check file headers begins#
def headerCheck(inputFileNameIn, hasHeadersIn)
	if headerPresentCheck(inputFileNameIn, hasHeadersIn):
		if headerCorrectCheck(inputFileNameIn, hasHeadersIn):
			print("Header and three sample lines from %S: ", %inputFileNameIn)
			with open(inputFileNameIn, 'r') as sourceFile:
				for i in range (4):
					sampleLine = sourceFile.readLine()
					print(sampleLine)
				testLine = sourcefile.readLine()
				columnsNumber = testLine.count(',') + 1
				columnCheck(columnsNumber)
	else:
		print("Four sample lines from %S: ", %inputFileNameIn)
		with open(inputFileNameIn, 'r') as sourceFile:
			for i in range (4):
				sampleLine = sourceFile.readLine())
				print(sampleLine)
			testLine = sourcefile.readLine()
			columnsNumber = testLine.count(',') + 1
			columnCheck(columnsNumber)
# headerCheck ends #

# function to evaluate columns begins #
def columnCheck(columnsNumberIn)
	while index > columnsNumberIn
		schemaList.add("I") 
	userResponse = 0
	while userResponse < 1 or userResponse >= columnsNumberIn
	userResponse = input("Please enter the number of values to anonymise: ")
		while i < userResponse:
			columnValue = input("Enter the index of the next element to anonymise (" + userResponse - i + " remaining): " )
			schemaList[i] = "A"
	userResponse = userResponse = input("Enter the number of values to draw from: ")
		while i < userResponse:
			columnValue = input("Enter the ranked index of the next source element (" + userResponse - i + " remaining): " )
			elementString = ("S%s" + %columnValue)
			schemaList[i] = elementString
# function to evaluate columns ends #

#function to build the anonymisation schema begins#
def schemaBuild(inputFileNameIn, schemaFileNameIn, schemaList)
	headerCheck(inputFileNameIn)
	
	if schemaFileName != None:
		writeSchema(schemaFileNameIn, schemaList)
# headerCheck ends #

# function to check file format of input file begins#
def writeSchema(schemaFileName, schemaList)
	with open("./schemas/%s.csv" %schemaFileName, "wb") as schemaOutputFile:
		schemaString = ",".join(schemaList)
		schemaOutputFile.write(schemaString)
# writeSchema ends #

# function to build list of data subjects begins #
def dataSubjectListBuild(inputFileIn, schemaListIn)
	inputFile.readLine()
	currentSubject = value at columnValueIn
	if (currentSubject is not in subjectList):
		subjectList.add(currentSubject)
# dataSubjectListBuild ends #

# function to run anonymisation begins #
def anonymise(fileIn)
	startTime = datetime.datetime.now()
	runTimeString = startTime.strftime("%Y%m%d%H%M%S")
	print("Anonymisation of " + inputFile + " started at: " + startTime.strftime("%H:%M:%S, %d/%m/%Y"))
	while (not EOF)
		currentLine = fileIn.readLine()
		currentLine.parseCSV()
		loopControl = None
			for (identifier in currentLine):
				if loopControl is not None
					for (replacement in tuple):
						if replacement is not None:
							element = replacement
							loopControl = "true"
							break
						if loopControl != "true"
						replacement = "subject" + subjectList.indexOf(replacement)
		linesAnonymised++

				
	completionTime = datetime.datetime.now()
	durationTaken = completionTime - startTime
	print("Anonymisation of " + inputFile + " completed at: " + completionTime.strftime("%H:%M:%S, %d/%m/%Y"))
	print("Total time taken: " durationTaken.strftime("%H:%M:%S, %d/%m/%Y")
	print("Number of lines anonymised: " + linesAnonymised)
# anonymise ends #

# run main #
if __name__ == "__main__":
    main(sys.argv[1:])
# main ends#
