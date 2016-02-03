#Author: Sudarshan Pawar
#Note: Animal's names(here) are just for educational purpose. Actual facts about them are not considered here.

import random
race_animals=['Gazelle','Tiger','Zebra','Kangaroo','Cheetah']
weight_animals=['Elephant','Gorilla','Hippopotamus','Bison',]
swimming=['Shark','Whale','Stringray','Catfish']

print"""
   *** 2015 ANIMAL OLYMPICS,South Africa ***
       400 Mtr. Sprint Race
______________________________________________
|| bear | tiger | zebra | kangaroo | Cheetah ||
||------|-------|-------|----------|---------||
|| L:1  |  L:2  |  L:3  |   L:4    |   L:5   ||
||      |       |       |          |         ||
||      |       |       |          |         ||
||      |       |       |          |         ||
||      |       |       |          |         ||
                 
"""

#RESULTS_RACING
def calc_race():
    race_result=random.sample(race_animals,3)
    print "<<<RESULTS>>>"
    print "1st Position: ",race_result[0],"(G)"
    print "2nd Position: ",race_result[1],"(S)"
    print "3rd Position: ",race_result[2],"(B)"
calc_race()

##########################################################

print"""
   *** 2015 ANIMAL OLYMPICS,South Africa ***
       Heavy Weight Champions
"""
print "Participants:",weight_animals       
print """
            ||||                    ||||
          ||||||                    ||||||
     ====|||||||====================|||||||====
     ====|||||||====================|||||||====
          ||||||                    ||||||
            ||||                    ||||
"""
#RESULTS_weights
def calc_weight():
    weight_result=random.sample(weight_animals,3)
    weights=random.sample(xrange(100,501),3)
    weights.sort()
    print "1st Position: ",weight_result[0],"Lifted ",weights[2],"Kgs","(G)"
    print "2nd Position: ",weight_result[1],"Lifted ",weights[1],"Kgs","(S)"
    print "3rd Position: ",weight_result[2],"Lifted ",weights[0],"Kgs","(B)"

calc_weight()
############################################################



print """

*** 2015 ANIMAL OLYMPICS,South Africa ***
       200 Mtr. Freestyle Swimming
"""
print "Participants:",swimming

print """
  _______________________________________________________________
|Lane 1|Shark~.~.~.~.~~.~.~.~.~.~~.~.~.~..~.~-.~.~..~.~~.~.-~~.~.]
|Lane 2|Whale.~.~~.~.~-.-~.~.~~.~-.~.~.~~.~.~.~~..-~.~.~.~.~.~.~~]
|Lane 3|Stringray~.~.-~.~.~~.~.~.~-.--~.~~.~.~-~.~.~.~.~..~.~~.~.]
|Lane 4|Catfish-.~.~~.~.~.~.~-.~~.~.~.~.~~.~.~.-..~.~.~.~.~.~.~~.]
||_______________________________________________________________]

"""

def calc_swim():
    swim_standings=random.sample(swimming,3)
    swim1=random.uniform(5.0,10.0)
    swim2=random.uniform(5.0,10.0)
    swim3=random.uniform(5.0,10.0)

    swim_1=swim1
    swim_2=swim1-1.0
    swim_3=swim1-1.75
    swim_result=[swim_1,swim_2,swim_3]
    print "<<<Results>>>"
    print "1st Position: ",swim_standings[0],"in ",swim_result[2],"Seconds"
    print "2nd Position: ",swim_standings[1],"in ",swim_result[1],"Seconds"
    print "3rd Position: ",swim_standings[2],"in ",swim_result[0],"Seconds"

calc_swim()
    
