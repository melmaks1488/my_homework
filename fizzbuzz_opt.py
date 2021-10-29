input_filename = "fizzbuzz.txt"
output_filename = "outfizzbuzz.txt"

with open(input_filename, "r") as file_fb_input:
    with open(output_filename, "w") as file_fb_output:
        for line in file_fb_input:

            fizz, buzz, c = list(map(int, line.split()))

            for x in (range(1, c + 1)):
                if x % fizz == 0 and x % buzz == 0:
                    file_fb_output.write(' FB ')
                elif x % fizz == 0:
                    file_fb_output.write(" B ")
                elif x % buzz == 0:
                    file_fb_output.write(" F ")
                else:
                    file_fb_output.write(" " + str(x) + " ")
            file_fb_output.write("\n")

file_fb_input.close()
file_fb_output.close()
