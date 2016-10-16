import unittest
from bars import calc_distance_between_two_coordinates


class BarsTestCase(unittest.TestCase):
    def test_calc_distance_on_real_data(self):
        # http://gis-lab.info/qa/great-circles.html
        dist1 = calc_distance_between_two_coordinates(
            77.1539, -139.398, -77.1804, -139.55
        )
        dist2 = calc_distance_between_two_coordinates(
            77.1539, 120.398, 77.1804, 129.55
        )
        dist3 = calc_distance_between_two_coordinates(
            77.1539, -120.398, 77.1804, 129.55
        )

        self.assertEqual(round(dist1), 17166029)
        self.assertEqual(round(dist2), 225883)
        self.assertEqual(round(dist3), 2332669)

if __name__ == '__main__':
    unittest.main()
