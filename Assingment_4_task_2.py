file2 = open('output.txt','a')
appending_user = input("Enter text to write to the files: \n")
print('data successfully written to output.txt.\n')
file2.write(appending_user + "\n")

appending_user = input("enter additional text to append: \n")
file2.write(appending_user + "\n")
print("Data successfully appended.\n")
file2.close()

file2 = open('output.txt','r')
print("Final content of the output.txt: \n" + file2.read())
file2.close()

