import random

class Person:
    pox_x = 0
    pox_y = 0
    id = 0
    relations = []
    movable = True

    def __init__(self, pos_x, pos_y, id, relations):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = id
        self.relations = relations

    def calc_score(self, class_array):
        total_score = 0
        for person2 in class_array:
            total_score += self.calc_relation(person2)
        return total_score

    def calc_relation(self, person2):
        return self.relations[person2.id] + person2.relations[self.id]

    def match_pos(self, x, y):
        return x == self.pos_x and y == self.pos_y

def make_random_relations():
    relations = []
    for i in range(30):
        relations.append(random.randint(1, 10))
    return relations

def swap(person1, person2, class_array):
    pos1 = class_array.index(person1)
    pos2 = class_array.index(person2)
    class_array[pos1], class_array[pos2] = class_array[pos2], class_array[pos1]
    return class_array

def calc_total_score(class_array):
    total_score = 0
    for person in class_array:
        total_score += person.calc_score(class_array)
    return total_score

def predict_swap_score_difference(person1, person2, class_array):
    inital_score = calc_total_score(class_array)
    temp_class_array = class_array
    temp_class_array = swap(person1, person2, temp_class_array)
    predicted_score = calc_total_score(temp_class_array)
    return temp_class_array - class_array

def show_class(class_array):
    for y in range(6):
        for x in range(6):
            for person in class_array:
                if person.match_pos(x, y):
                    string = str(person.id)
                    if len(string) == 1:
                        string += " "
                    if x % 2 == 0:
                        print(string, end=" ")
                    else:
                        print(string, end="   ")
        print("")

#-------------------------------------------------------End of definitions-------------------------------------------------------#

class_array = []

#init class_array
id = 0
for x in range(6):
    for y in range(6):
        class_array.append(Person(x, y, id, make_random_relations()))
        id += 1

show_class(class_array)

#algo
# swap_thresh = 1
# iter_amt = 10
# for i in range(iter_amt):
#     for person1 in class_array:
#         for person2 in class_array:
#             if person1 != person2:
#                 if predict_swap_score_difference(person1, person2, class_array) > swap_thresh:
#                     swap(person1, person2, class_array)
