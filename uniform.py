import random
import math
import operator

def randomStrategy2(num_soldiers,num_castles):
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
    first_half_strategy = random.choice(all_possible_entries_first_half)
    second_half_strategy = random.choice(all_possible_entries_second_half)
  return strategy


def randomStrategy(num_soldiers,num_castles):
  if num_castles == 1 :
    strategy = [num_soldiers]
  elif num_castles == 2:
    soldiers_at_castle_1 = random.randint(0,num_soldiers)

    soldiers_at_castle_2 = num_soldiers - soldiers_at_castle_1

    strategy = [soldiers_at_castle_1,soldiers_at_castle_2]
  elif num_castles > 2:
    num_castles_first_half = int(math.floor(float(num_castles)/2.0))

    num_castles_second_half = num_castles - num_castles_first_half

    # print num_castles_first_half,num_castles_second_half

    # print int(round(2*num_castles_first_half*(float(num_soldiers)/float(num_castles))))

    soldiers_in_first_half = random.randint(0,int(round(2*num_castles_first_half*(float(num_soldiers)/float(num_castles)))))
    soldiers_in_second_half = num_soldiers - soldiers_in_first_half
    # print soldiers_in_first_half, soldiers_in_second_half

    

    strategy_first_half = randomStrategy(soldiers_in_first_half,num_castles_first_half)

    strategy_second_half = randomStrategy(soldiers_in_second_half,num_castles_second_half)

    strategy  = strategy_first_half + strategy_second_half
  return strategy

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


