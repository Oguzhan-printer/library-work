def greetings(name):
    return ("Hello" + name)

greetings("Oguzhan")

def difference(number1, number2):
    differ = number1 - number2
    return differ

difference(14.99, 12.49)


birthday = "4 September 1996"
place_of_birth = "London"
current_city = "London"

def print_introduction(birthday, place_of_birth, current_city):
    print("I was born on " + birthday + " in " + place_of_birth + " and now I live in " + current_city + ".")

print_introduction(birthday, place_of_birth, current_city)

#Write a function to change the current_city 
def change_current_city(new_city):
  global current_city
  current_city = new_city

#Change current_city to "New York"
change_current_city("New York")

#Call the introduction function 
print_introduction(birthday, place_of_birth, current_city)


#We need to import the seaborn library
import seaborn as sns
#Weather data 
day = [1, 2, 3, 4, 5, 6, 7]
avg_temperature = [14,9,3,11,18,27,6]

#Create a bar plot for the given data
sns.barplot(x = day, y = avg_temperature)

import math

#DISTANCE WORK

def mile2km(miles):
  #Write a function to convert miles to kilometers 
  km = miles * 1.60934
  return km

def km2mile(km):
  #Write a function to convert kilometers to miles
  miles = km / 1.60934
  return miles

assert math.isclose(mile2km(132.2), 212.754748, abs_tol=1e-5), "Test failed for mile2km!"
assert math.isclose(km2mile(48.44), 30.099295, abs_tol=1e-5), "Test failed for km2mile!"
print("Test passed!")

#Call the mile2km function to convert 12 miles
mile2km(12)

#MASS WORK

def pound_kilogram(quantity, mode):
  assert mode == "pound2kg" or mode == "kg2pound", "Invalid argument!"
  #Here the assert command ensures that a valid mode is given as argument.
  
  if mode == "pound2kg":
    #write a statement to convert pound to kilogram for mode "pound2kg"
    conv_quan = quantity * 0.45359

    #Else it should convert kilogram to pound
  else:
    conv_quan = quantity / 0.45359
  return conv_quan

#Test the function
assert math.isclose(pound_kilogram(2.20462, "pound2kg"), 1, abs_tol=1e-5), "Test failed for mode \"pound2kg\"!"
assert math.isclose(pound_kilogram(43, "kg2pound"), 94.79926, abs_tol=1e-5), "Test failed for mode \"kg2pound\"!"
print("Test passed!")

#Call the function to convert 2 kilograms to pound
pound_kilogram(2, "kg2pound")

#DEGREE WORK

def fahrenheit_celcius(temperature, mode):
  assert mode == "f2c" or mode == "c2f", "Invalid argument!"
  # Write a statement to convert Fahrenheit to Celsius or Celsius to Fahrenheit
  if mode == "f2c":
    conv_temp = (temperature - 32) * 5/9
  else:
    conv_temp = (temperature * 9/5) + 32
  return conv_temp


assert math.isclose(fahrenheit_celcius(98.6, "f2c"), 37.0, abs_tol=1e-5), "Test failed for mode \"f2c\"!"
assert math.isclose(fahrenheit_celcius(42, "c2f"), 107.6, abs_tol=1e-5), "Test failed for mode \"c2f\"!"
print("Test passed!")

#Call the function to convert 88° Fahrenheit to Celsius
fahrenheit_celcius(88, "f2c")