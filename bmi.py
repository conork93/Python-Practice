#Conor Kennedy
#8/13/2017

#calculate bmi 

height = input("Enter height in meters: ")
weight = input("Enter weight in kg: ")

bmi = (weight)/(height * height)

print("BMI: ")+("%.1f" % bmi)


#calculate bmi with pounds and inches
def mericaUnits(height, weight):
  return (weight/(height * height)) * 703


def feetToInches(feet):
  return feet * 12


#calculate bmi with meters and kg
def restOfTheWorld(height, weight):
  return (weight)/(height * height)

