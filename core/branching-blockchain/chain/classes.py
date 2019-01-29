'''
# CLASSES
# This module exists as a tunnel connecting everything to the client module

'''

# Data and functions for users
class User:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.reputation = 0.0
        self.fullname = self.fullname_construction()

    # fullname
    def fullname_construction(self):
        return '{}{}'.format(self.first, self.last)
        
    # method for storing user reputation status
    def reputation_calc(self):
        category_rep = self.reputation

# Data and functions for ideas
class Idea:
    
    def __init__(self, title, category, value, creator):
        self.title = title
        self.category = category
        self.value = value
        self.creator = creator     # userfullname

