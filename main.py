import BusinessCardOCR
def main():
    #the following are the examples from the prompt
    mikesCardStr = "ASYMMETRIK LTD\nMike Smith\nSenior Software Engineer\n(410)555-1234\nmsmith@asymmetrik.com\n"
    mikesCard = BusinessCardOCR.ContactInfo(mikesCardStr)
    mikesCard.fullPrint()
    lisasCardStr = "Foobar Technologies\nAnalytic Developer\nLisa Haung\n1234 Sentry Road\nColumbia, MD 12345\nPhone: 410-555-1234\nFax: 410-555-4321\nlisa.haung@foobartech.com\n"
    lisasCard = BusinessCardOCR.ContactInfo(lisasCardStr)
    lisasCard.fullPrint()
    arthursCardStr = "Arthur Wilson\nSoftware Engineer\nDecision & Security Technologies\nABC Technologies\n123 North 11th Street\nSuite 229\nArlington, VA 22209\nTel: +1 (703) 555-1259\nFax: +1 (703) 555-1200\nawilson@abctech.com"
    arthursCard = BusinessCardOCR.ContactInfo(arthursCardStr)
    arthursCard.fullPrint()

    #the following is an example of when the system can't figure out the name field
    #it will display all lines and ask the using to chose the line with the name on it
    #uncomment the next 3 line to see example
    # ryansCardStr = "ryab\n443-619-3260\nhartig1@umbc.edu\n"
    # ryansCard = BusinessCardOCR.ContactInfo(ryansCardStr)
    # ryansCard.printInfo()
if __name__ == "__main__":
    main()
