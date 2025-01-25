import unittest
import math
import complejos

class TestComplejos(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(complejos.suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(complejos.suma((0, 0), (0, 0)), (0, 0))
        self.assertEqual(complejos.suma((-1, -2), (1, 2)), (0, 0))
    
    def test_resta(self):
        self.assertEqual(complejos.resta((5, 6), (3, 4)), (2, 2))
        self.assertEqual(complejos.resta((0, 0), (0, 0)), (0, 0))
        self.assertEqual(complejos.resta((-1, -2), (-3, -4)), (2, 2))

    def test_producto(self):
        self.assertEqual(complejos.producto((1, 1), (1, -1)), (2, 0))
        self.assertEqual(complejos.producto((0, 0), (5, 6)), (0, 0))
        self.assertEqual(complejos.producto((2, 3), (-1, 4)), (-14, 5))

    def test_division(self):
        self.assertEqual(complejos.division((3, 2), (4, -3)), (0.24, 0.68))
        self.assertEqual(complejos.division((0, 0), (1, 1)), (0.0, 0.0))
        self.assertEqual(complejos.division((5, 5), (1, 1)), (5.0, 0.0))
        with self.assertRaises(ValueError):
            complejos.division((1, 1), (0, 0))

    def test_modulo(self):
        self.assertEqual(complejos.modulo((3, 4)), 5)
        self.assertEqual(complejos.modulo((0, 0)), 0)
        self.assertAlmostEqual(complejos.modulo((-3, -4)), 5, places=4)

    def test_conjugado(self):
        self.assertEqual(complejos.conjugado((3, -4)), (3, 4))
        self.assertEqual(complejos.conjugado((0, 0)), (0, 0))
        self.assertEqual(complejos.conjugado((-1, 2)), (-1, -2))

    def test_polar_a_cartesiano(self):
        self.assertAlmostEqual(complejos.polar_a_cartesiano((5, math.pi/4))[0], 3.5355, places=4)
        self.assertAlmostEqual(complejos.polar_a_cartesiano((5, math.pi/4))[1], 3.5355, places=4)
        self.assertAlmostEqual(complejos.polar_a_cartesiano((0, math.pi))[0], 0, places=4)
        self.assertAlmostEqual(complejos.polar_a_cartesiano((0, math.pi))[1], 0, places=4)
        self.assertAlmostEqual(complejos.polar_a_cartesiano((10, math.pi/2))[0], 0, places=4)
        self.assertAlmostEqual(complejos.polar_a_cartesiano((10, math.pi/2))[1], 10, places=4)

    def test_cartesiano_a_polar(self):
        self.assertAlmostEqual(complejos.cartesiano_a_polar((3, 4))[0], 5, places=4)
        self.assertAlmostEqual(complejos.cartesiano_a_polar((3, 4))[1], 0.9273, places=4)
        self.assertAlmostEqual(complejos.cartesiano_a_polar((0, 0))[0], 0, places=4)
        self.assertAlmostEqual(complejos.cartesiano_a_polar((0, 0))[1], 0, places=4)
        self.assertAlmostEqual(complejos.cartesiano_a_polar((1, 0))[0], 1, places=4)
        self.assertAlmostEqual(complejos.cartesiano_a_polar((1, 0))[1], 0, places=4)

    def test_fase(self):
        self.assertAlmostEqual(complejos.fase((1, 1)), math.pi / 4, places=4)
        self.assertAlmostEqual(complejos.fase((0, 1)), math.pi / 2, places=4)
        self.assertAlmostEqual(complejos.fase((1, 0)), 0, places=4)

if __name__ == "__main__":
    unittest.main()
