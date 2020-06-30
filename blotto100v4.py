import random
import math
import operator
import copy
def nCr(n,r):
  f = math.factorial
  return f(n) / f(r) / f(n-r)

entries_cache = {}
def all_possible_entries(num_soldiers,num_castles):
  sequences = []
  if (num_soldiers,num_castles) in entries_cache:
    return entries_cache[(num_soldiers,num_castles)]

  elif num_castles ==1:
    sequences += [[num_soldiers]]
    entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences
  elif num_castles ==2:
    for i in range(0,num_soldiers+1):
      sequences += [[i,num_soldiers - i]]
    entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences
  elif num_castles > 2:
    lower_half_castles = int(math.floor(num_castles/2.0))
    higher_half_castles = num_castles - lower_half_castles
    split_soldiers = all_possible_entries(num_soldiers,2)
    for i in range(0,len(split_soldiers)):
      a = len(all_possible_entries(split_soldiers[i][0],lower_half_castles))
      b = len(all_possible_entries(split_soldiers[i][1],higher_half_castles))
      for j in range(0,a):
        for k in range(0,b):
          entry = all_possible_entries(split_soldiers[i][0],lower_half_castles)[j] + all_possible_entries(split_soldiers[i][1],higher_half_castles)[k]
          sequences += [entry]
    entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences

for i in range(0,101):
  globals()['all_entries_{0}'.format(i)] = all_possible_entries(i,5)
  print i 

mylist = []
mylist.append(all_entries_0)
mylist.append(all_entries_1)
mylist.append(all_entries_2)
mylist.append(all_entries_3)
mylist.append(all_entries_4)
mylist.append(all_entries_5)
mylist.append(all_entries_6)
mylist.append(all_entries_7)
mylist.append(all_entries_8)
mylist.append(all_entries_9)
mylist.append(all_entries_10)
mylist.append(all_entries_11)
mylist.append(all_entries_12)
mylist.append(all_entries_13)
mylist.append(all_entries_14)
mylist.append(all_entries_15)
mylist.append(all_entries_16)
mylist.append(all_entries_17)
mylist.append(all_entries_18)
mylist.append(all_entries_19)
mylist.append(all_entries_20)
mylist.append(all_entries_21)
mylist.append(all_entries_22)
mylist.append(all_entries_23)
mylist.append(all_entries_24)
mylist.append(all_entries_25)
mylist.append(all_entries_26)
mylist.append(all_entries_27)
mylist.append(all_entries_28)
mylist.append(all_entries_29)
mylist.append(all_entries_30)
mylist.append(all_entries_31)
mylist.append(all_entries_32)
mylist.append(all_entries_33)
mylist.append(all_entries_34)
mylist.append(all_entries_35)
mylist.append(all_entries_36)
mylist.append(all_entries_37)
mylist.append(all_entries_38)
mylist.append(all_entries_39)
mylist.append(all_entries_40)
mylist.append(all_entries_41)
mylist.append(all_entries_42)
mylist.append(all_entries_43)
mylist.append(all_entries_44)
mylist.append(all_entries_45)
mylist.append(all_entries_46)
mylist.append(all_entries_47)
mylist.append(all_entries_48)
mylist.append(all_entries_49)
mylist.append(all_entries_50)
mylist.append(all_entries_51)
mylist.append(all_entries_52)
mylist.append(all_entries_53)
mylist.append(all_entries_54)
mylist.append(all_entries_55)
mylist.append(all_entries_56)
mylist.append(all_entries_57)
mylist.append(all_entries_58)
mylist.append(all_entries_59)
mylist.append(all_entries_60)
mylist.append(all_entries_61)
mylist.append(all_entries_62)
mylist.append(all_entries_63)
mylist.append(all_entries_64)
mylist.append(all_entries_65)
mylist.append(all_entries_66)
mylist.append(all_entries_67)
mylist.append(all_entries_68)
mylist.append(all_entries_69)
mylist.append(all_entries_70)
mylist.append(all_entries_71)
mylist.append(all_entries_72)
mylist.append(all_entries_73)
mylist.append(all_entries_74)
mylist.append(all_entries_75)
mylist.append(all_entries_76)
mylist.append(all_entries_77)
mylist.append(all_entries_78)
mylist.append(all_entries_79)
mylist.append(all_entries_80)
mylist.append(all_entries_81)
mylist.append(all_entries_82)
mylist.append(all_entries_83)
mylist.append(all_entries_84)
mylist.append(all_entries_85)
mylist.append(all_entries_86)
mylist.append(all_entries_87)
mylist.append(all_entries_88)
mylist.append(all_entries_89)
mylist.append(all_entries_90)
mylist.append(all_entries_91)
mylist.append(all_entries_92)
mylist.append(all_entries_93)
mylist.append(all_entries_94)
mylist.append(all_entries_95)
mylist.append(all_entries_96)
mylist.append(all_entries_97)
mylist.append(all_entries_98)
mylist.append(all_entries_99)
mylist.append(all_entries_100)






