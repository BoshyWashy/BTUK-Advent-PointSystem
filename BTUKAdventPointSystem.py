import os
import math

BASE_POINTS = 10

def calculatePoints(evaluationQuery):

    # size
    if evaluationQuery == "building":
        size_medium_minimum = 175.0
        size_large_minimum = 350.0
        floors = int(input("Enter number of floors."))
        area = int(input("Enter polygon area from google earth pro."))
        floors = math.sqrt(floors)
        size = floors * area
        if size < size_medium_minimum:
            base_score_size = 0 # small
        elif size >= size_medium_minimum and size < size_large_minimum:
            base_score_size = 2 # medium
        else:
            base_score_size = 4 # large
    elif evaluationQuery == "park":
        size_medium_minimum = 1000
        size_large_minimum = 2500
        area = int(input("Enter polygon area from google earth pro."))
        if area < size_medium_minimum:
            base_score_size = 0 # small
        elif area >= size_medium_minimum and area < size_large_minimum:
            base_score_size = 2 # medium
        else:
            base_score_size = 4 # large
    elif evaluationQuery == "road":
            size_medium_minimum = 4000
            size_large_minimum = 8000
            area = int(input("Enter polygon area from google earth pro."))
            if area < size_medium_minimum:
                base_score_size = 0 # small
            elif area >= size_medium_minimum and area < size_large_minimum:
                base_score_size = 2 # medium
            else:
                base_score_size = 4 # large
    print("size:", base_score_size) 
    #base_score_size = 0
    #size = input("enter size: s/m/l") # 
    #if size == "l":
    #    base_score_size = 4
    #elif size == "m":
    #    base_score_size = 2
    #print("size:", base_score_size) 

    # complexity
    if evaluationQuery == "building":
        base_score_complexity = 0
        complexities = []
        complexities.append( input("enter shape complexity: h/m/l"))
        complexities.append( input("enter roof complexity: h/m/l"))
        complexities.append( input("enter details complexity: h/m/l"))
        complexities.append( input("enter garden complexity: h/m/l"))
        complexities.append( input("enter overhang complexity: h/m/l"))
        
    elif evaluationQuery == "road":
        base_score_complexity = 0
        complexities = []
        complexities.append(input("enter detail complexity: h/m/l"))
        complexities.append(input("enter layout complexity: h/m/l"))
        
    elif evaluationQuery == "park":
        base_score_complexity = 0
        complexities = []
        complexities.append(input("enter layout (eg paths) complexity: h/m/l"))
        complexities.append(input("enter trees complexity: h/m/l"))
        complexities.append(input("enter bushes/flora complexity: h/m/l"))
        
    for c in complexities:
        if c == "h":
            base_score_complexity = base_score_complexity + 1
        elif c == "m":
            base_score_complexity = base_score_complexity + 0.5
    print("complexity:",base_score_complexity)

    # quality
    base_score_quality = 0
    quality = input("enter quality: h/m/l")
    if quality == "h":
        base_score_quality = 4
    elif quality == "m":
        base_score_quality = 2
    print("quality:", base_score_quality)
    
    final_score = BASE_POINTS + base_score_quality + base_score_size + base_score_complexity
    print(final_score)
    print("Type anything to clear the console and continue calculating.")
    input("")
    return final_score


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What is being evaluated:")
    print("- building")
    print("- park")
    print("- road\n")
    evaluationQuery = input("")
    if evaluationQuery == "building" or evaluationQuery == "park" or evaluationQuery == "road":
        final_score = calculatePoints(evaluationQuery)
    else:
        print("Invalid.")
