class Person:
    pox_x = 0
    pox_y = 0
    id = 0
    relations = []

    def __init__(self, pos_x, pos_y, id, relations) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.id = id
        self.relations = relations

    def calc_score(self, class_array):
        pass

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

#-------------------------------------------------------End of definitions-------------------------------------------------------#

class_array = []

for i in range(30):
    class_array.append(Person(0, 0, i, []))