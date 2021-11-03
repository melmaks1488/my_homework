input_filename = "fizzbuzz.txt"
output_filename = "new_fizzbuzz.txt"

file_for_input = open(input_filename, "r")
file_for_output = open(output_filename, "w")
for line in file_for_input:
    fizz, buzz, c = line.split()
    fizz = int(fizz)
    buzz = int(buzz)
    c = int(c)

    for x in (range(1, c + 1)):
        if x % fizz == 0 and x % buzz == 0:
            file_for_output.write(' FB ')
        elif x % fizz == 0:
            file_for_output.write(" B ")
        elif x % buzz == 0:
            file_for_output.write(" F ")
        else:
            file_for_output.write(" " + str(x) + " ")
    file_for_output.write("\n")

file_for_input.close()
file_for_output.close()
