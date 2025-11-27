import sys

script_name = sys.argv[0]   

temp = float(sys.argv[1])

if temp < 15:
    result = "Cold"
elif 15 <= temp <= 30:
    result = "Normal"
else:
    result = "Hot"
print("Temperature (C):", temp)
print("Condition:", result)
