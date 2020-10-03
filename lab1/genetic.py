from typing import List
from itertools import permutations, combinations
import random
from random import randint
import copy

random.seed(42)

class Point:
    def __init__(self, x=None, y=None, name='No name'):
        self.x = x
        self.y = y
        self.name = name

    def randomly_fill(self, x_min, x_max,
                      y_min, y_max):
        self.x = randint(x_min, x_max)
        self.y = randint(y_min, y_max)

    #def __eq__(self, other):
        #return self.x == other.x and self.y == other.y

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Chromosome:
    starting_point = None

    def __init__(self, vec, starting_point=None):
        self.vec = vec
        self.starting_point = starting_point

    def mutate(self):
        i = randint(1, len(self.vec)-2)
        j = randint(1, len(self.vec)-2)
        temp = self.vec[i]
        self.vec[i] = self.vec[j]
        self.vec[j] = temp

    def truncate(self):
        if not Chromosome.starting_point:
            Chromosome.starting_point = self.vec[0]
        self.vec = self.vec[1:-1]

    def augment(self):
        sp = [Chromosome.starting_point]
        self.vec = sp + self.vec + sp

    def __repr(self):
        res = "["
        n = len(self.vec)
        for i in range(n):
            res += str(self.vec[i])
            if i == n-1:
                res += ']'
                break
            res += ','
        return res

    def __eq__(self, other):
        return self.vec == other.vec

    def __gt__(self, other):
        return fit_function(self) > fit_function(other)

    def __lt__(self, other):
        return fit_function(self) < fit_function(other)

    def __setitem__(self, key, value):
        self.vec[key] = value

    def __getitem__(self, key):
        return self.vec[key]

    def __len__(self):
        return len(self.vec)

    def __str__(self):
        return self.__repr()

    def __repr__(self):
        return self.__repr()


def create_points(amount):
    points = []
    for i in range(amount):
        p = Point(name=f"City:{i}")
        p.randomly_fill(0, 300, 0, 300)
        points.append(p)
    return points


def create_population(points, amount):
    starting_point = points.pop(0)
    sp = [starting_point]
    population = []
    i = 0

    while i != amount:
        random.shuffle(points)
        vec = sp + points + sp
        c = Chromosome(vec)
        if c not in population:
            population.append(c)
            i += 1

    return population


def transfer_genes(parent, child, _max, _min):
    n = len(parent)
    aug_i = list(range(_max, n)) + list(range(_max))
    j = _max%n
    for i in aug_i:
        if j == _min:
            break
        if parent[i] not in child:
            child[j] = parent[i]
            j = (j + 1)%n

    return child


def crossover(c1, c2, _max=None, _min=None):
    c1 = copy.copy(c1)
    c2 = copy.copy(c2)

    c1.truncate()
    c2.truncate()
    n = len(c1)

    if not _max or not _min:
        p1 = randint(1, n)
        p2 = (p1 + 3)%n
        _max, _min = max(p1, p2), min(p1, p2)
    #print("======================================")
    #print("Max: ", _max)
    #print("Min: ", _min)
    #print("C1: ", c1)
    #print("C2: ", c2)

    # here we have Ints instead of Points
    child_1 = Chromosome(['k']*n)
    child_2 = Chromosome(['k']*n)

    #print("Range: ", list(range(_min-1, _max)))

    for i in range(_min-1, _max):
        child_1[i] = c2[i]
        child_2[i] = c1[i]
    #print("child_1: ", child_1)
    #print("child_2: ", child_2)
    #print("======================================")

    child_1 = transfer_genes(c1, child_1, _max, _min)
    child_2 = transfer_genes(c2, child_2, _max, _min)

    child_1.augment()
    child_2.augment()

    return [child_1, child_2]


def euclide_distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**(1/2)


def fit_function(c):
    value = 0
    for i in range(len(c)-1):
        value += euclide_distance(c[i], c[i+1])
    return value


def selection(chromosomes, result_amount):
    c_sorted = sorted(chromosomes)
    for c in c_sorted:
        c.mutate()
    selected = c_sorted[:len(chromosomes)//2]
    combs = list(combinations(selected, 2))
    combs_selected = combs[:len(combs)//2]

    return combs_selected[:result_amount]


def create_new_population(combs):
    population = []
    for c in combs:
        population += crossover(c[0],c[1])
    return population
