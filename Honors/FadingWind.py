import math

startHeight, fixedFactor, startingVelocity, windStrength = map(int, input().split())

distance = 0
while startHeight > 0:
    startingVelocity += windStrength 
    startingVelocity -= max(1, math.floor(startingVelocity/10))
    if startingVelocity >= fixedFactor:
        startHeight += 1
    elif startingVelocity > 0 and startingVelocity < fixedFactor:
        startHeight -= 1
        if startHeight == 0:
            startingVelocity = 0
    if startingVelocity <= 0:
        startHeight = 0
        startingVelocity = 0
    if windStrength > 0:
        windStrength -= 1

    distance += startingVelocity

print(distance)
