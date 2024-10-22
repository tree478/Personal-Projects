import math as m
import sys

#getting inputs & initializing support variables
# "og" as original & "samb"/"amb" as ambiguous side/angle
print("Type in your 3 knowns, while typing in 0 for your unknowns!")

sA = float(input("Side A: "))
ogsA = sA
sambA = sA
sB = float(input("Side B: "))
ogsB = sB
sambB = sB
sC = float(input("Side C: "))
ogsC = sC
sambC = sC
aA = float(input("Angle A: "))
ogaA = aA
ambA = aA
aB = float(input("Angle B: "))
ogaB = aB
ambB = 0
aC = float(input("Angle C: "))
ogaC = aC
ambC = 0
amby = False

# finds mathematical errors within inputs if present & figures out unknowns
def unknowns (sA,sB,sC,aA,aB,aC):
    vars = [sA,sB,sC,aA,aB,aC]
    unks = []
    anglesOnly = True
    count = 0
    if (aA + aB + aC > 180):
        print("Angles are too large")
        sys.exit()
    if (sA > sB + sC > 0 or sB > sA + sC > 0 or sC > sA + sB > 0):
        print("One side is too long")
        sys.exit()
    for i in range (3):
        if (vars [i] != 0):
            anglesOnly = False
    if (anglesOnly):
        print ("Side information needed")
        sys.exit()
    for i in range (6):
        val = vars[i]
        if (val == 0):
            count += 1
            unks.append (i)
        elif (val < 0):
            print ("One or more values are negative")
            sys.exit()
    if (count > 3):
        print ("More information is needed")
        sys.exit()
    elif(count < 3):
        print ("Too much information given")
        sys.exit()
    return unks

#finds an angle thru Law of Cosines
def cosAngle (side1,side2,side3):
    angle1 = round(m.degrees(m.acos(((side2 ** 2) + (side3 ** 2) - (side1 ** 2)) / (2 * side2 * side3))),4)
    return angle1

#finds a side thru Law of Cosines
def cosSide (angle1,side2,side3):
    side1 = round(((side2 ** 2 + side3 ** 2 - (2 * side2 * side3 * m.cos(m.radians(angle1)))) ** 0.5),4)
    return side1

#finds an angle thru Law of Sines
def sinAngle (side1,angle1,side2):
    angle2 = round(m.degrees(m.asin(m.sin(m.radians(angle1)) * side2 / side1)),4)
    return angle2

#finds a side thru Law of Sines
def sinSide (side1,angle1,angle2):
    side2 = round(m.sin(m.radians(angle2)) * side1 / m.sin(m.radians(angle1)),4)
    return side2

#figures out num of solutions of an ASS triangle
def ambiguity (side1,angle1,side2):
    if (m.sin(m.radians(angle1)) * side2 > side1):
        cond = 0
    elif (m.sin(m.radians(angle1)) * side2 == side1):
        cond = 1
    elif (m.sin(m.radians(angle1)) * side2 < side1):
        cond = 2
    return cond

#if/else chain to figure out known information & to solve for unknowns (including ambigiuous cases)
#lowercase: sides & uppercase: angles
if (sA != 0):
    if (sB != 0):
        if (sC != 0):
            #abc
            aA = cosAngle (sA,sB,sC)
            aB = cosAngle (sB,sC,sA)
            aC = round(180 - aA - aB,4)
        elif (aA != 0):
            #abA (ambiguous)
            amb = ambiguity (sA,aA,sB)
            if (amb == 0):
                print ("Triangle is not possible")
                sys.exit()
            elif (amb >= 1):
                aB = sinAngle (sA,aA,sB)
                aC = round(180 - aA - aB,4)
                sC = sinSide (sA,aA,aC)
                amby = False
                if (amb == 2):
                    ambB = round(180 - aB,4)
                    ambC = round(180 - aA - ambB,4)
                    sambC = sinSide (sA,aA,aC)
                    if (ambC > 0):
                        amby = True
        elif (aB != 0):
            #abB (ambiguous)
            amb = ambiguity (sB,aB,sA)
            if (amb == 0):
                print ("Triangle is not possible")
                sys.exit()
            elif (amb >= 1):
                aA = sinAngle (sB,aB,sA)
                aC = round(180 - aA - aB,4)
                sC = sinSide (sB,aB,aC)
                amby = False
                if (amb == 2):
                    ambA = round(180 - aA,4)
                    ambC = round(180 - ambA - aB,4)
                    sambC = sinSide (sB,aB,aC)
                    if (ambC > 0):
                        amby = True       
        elif (aC != 0):
            #abC
            sC = cosSide (aC,sA,sB)
            aA = sinAngle (sC,aC,sA)
            aB = round(180 - aA - aC,4)
    elif (sC != 0):
        if (aA != 0):
            #acA (ambiguous)\
            amb = ambiguity (sA,aA,sC)
            if (amb == 0):
                print ("Triangle is not possible")
                sys.exit()
            elif (amb >= 1):
                aC = sinAngle (sA,aA,sC)
                aB = round(180 - aA - aC,4)
                sB = sinSide (sA,aA,aB)
                amby = False
                if (amb == 2):
                    ambC = round(180 - aC,4)
                    ambB = round(180 - aA - ambC,4)
                    sambB = sinSide (sA,aA,aB)
                    if (ambB > 0):
                        amby = True          
        elif (aB != 0):
            #acB
            sB = cosSide (aB,sA,sC)
            aA = cosAngle (sA,sB,sC)
            aC = round(180 - aA - aB,4) 
        elif (aC != 0):
            #acC (ambiguous)
            amb = ambiguity (sC,aC,sA)
            if (amb == 0):
                print ("Triangle is not possible")
                sys.exit()
            elif (amb >= 1):
                aA = sinAngle (sC,aC,sA)
                aB = round(180 - aA - aC,4)
                sB = sinSide (sC,aC,aB)
                amby = False
                if (amb == 2):
                    ambA = round(180 - aA,4)
                    ambB = round(180 - ambA - aC,4)
                    sambB = sinSide (sC,aC,aB)
                    if (ambB > 0):
                        amby = True        
    elif (aA != 0):
        if (aB != 0):
            #aAB
            sB = sinSide (sA,aA,aB)
            aC = round(180 - aA - aB,4)
            sC = sinSide (sA,aA,aC)
        elif (aC != 0):
            #aAC
            aB = round(180 - aA - aC,4)
            sB = sinSide (sA,aA,aB)
            sC = sinSide (sA,aA,aC)
    elif (aB != 0):
        if (aC != 0):
            #aBC
            aA = round(180 - aB - aC,4)
            sB = sinSide (sA,aA,aB)
            sC = sinSide (sA,aA,aC)

