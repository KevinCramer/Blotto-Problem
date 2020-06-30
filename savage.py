import random
import math
import operator
def nCr(n,r):
  f = math.factorial
  return f(n) / f(r) / f(n-r)

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
    soldiers_at_first_half = random.randint(0,num_soldiers)
    soldiers_at_second_half = num_soldiers - soldiers_at_first_half
    all_possible_entries_first_half = all_possible_entries(soldiers_at_first_half,num_castles/2)
    all_possible_entries_second_half = all_possible_entries(soldiers_at_second_half,num_castles/2)
    first_half_strategy = randomStrategy(soldiers_at_first_half,5)
    # first_half_strategy = random.choice(all_possible_entries_first_half)
    second_half_strategy = random.choice(all_possible_entries_second_half)
    # second_half_strategy = randomStrategy(soldiers_at_second_half,5)
    strategy = first_half_strategy + second_half_strategy
  return strategy


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
      score_player_1 += 1 
    elif strat1[i] < strat2[i]:
      score_player_2 += 1
    elif strat1[i] == strat2[i]:
      score_player_1 += 0.5
      score_player_2 += 0.5



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
  all_strategies = fixed_sample
  num_samples = len(all_strategies) 
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
  print all_strategies
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
  locals()['all_entries_{0}'.format(i)] = all_possible_entries(i,5)
  print i 

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



random_strats_120_6 = [[29, 28, 0, 7, 53, 3], [20, 30, 18, 6, 18, 28], [27, 4, 3, 0, 57, 29], [7, 19, 8, 2, 2, 82], [26, 9, 57, 18, 1, 9], [17, 34, 12, 15, 19, 23], [32, 15, 5, 48, 20, 0], [12, 40, 47, 6, 9, 6], [18, 42, 24, 7, 9, 20], [5, 3, 20, 39, 49, 4],[42, 41, 17, 8, 1, 11],[4, 8, 12, 4, 4, 88], [39, 11, 26, 0, 36, 8], [18, 9, 0, 71, 16, 6],[61, 19, 8, 1, 21, 10]]

def learning_agent2(num_soldiers,num_castles,num_consecutive_wins,num_best_strategies):
  best_strats = []
  while len(best_strats)< num_best_strategies:
    current_strat = random.choice(random_strats_120_6)
    counter = 0 

    while counter < num_consecutive_wins:
      opponent_strat =  random.choice(random_strats_120_6)
      current_strat_score = score_players(current_strat,opponent_strat)[0]
      opponent_strat_score = score_players(current_strat,opponent_strat)[1]
   
      if current_strat_score < opponent_strat_score:
        current_strat = opponent_strat
      else:
        counter +=1
    best_strats.append(current_strat)
  return best_strats