from math import pi as uwu
# Radius=eval(input("Enter The Value of Radius(in Meters): ")) 
# if Radius>=100:
#     volume=4/3*uwu *pow(Radius,3)       //////Without  Function
#     print(volume)
# else:
#     print("Invalid Input")
def volume(Radius):
    
    if Radius>=100:
        volume=2/3*uwu *pow(Radius,3)
        return volume              # ////with function
    else:
        return("Invalid Input")

print(volume(Radius=eval(input("Enter The Value of Radius(in Meters): "))))