# x = []
# for i in range(0,101):
#   x.append([i,nCr(i+4,4)])

# y = []
# for i in range(0,101):
#   y.append([i,x[i][1]*x[100-i][1]])

# total_combinations = 0
# for i in range(0,101):
#   total_combinations += y[i][1]

# for i in range(0,101):
#   y[i][1]= float(y[i][1])/total_combinations

# weighted_list = []

# for i in range(0,101):
#   for j in range(0,int(round(y[i][1]*100000000))):
#     weighted_list.append(y[i][0])
    
# def half_cutter(num_soldiers,num_castles):
#   dist = []
#   total_combinations = 0
#   for i in range(0,num_soldiers+1):
#     combinations = len(all_possible_entries(i,num_castles/2))*len(all_possible_entries(num_soldiers-i, num_castles/2))
#     dist.append([i,combinations])
#     total_combinations += combinations
#   for i in range(0,len(dist)):
#     dist[i][1] = float(dist[i][1])/float(total_combinations)
#   return dist

def weighted_half_cutter(num_soldiers,num_castles,acc):
  weighted_list = []
  distr = half_cutter(num_soldiers,num_castles)
  for i in range(0,num_soldiers+1):
    for j in range(0,int(round(distr[i][1]*acc))):
      weighted_list.append(distr[i][0])
  return weighted_list

def randomStrategy(num_soldiers,num_castles):
  if num_castles == 1 :
    strategy = [num_soldiers]
  elif num_castles == 2:
    soldiers_at_castle_1 = random.randint(0,num_soldiers)

    soldiers_at_castle_2 = num_soldiers - soldiers_at_castle_1

    strategy = [soldiers_at_castle_1,soldiers_at_castle_2]
  elif num_castles > 2:
    soldiers_at_first_half =random.randint(0,num_soldiers)
    soldiers_at_second_half = num_soldiers - soldiers_at_first_half
    entries_first_half = mylist[soldiers_at_first_half]
    entries_second_half = mylist[soldiers_at_second_half]
    first_half_strategy = random.choice(entries_first_half)
    # first_half_strategy = random.choice(all_possible_entries_first_half)
    second_half_strategy = random.choice(entries_second_half)
    # second_half_strategy = randomStrategy(soldiers_at_second_half,5)
    strategy = first_half_strategy + second_half_strategy
  return strategy

# for i in range(0, 50):
#   locals()['all_entries_{0}'.format(i)] = all_possible_entries(i,5)
#   print i 


# def randomStrategy(num_soldiers,num_castles):
#   if num_castles == 1 :
#     strategy = [num_soldiers]
#   elif num_castles == 2:
#     soldiers_at_castle_1 = random.randint(0,num_soldiers)

#     soldiers_at_castle_2 = num_soldiers - soldiers_at_castle_1

#     strategy = [soldiers_at_castle_1,soldiers_at_castle_2]
#   elif num_castles > 2:
#     num_castles_first_half = int(math.floor(float(num_castles)/2.0))

#     num_castles_second_half = num_castles - num_castles_first_half

#     # print num_castles_first_half,num_castles_second_half

#     # print int(round(2*num_castles_first_half*(float(num_soldiers)/float(num_castles))))

#     soldiers_in_first_half = random.randint(0,int(round(2*num_castles_first_half*(float(num_soldiers)/float(num_castles)))))
#     soldiers_in_second_half = num_soldiers - soldiers_in_first_half
#     # print soldiers_in_first_half, soldiers_in_second_half

    

#     strategy_first_half = randomStrategy(soldiers_in_first_half,num_castles_first_half)

#     strategy_second_half = randomStrategy(soldiers_in_second_half,num_castles_second_half)

#     strategy  = strategy_first_half + strategy_second_half
#   return strategy

