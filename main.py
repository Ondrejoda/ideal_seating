from __future__ import print_function

import random, math

class Person:
    def __init__(self, pos_x, pos_y, id, name, relations):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = id
        self.name = name
        self.relations = relations

    def calc_score(self, class_array):
        total_score = 0
        for person2 in class_array:
            total_score += self.calc_relation(person2)
        return total_score

    def calc_relation(self, person2, dist_weight=1):
        dist = math.hypot(person2.pos_x - self.pos_x, person2.pos_y - self.pos_y)
        score = (self.relations[person2.id] + person2.relations[self.id]) * ((8.5 - (dist / 8.5)) * dist_weight)
        return score

    def match_pos(self, x, y):
        return x == self.pos_x and y == self.pos_y

def make_random_relations():
    relations = []
    for i in range(50):
        relations.append(random.randint(1, 10))
    return relations

def swap(person1, person2, class_array):
    rtn = class_array.copy()
    tmp_x = person1.pos_x
    tmp_y = person1.pos_y
    person1.pos_x = person2.pos_x
    person1.pos_y = person2.pos_y
    person2.pos_x = tmp_x
    person2.pos_y = tmp_y
    pos1 = rtn.index(person1)
    pos2 = rtn.index(person2)
    rtn[pos1], rtn[pos2] = rtn[pos2], rtn[pos1]
    return rtn

def calc_total_score(class_array):
    total_score = 0
    for person in class_array:
        total_score += person.calc_score(class_array)
    return total_score / len(class_array)

def predict_swap_score_difference(person1, person2, class_array):
    inital_score = calc_total_score(class_array)
    temp_class_array = swap(person1, person2, class_array.copy())
    predicted_score = calc_total_score(temp_class_array)
    return predicted_score - inital_score

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
        class_array.append(Person(x, y, id, "id", make_random_relations()))
        id += 1

show_class(class_array)

#algo
print("algo")
swap_thresh = 10
iter_amt = 10
for i in range(iter_amt):
    for person1 in class_array:
        for person2 in class_array:
            if predict_swap_score_difference(person1, person2, class_array) > swap_thresh:
                class_array = swap(person1, person2, class_array)
                # print(person1.id, person2.id, "swapped, iter:", i + 1)
    show_class(class_array)
    print("total score:", calc_total_score(class_array))
    print("#######################################")
