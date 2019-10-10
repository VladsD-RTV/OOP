#Program: Gibberish program that has the user enter data which will then scramble
#the word which will then be shown at the end of the game.
#Date:09/10/2019
#Author:VLads Drobovics
#Complier:OnlineGDB


#Global Variables Needed
Alphabet_Str = "*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#variables to check words
Vowels_Str = "aeiouAEIOU"#variables to check for volels

Constant = "y"#Variable used to control the while

while Constant == "y":
    WordEntered = input("Enter your first gibberish syllable (add * for the vowel substitute) :")
    WordEntered = inputchecker(GibberishWord) #Checking if the word matches
    
    GibberishWord = input("Enter your first gibberish syllable (add * for the vowel substitute) :")
    GibberishWord = inputcher(GibberishWord) #Checking if the word matches
    
    File_Name = input("please enter a file you want want to access: ")#Asking for the file name
    
    Text_Reader = File_Reader(File_Name)#Accessing the file and reading it
    
    New_text = ""
    Syllable = WordEntered
    PreviousConsonant = True
    
    for letter in text:
        if PreviousConsonant and letter in Vowels_Str:
            for Character in Syllable:
                if Character == "*":
                    New_text += letter #replacing the wildcard
                #end if
                else:
					New_text += character
			        New_text += letter
			        Syllable = GibberishWord 
			        PreviousConsonant = False
        else:
            New_text += letter
            PreviousConsonant = True
            if letter == " ":
            Syllable = WordEntered #reseting the WordEntered
            
        #end else
        
    
    #end for
    
    OutPut_File = NewFile_Name(File_Name)
	with open(outputfile, "w") as outputfile:
		outputfile.write(newtext)
	
	print("Your final text is:\n" + New_text)
	
	print("\nResults can be seen in file " + OutPut_File)
	
	Constant = input("Play again? (y/n) ")
	while Constant not in "yn":
		Constant= input("Please enter y to continue or n to quit: ")

print("\nThanks For Playing the Game")

#Other functions

#checking the in put so that it makes sure that user entered letters and not numbers
def inputchecker(word):
    while not alphabetchecker(word):
        word = input("This not a vailid input please input something that is a valid character")
    return word
    
#checking if the letters in word entered by the user are valid characters
def alphabetchecker(word):
	for letter in word:
		if letter not in Alphabet_Str:
			return False
	return True
	
#creating a function that reads a file and then lets you create a file read
def filereader(File_Name):
	while True:
		try:
			with open(File_Name, "r") as file:
				text = file.read()
		except FileNotFoundError:
			File_Name = input("Invalid file reading try again ")
		else:
			return text

#creating a function that will take the NewFile_Name convert the old file name and will return the old file with the
#gibberi word
def NewFile_Name(oldfilename):
	dotspot = -(oldfilename[::-1].find(".")+1) 
	return oldfilename[dotspot] + "Gibberish" + oldfilename[dotspot] 
    