elif (sB != 0):
    if (sC != 0):
        if (aA != 0):
            #bcA
            sA = cosSide (aA,sB,sC)
            aB = cosAngle (sB,sA,sC)
            aC = round(180 - aA - aB,4)            
        elif (aB != 0):
            #bcB (ambiguous)
            amb = ambiguity (sB,aB,sC)
            if (amb == 0):
                print ("Triangle is not possible")
                sys.exit()
            elif (amb >= 1):
                aC = sinAngle (sB,aB,sC)
                aA = round(180 - aB - aC,4)
                sA = sinSide (sB,aB,aA)
                amby = False
                if (amb == 2):
                    ambC = round(180 - aC,4)
                    ambA = round(180 - aB - aC,4)
                    sambA = sinSide (sB,aB,aA)
                    if (ambA > 0):
                        amby = True
        elif (aC != 0):
            #bcC (ambiguous)
            amb = ambiguity (sC,aC,sB)
            if (amb == 0):
                print ("Triangle is not possible")
                sys.exit()
            elif (amb >= 1):
                aB = sinAngle (sC,aC,sB)
                aA = round(180 - sB - sC,4)
                sA = sinSide (sC,aC,aA)
                amby = False
                if (amb == 2):
                    ambB = round(180 - aB,4)
                    ambA = round(180 - sB - sC,4)
                    sambA = sinSide (sC,aC,aA)
                    if (ambA > 0):
                        amby = True
    elif (aA != 0):
        if (aB != 0):
            #bAB
            aC = round(180 - aA - aB,4)
            sA = sinSide (sB,aB,aA)
            sC = sinSide (sB,aB,aC)
        elif (aC != 0):
            #bAC
            aB = round(180 - aA - aC,4)
            sA = sinAngle (sB,aB,aA)
            sC = sinSide (sB,aB,aC)
    elif (aB != 0):
        if (aC != 0):
            #bBC
            aA =round(180 - aB - aC,4)
            sA = sinSide (sB,aB,aA)
            sC = sinSide (sB,aB,aC)
elif (sC != 0):
    if (aA != 0):
        if (aB != 0):
            #cAB
            aC = round(180 - aA - aB,4)
            sA = sinSide (sC,aC,aA)
            sB = sinSide(sC,aC,aB)
        elif (aC != 0):
            #cAC
            aB = round(180 - aA - aC,4)
            sA = sinSide(sC,aC,aA)
            sB = sinSide (sC,aC,aB)
    elif (aB != 0):
        if (aC != 0):
            #cBC
            aA = round(180 - aB - aC,4)
            sA = sinSide (sC,aC,aA)
            sB = sinSide(sC,aC,aB)

#lists for measurements and names to be accessed
vars = [sA,sB,sC,aA,aB,aC]
ambVars = [sambA,sambB,sambC,ambA,ambB,ambC]
varNames = ["Side A:","Side B:","Side C:","Angle A:","Angle B:","Angle C:"]
unks = unknowns (ogsA,ogsB,ogsC,ogaA,ogaB,ogaC)

#printing previously unknown measurements
print ("\n")
print("Answers:")
for i in range (3):
    print(varNames [unks [i]],vars [unks [i]])

if (amby):
    print("OR")
    for i in range (3):
        print(varNames [unks [i]],ambVars [unks [i]])