def converter(convertFrom, convertTo, system, value):
    if system == "temperature":
        try:
            if convertFrom == "kelvin" and convertTo == "celsius":
                celsius = value + -273.15
                return celsius
            
            elif convertFrom == "celsius" and convertTo == "kelvin":
                kelvin = value + 273.15
                return kelvin

            elif convertFrom == "celsius" and convertTo == "fahrenheit":
                fahrenheit = (value * 9/5) + 32
                return fahrenheit

            elif convertFrom == "fahrenheit" and convertTo == "celsius":
                celsius = (value-32) * 5/9
                return celsius

            elif convertFrom == "celsius" and convertTo == "rankine":
                rankine = (value + 273.15) * 9/5
                return rankine

            elif convertFrom == "rankine" and convertTo == "celsius":
                rankine = (value - 491.67) * 5/9
                return celsius

            elif convertFrom == "celsius" and convertTo == "delisle":
                delisle = (100-value) * 3/2
                return delisle

            elif convertFrom == "delisle" and convertTo == "celsius":
                celsius = (100-value) * 2/3
                return celsius

            else:
                tocelsius = converter(convertFrom, "celsius", system, value)
                tofinal = converter("celsius", convertTo, system, value)
                return tofinal

        except: 
            print("The input is invalid")

value = float(input("Enter a value"))
convertFrom = input("What are you converting from? (lowerspace): ")
convertTo = input("What are you converting to? (lowerspace): ")
system = input("What measurement system? (lowerspace): ")

converted = converter(convertFrom, convertTo, system, value)

print("The converted value in " + str(convertTo) + " is " + str(converted))