import unittest
import os, sys
import math

sys.path.append(os.getcwd())

from main import *

class TestTransferGenes(unittest.TestCase):
    def test_1_transfer_genes(self):
        _min, _max = 3, 5
        parent = Chromosome([4,2,6,3,1,5])
        child = Chromosome([0,0,3,4,5,0])
        result = transfer_genes(parent,child,_max,_min)
        self.assertEqual(
            result,
            Chromosome([6,1,3,4,5,2])
        )

    def test_2_transfer_genes(self):
        _min, _max = 3, 5
        parent = Chromosome([1,2,3,4,5,6])
        child = Chromosome([0,0,6,3,1,0])
        result = transfer_genes(parent,child,_max,_min)
        self.assertEqual(
            result,
            Chromosome([4,5,6,3,1,2])
        )

    def test_3_transfer_genes(self):
        #import pdb; pdb.set_trace()
        _min, _max = 3, 5
        parent = Chromosome([8,2,1,4,3,5,7,6])
        child = Chromosome([0,0,3,6,5,0,0,0])
        result = transfer_genes(parent,child,_max,_min)
        self.assertEqual(
            result,
            Chromosome([1,4,3,6,5,7,8,2])
        )


class TestCrossover(unittest.TestCase):
    def test_1_crossover(self):
        parent_1 = Chromosome([0,1,2,3,4,5,6,0])
        parent_2 = Chromosome([0,4,2,6,3,1,5,0])
        children = crossover(parent_1, parent_2, 5, 3)
        assertEqual(children, [
            Chromosome([0,4,5,6,3,1,2,0]),
            Chromosome([0,6,1,3,4,5,2,0])
        ])

    def test_2_crossover(self):
        parent_1 = Chromosome([0,8,2,1,4,3,5,7,6,0])
        parent_2 = Chromosome([0,4,7,3,6,5,2,8,1,0])
        children = crossover(parent_1, parent_2, 5, 2)
        assertEqual(children, [
            Chromosome([0,1,4,3,6,5,7,8,2,0]),
            Chromosome([0,6,5,1,4,3,2,8,7,0])
        ])

    def test_2_crossover(self):
        parent_1 = Chromosome([0,4,3,6,2,1,5,0])
        parent_2 = Chromosome([0,4,6,2,5,1,3,0])
        children = crossover(parent_1, parent_2)
        print(children)


class TestEuclideDistance(unittest.TestCase):
    def test_1_euclidian_distance(self):
        p1 = Point(4, 0, "one")
        p2 = Point(4, 5, "two")
        self.assertEqual(euclide_distance(p1, p2), 5)

    def test_2_euclidian_distance(self):
        p1 = Point(3, 5)
        p2 = Point(6, 9)
        self.assertEqual(euclide_distance(p1, p2), 5)


class TestFitFunction(unittest.TestCase):
    def test_1_fit_function(self):
        p1, p2, p3 = Point(3, 5), Point(4, 1), Point(2,2)
        c = Chromosome([p1, p2, p3])
        self.assertAlmostEqual(fit_function(c),
                               6.359173, places=5)


class TestSelection(unittest.TestCase):
    pass

class TestCrossover(unittest.TestCase):
    pass

class TestCreateNewPopulation(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
