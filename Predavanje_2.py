# Pretvornik

print("Dobrodošli v pretvornik.")

while True:

    km = int(input("Vnesi vrednost za kilometer: "))

    mi = km * 0.621371

    print("Vnešena vrednost za miljo: ", mi)

    choice = input("Želite vnesti novo vrednost (da/ne): ")

    if choice.lower() != "da":
        break

print("Hvala")


# Fizzbuzz

print("Fizzbuzz igra!")

end = input("Vnesi številko med 1 in 100: ")
end = int(end)  # convert string into number

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)


# Make string lowercase

s = "Today Is A BeautiFul DAY"
print(s.lower()) 
