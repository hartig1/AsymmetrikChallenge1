clone the repo or download and unzip to a folder
requires names.csv to be in the directory
main.py contains a driver that uses the examples from the webpage
Written using python 2.7
To use your own test files 'import BusinessCardOCR'
create a card with 'x = BusinessCardOCR.ContactInfo(y)' where x is the resulting object, and y is the string from OCR
function available to that object:
  getName()
  getPhoneNumber
  getEmailAddress()
  getOCR() -- the original string
  setContactInfo() -- user doesn't need to call this, it is called in initialization
  setName() -- called by setContactInfo
  setPhoneNumber() -- called by setContactInfo -- these can call the correct____() functions below if they can't figure out the right value
  setEmailAddress() -- called by setContactInfo
  correctName()
  correctNumber() -- these 3 can be used so the user can fix any of the values, in case they are incorrect
  correctEmail()
  printInfo() -- prints all 3 output values
  fullPrint() -- prints in the form of the example
For your own driver the only lines you need are:
  x = BusinessCardOCR.ContactInfo(input)
  x.fullPrint()
for each input you want to test
