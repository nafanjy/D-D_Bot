import random
import vars



def roll(input_string):
  parse_roll = input_string.split('+')
  return_total = 0
  roll_values = []
  roll_string = '['
  
  for i in parse_roll:
    in_value = i.strip().rstrip()
    #if addition is a die then parse out values
    if 'd' in in_value:
      #if die parse fails then call yourself stupid
      try:
        parse_dice = in_value.split('d')
        num_of_dice = parse_dice[0]
        size_of_dice = int(parse_dice[1])
        if size_of_dice not in vars.valid_sizes:
          return "Sorry, I'm too dumb to understand what you want..."
        for j in range(int(num_of_dice)):
          num_to_add = random.randint(1, size_of_dice)
          roll_values.append(num_to_add)
          return_total += num_to_add
      except:
        return "Sorry, I'm too dumb to understand what you want..."
    #addition is not a die so it must be an integer
    else:
      #if the addition is not an integer then fail
      try:
        value_to_add = int(in_value)
        return_total += value_to_add
      except:
        return "Sorry, I'm too dumb to understand what you want..."
  for k in roll_values:
    roll_string += str(k) + ","
  roll_string = roll_string.rstrip(roll_string[-1])
  roll_string += "]"
  return_string = str(return_total) + " " + roll_string
  return return_string



def conversation(name):
  response_options = [
    "Fuck you, " + name + "!",
    "Omg! Hey, " + name + "!",
    "Hi " + name,
    "What's up?",
    "Am I alive?",
    "Hey, " + name,
    "Everyone be quiet, " + name + " is here...",
    "Yo",
    "Sup rich homie " + name,
    "What's good?"
  ]
  
  response_to_send = ''
  length_of_options = len(response_options)

  index_of_choice = random.randint(0, length_of_options - 1)
  response_to_send = response_options[index_of_choice]

  return response_to_send



def feeling_sad(name):
  starter_encouragements = [
    "Cheer up, " + name + "!",
    "Hang in there, " + name + "!",
    "You are a great person, " + name + ".",
  ]
    
  return random.choice(starter_encouragements)