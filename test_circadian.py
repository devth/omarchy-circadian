import datetime as dt
import runpy
import unittest

app = runpy.run_path('circadian')

class SolarTests(unittest.TestCase):
    def test_equator_day_and_night(self):
        day = dt.datetime(2026, 3, 20, 12, tzinfo=dt.timezone.utc)
        night = day.replace(hour=0)
        self.assertTrue(app['is_day'](day, 0, 0))
        self.assertFalse(app['is_day'](night, 0, 0))

    def test_polar_seasons(self):
        june = dt.datetime(2026, 6, 21, 0, tzinfo=dt.timezone.utc)
        december = dt.datetime(2026, 12, 21, 12, tzinfo=dt.timezone.utc)
        self.assertTrue(app['is_day'](june, 89, 0))
        self.assertFalse(app['is_day'](december, 89, 0))

    def test_coordinates(self):
        with self.assertRaises(ValueError):
            app['coordinates'](91, 0, 'bad')

if __name__ == '__main__': unittest.main()