entries_cache = {} #this acts as a a cache for the function below, allowing it to instantly recall smaller subproblems that it has already solved. This method is called dynamic programming
def all_possible_entries(num_soldiers,num_castles):
    sequences = []    # sequences is a list that will store all the possible battle configurations for the blotto-problem(num_soldiers,num_castles)
  if (num_soldiers,num_castles) in entries_cache:
    return entries_cache[(num_soldiers,num_castles)]
  
  elif num_castles ==1:
    sequences += [[num_soldiers]]
    entries_cache[(num_soldiers,num_castles)] = sequences   #
    return sequences
  elif num_castles ==2:
    for i in range(0,num_soldiers+1):
      sequences += [[i,num_soldiers - i]]
    entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences
  elif num_castles > 2:
    lower_half_castles = int(math.floor(num_castles/2.0))  # Here I split the number of castles into two equal parts called lower_half_castles and upper_half_castles. They differ in size by 1 if num_castles is odd.
    higher_half_castles = num_castles - lower_half_castles
    split_soldiers = all_possible_entries(num_soldiers,2) #here split soldiers is a list containing all the ways of splitting the soldiers amongst the lower_half_castles and upper_half_castles
    for i in range(0,len(split_soldiers)):
        a = len(all_possible_entries(split_soldiers[i][0],lower_half_castles)) # a is the number of configurations for the blotto-problem(
        b = len(all_possible_entries(split_soldiers[i][1],higher_half_castles))
      for j in range(0,a):
        for k in range(0,b): #this nested for loop
          entry = all_possible_entries(split_soldiers[i][0],lower_half_castles)[j] + all_possible_entries(split_soldiers[i][1],higher_half_castles)[k]
          sequences += [entry]
    entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences

def is_it_uniform(num_soldiers,num_castles,num_samples):
  all_strategies = all_possible_entries(num_soldiers,num_castles)
  n = len(all_strategies)
  distribution = [0]*n
  print (all_strategies)
  for i in range(0,num_samples):
    random_strat = randomStrategy(num_soldiers,num_castles)
    # print random_strat
    for j in range(0,n):
      if all_strategies[j] == random_strat:
        distribution[j] += 1
    # print distribution 
  return distribution

fib_cache = {}
def fib(n):
  if n in fib_cache:
    return fib_cache[n]
  elif n < 2:
      value = n
  else:
    value = fib(n-1) + fib(n-2)
    fib_cache[n] = value
  return value

# def nCr(n,r):
#   f = math.factorial
#   return f(n) / f(r) / f(n-r)

# x = []
# for i in range(0,101):
#   x.append([i,nCr(i+4,4)])

# y = []
# for i in range(0,101):
#   y.append([i,x[i][1]*x[100-i][1]])

# total_combinations = 0
# for i in range(0,101):
#   total_combinations += y[i][1]
# print total_combinations


# for i in range(0,101):
#   y[i][1]= float(y[i][1])/total_combinations

# weighted_list = []

# for i in range(0,101):
#   for j in range(0,int(round(y[i][1]*100000000))):
#     weighted_list.append(y[i][0])




def score_players(strat1,strat2):
  assert len(strat1) == len(strat2)
  score_player_1 = 0
  score_player_2 = 0
  for i in range(0,len(strat1)):
    if strat1[i] > strat2[i]:
      score_player_1 += i+1
    elif strat1[i] < strat2[i]:
      score_player_2 += i+1
    elif strat1[i] == strat2[i]:
      score_player_1 += 0
      score_player_2 += 0



  return [score_player_1,score_player_2]

def random_samples(num_soldiers,num_castles,num_samples):
  all_strategies = []
  for i in range(num_samples):
    x = randomStrategy(num_soldiers,num_castles)
    all_strategies.append(x)
  return all_strategies 

def round_robbin_average_score(num_soldiers,num_castles,num_samples):
  all_strategies = random_samples(num_soldiers,num_castles,num_samples)
  scores = [0]*num_samples
  
  for i in range(0,num_samples):
    for j in range(i,num_samples):
      if i != j:
        scores[i] += score_players(all_strategies[i],all_strategies[j])[0]
        scores[j] += score_players(all_strategies[i],all_strategies[j])[1]
  for i in range(0,num_samples):
    scores[i] = round(float(scores[i])/float(num_samples-1),2)

  dicts = {}
  keys = range(1,num_samples+1)
  values = scores
  for i in keys:
    dicts[i] = values[i-1]
  sorted_d = sorted(dicts.items(), key=operator.itemgetter(1))
  print(sorted_d)
  for i in range(0,num_samples):
    all_strategies[i].append([i+1])
  # for i in range(0,num_samples):
  #   (all_strategies[i]).append([scores[i]])
  # scores.sort()

  print all_strategies
def learning_agent(num_soldiers,num_castles,num_consecutive_wins,num_best_strategies):
  best_strats = []
  while len(best_strats)< num_best_strategies:
    current_strat = randomStrategy(num_soldiers,num_castles)
    counter = 0 

    while counter < num_consecutive_wins:
      opponent_strat =  randomStrategy(num_soldiers,num_castles)
      current_strat_score = score_players(current_strat,opponent_strat)[0]
      opponent_strat_score = score_players(current_strat,opponent_strat)[1]
   
      if current_strat_score < opponent_strat_score:
        current_strat = opponent_strat
      else:
        counter +=1
    best_strats.append(current_strat)
  return best_strats
    
  
