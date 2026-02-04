'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
1. The warehouse function should add an item to an inventory list.
2. It uses a mutable default list parameter, which causes duplicates when
   the function is called more than once.
3. Fix the code so that each call starts with a fresh list unless an
   existing list is passed in.
'''

def add_item(item, inventory = None):
   if inventory == None:
      inventory=[]
   inventory.append(item)
   return inventory

print(add_item("stapler"))
print(add_item("pen"))
