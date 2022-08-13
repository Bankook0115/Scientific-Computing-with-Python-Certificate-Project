import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__ (self,**kwargs):
    #print(kwargs)
    self.contents = []
    for k,v in kwargs.items(): #method ites to select the key and value
      for i in range(v):
        self.contents.append(k)
    #print(self.contents)

  def draw(self,number):
    ball_gotten = []
    if number > len(self.contents):
      return self.contents
    for i in range(number):
      random_ball = random.randint(0,len(self.contents)-1)
      ball_gotten.append(self.contents[random_ball])
      self.contents.remove(self.contents[random_ball])
    # print(ball_gotten)
    return ball_gotten


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count_m = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)
    #must copy becase it will remove the list when drawn the ball must use copy instead.
    for color in colors_gotten:
      if (color in expected_copy):
        expected_copy[color]-= 1
    if (all(x <= 0 for x in expected_copy.values())):
      count_m += 1
  return count_m/num_experiments
    
        
