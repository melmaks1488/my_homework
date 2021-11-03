input_filename = "fizzbuzz.txt"
output_filename = "outfizzbuzz.txt"

def fizzbuzz(num1, num2, d):
    for x in (range(1, d + 1)):
        if x % num1 == 0 and x % num2 == 0:
            file_fb_output.write(" FB ")
        elif x % num1 == 0:
            file_fb_output.write(" B ")
        elif x % num2 == 0:
            file_fb_output.write(" F ")
        else:
            file_fb_output.write(f" {x} ")
    file_fb_output.write("\n")
    return file_fb_input

with open(input_filename, "r") as file_fb_input:
    with open(output_filename, "w") as file_fb_output:
        for line in file_fb_input:
            fizz, buzz, c = map(int, line.split())

            fizzbuzz(fizz,buzz,c)
