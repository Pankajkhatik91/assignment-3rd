from logging import exception

try:
    file1 = open ('simple.txt', 'r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("The file 'simple.txt' does not found.")
finally:
    print("Task Ends Here\n" + "Thank You!!")


