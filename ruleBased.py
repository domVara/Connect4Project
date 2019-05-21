from pyknow import *
from Knowledge import *
from numpy import *

class step(Fact):
      """Inference Engine For a Connect-Four agent utilizing the facts and Knowledge from the knowledge base to infer and take a winning or drawing action to aggressively attack or defend against an Human playing agent or computer playing agent."""
      pass

class ConnectFourEngine(KnowledgeEngine):
 def __init__(self,s):
  self.stepToTake = []
  self.state = s
 
 @Rule(numpy.count_nonzero(state == 0) > 36)
 def play_InMiddle():
  self.stepToTake.append(2);
