import os

BASE_POINTS = 10

def calculatePoints(evaluationQuery):
    
    # size
    base_score_size = 0
    size = input("enter size: s/m/l") # 
    if size == "l":
        base_score_size = 4
    elif size == "m":
        base_score_size = 2
    print("size:", base_score_size) 

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