def fixed_round_robbin_average_score(num_soldiers,num_castles,fixed_sample):
  all_strategies = copy.deepcopy(fixed_sample)
  num_samples = len(all_strategies) 
  scores = [0]*num_samples
  
  for i in range(0,num_samples):
    for j in range(i,num_samples):
      if i != j:
        scores[i] += score_players(all_strategies[i],all_strategies[j])[0]
        scores[j] += score_players(all_strategies[i],all_strategies[j])[1]
  for i in range(0,num_samples):
    scores[i] = float(scores[i])/float(num_samples-1)

  dicts = {}
  keys = range(1,num_samples+1)
  values = scores
  for i in keys:
    dicts[i] = values[i-1]
  sorted_d = sorted(dicts.items(), key=operator.itemgetter(1))
##  print(sorted_d)
  numbered_all_strategies = all_strategies
  for i in range(0,num_samples):
    numbered_all_strategies[i].append([i+1])
##  print all_strategies
  return sorted_d, numbered_all_strategies
  # for i in range(0,num_samples):
  #   (all_strategies[i]).append([scores[i]])
  # scores.sort()
  
def basic(x):
  entries = []
  for i in range(0,x+1):
    entry_i = []
    entry_i += [i]
    entry_i += [x - i] 
    entries += [entry_i]
  return entries

def entries(x,y):
  entries = []
  if y == 1:
    entries += [x]
    print entries
  else:
    entry = []
    print entry 
    for i in range(0,x+1):
      remainder = basic(x-i)
      for j in range(0,len(remainder)-1):
        entry += [i]
        
        entry += remainder[j]
        print entry 
  return entries



def basic(x):
  entries = []
  for i in range(0,x+1):
    entry_i = []
    entry_i += [i]
    entry_i += [x - i] 
    entries += [entry_i]
    #print entry_i
 # print entries
  return entries

def split(n):
  lower = int(math.floor(n/2.0))
  higher = n - lower 
  return [lower, higher]

# def entries2(x,y):
#   entry = []
#   if y == 1:
#     return [x]
#   elif y == 2:
#     return basic(x)
#   elif y > 2:
#     splits = basic(x)
#     lower = int(math.floor(y/2.0)
#     higher = y - lower 
#     for i in range(0,len(basic(x))):
#       entry += entries2(basic(x)[i][0])
#       entry += entries2(basic(x)[i][1])
#       return entry 



def is_it_uniform(num_soldiers,num_castles,num_samples):
  all_strategies = all_possible_entries(num_soldiers,num_castles)
  n = len(all_strategies)
  distribution = [0]*n
  print all_strategies
  for i in range(0,num_samples):
    random_strat = randomStrategy(num_soldiers,num_castles)
    # print random_strat
    for j in range(0,n):
      if all_strategies[j] == random_strat:
        distribution[j] += 1
    # print distribution
  return distribution

entries_cache = {} #this acts as a a cache for the function below, allowing it to instantly recall smaller subproblems that it has already solved. This method is called dynamic programming
def all_possible_entries(num_soldiers,num_castles):
    sequences = []    # sequences is a list that will store all the possible battle configurations for the blotto-problem(num_soldiers,num_castles)
        if (num_soldiers,num_castles) in entries_cache:
            return entries_cache[(num_soldiers,num_castles)]
                
                elif num_castles ==1:
sequences += [[num_soldiers]]
    entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences
        elif num_castles ==2:
for i in range(0,num_soldiers+1):
    sequences += [[i,num_soldiers - i]]
    entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences
        elif num_castles > 2:
lower_half_castles = int(math.floor(num_castles/2.0))  # Here I split the number of castles into two equal parts called lower_half_castles and upper_half_castles. They differ in size by 1 if num_castles is odd.
    higher_half_castles = num_castles - lower_half_castles
    split_soldiers = all_possible_entries(num_soldiers,2) #here split soldiers is a list containing all the ways of splitting the soldiers amongst the lower_half_castles and upper_half_castles, not counting the configurations within the halves that is. i.e there are (num_soldiers +1) ways to split the soldiers.
    for i in range(0,len(split_soldiers)):
        a = len(all_possible_entries(split_soldiers[i][0],lower_half_castles)) # a is the number of configurations for the blotto-problem(number of soldiers assigned to lower_half_castles for current value of i, lower_half_castles)
        b = len(all_possible_entries(split_soldiers[i][1],higher_half_castles))# b is the number of configurations for the blotto-problem(number of soldiers assigned to upper_half_castles for current value of i, higher_half_castles)
            for j in range(0,a):
                for k in range(0,b): #this nested loop iterates over all possible configurations for the way of splitting soldiers amongst the two halves that corresponds to split_soldiers[i]
                    entry = all_possible_entries(split_soldiers[i][0],lower_half_castles)[j] + all_possible_entries(split_soldiers[i][1],higher_half_castles)[k] #entry is the conjunction of the configurations for the halves
                        sequences += [entry]
entries_cache[(num_soldiers,num_castles)] = sequences
    return sequences



