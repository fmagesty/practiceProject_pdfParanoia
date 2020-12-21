# Go trough every PDF in a folder and its subfolders (os.walk function);
# Encrypt the PDFs using a password provided on the command line;
# Save each encrypted PDF with an _encrypted.pdf suffix added to the original file;
# Before deleting the file: program must read and decrypt the file to ensure it was encrypted correctly.
# Finds all encrypted PDFs in a folder/subfolders and creates a decrypted copy of the PDF using a provided password;
# If the password is incorrect, the program should print a message to the user and continue to the next PDF.
# Example command line: py practiceProject_pdfParanoia password

import os, sys, PyPDF2, time

# Get the password from command line:
password = str(sys.argv[-1])
# password = 'password'

# Check the folder/subfolders for PDF files:
for i in os.walk('C:\\Users\\Felipe'):
    for x in i:
        for file in x:
            if file.endswith('.pdf'):
                # Get the file:
                pdfFile = open(str(file), 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                
                # Add encryption using the password passed to command line:
                print('Encrypting  ' + file + '...')
                pdfWriter.encrypt(password)
                
                # Save each encrypted PDF with the suffix '_encrypted.pdf':
                resultPdf = open(str(file)[:-4] + '_encrypted.pdf', 'wb')
                pdfWriter.write(resultPdf)
                pdfFile.close()
                resultPdf.close()

                # Read and decrypt the file to ensure it was encrypted correctly:
                checkEncripted = PyPDF2.PdfFileReader(open(resultPdf.name, 'rb'))
                checkEncripted.decrypt('password')
                if checkEncripted.getPage(0):
                    print('Deleting %s.' % (file)
                # Find encrypted PDFs in folder/subfolder and create decrypted copy:
                    os.unlink(file)
                # If password is incorrect, print a message to the user and continue.
                else:
                    print('Password is incorrect.')
print('Done.')
time.sleep(5) # just a pause so that the user can read the console.