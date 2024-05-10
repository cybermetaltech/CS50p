# einstein

# ask the user an int (mass in kilograms)
# outputs the equivalent number of joules as an int

mass = int(input())
lightspeed = 300000000

energy = mass * lightspeed ** 2

print(energy)