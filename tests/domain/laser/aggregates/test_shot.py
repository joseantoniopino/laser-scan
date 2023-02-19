from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock

from src.domain.common.faction import Faction
from src.domain.common.value_objects import Coordinates
from src.domain.exceptions.domain_exception import DomainException
from src.domain.shot.shot import Shot
from src.domain.target.target import Target


class TestShot(TestCase):

    def setUp(self):
        self.origin = Coordinates(0, 0)
        self.target = Target(Coordinates(10, 10))
        self.shot = Shot(self.origin, self.target)

    def test_fire(self):
        # Check exception is raised when target is a friend.
        self.target.get_faction = MagicMock(return_value=Faction.REBEL.value)
        with self.assertRaises(DomainException) as cm:
            self.shot.fire()
        self.assertEqual(cm.exception.status_code, 422)
        self.assertEqual(cm.exception.code, 'target_friend')
        self.assertEqual(cm.exception.detail, 'Target is a friend!!')

        # Check exception is raised when the laser is reloading.
        self.target.get_faction = MagicMock(return_value=Faction.IMPERIAL.value)
        self.shot._last_fire = datetime.now()
        with self.assertRaises(DomainException) as cm:
            self.shot.fire()
        self.assertEqual(cm.exception.status_code, 400)
        self.assertEqual(cm.exception.code, 'reloading')
        self.assertEqual(cm.exception.detail, 'Laser is reloading...')

        # Check shot is fired correctly.
        self.shot._last_fire = None
        self.shot.fire()
        self.assertIsNotNone(self.shot.get_last_fire())

    def test_get_last_fire(self):
        # First shot expected to be None
        last_fire = self.shot.get_last_fire()
        self.assertIsNone(last_fire)

        # Shot and check that the current date and time is returned
        self.shot.fire()
        last_fire = self.shot.get_last_fire()
        self.assertIsInstance(last_fire, datetime)
        self.assertAlmostEqual(datetime.now(), last_fire, delta=timedelta(seconds=1))

    def test__can_fire(self):
        shot = Shot(self.origin, self.target)
        self.assertTrue(shot._can_fire())

        shot._last_fire = datetime.now()
        shot._reload_time = timedelta(seconds=30)
        self.assertFalse(shot._can_fire())

    def test_calculate_reload_time_distance_less_than_10(self):
        # Test 1: Distance less than 10
        origin = Coordinates(0, 0)
        target = Target(Coordinates(3, 4))
        shot = Shot(origin, target)
        reload_time = shot._calculate_reload_time()
        self.assertEqual(reload_time, timedelta(seconds=30))

    def test_calculate_reload_time_distance_between_10_and_50(self):
        # Test 2: Distance between 10 and 50
        origin = Coordinates(0, 0)
        target = Target(Coordinates(20, 20))
        shot = Shot(origin, target)
        reload_time = shot._calculate_reload_time()
        self.assertEqual(reload_time, timedelta(seconds=60))

    def test_calculate_reload_time_distance_between_50_and_100(self):
        # Test 3: Distance between 50 and 100
        origin = Coordinates(0, 0)
        target = Target(Coordinates(70, 70))
        shot = Shot(origin, target)
        reload_time = shot._calculate_reload_time()
        self.assertEqual(reload_time, timedelta(seconds=105))

    def test_calculate_reload_time_distance_greater_than_100(self):
        # Test 4: Distance greater than 100
        with self.assertRaises(DomainException) as context:
            origin = Coordinates(0, 0)
            target = Target(Coordinates(150, 150))
            shot = Shot(origin, target)
            reload_time = shot._calculate_reload_time()
        self.assertEqual(context.exception.status_code, 422)
        self.assertEqual(context.exception.code, 'out_of_range')
        self.assertEqual(context.exception.detail, 'Target is out of range.')

    def test__calculate_distance(self):
        # Test 1: Distance between (0, 0) and (3, 4)
        origin = Coordinates(0, 0)
        target = Target(Coordinates(3, 4))
        shot = Shot(origin, target)
        distance = shot._calculate_distance()
        self.assertEqual(distance, 5.0)

        # Test 2: Distance between (0, 0) and (5, 12)
        origin = Coordinates(0, 0)
        target = Target(Coordinates(5, 12))
        shot = Shot(origin, target)
        distance = shot._calculate_distance()
        self.assertEqual(distance, 13.0)

        # Test 3: Distance between (0, 0) and (-5, -12)
        origin = Coordinates(0, 0)
        target = Target(Coordinates(-5, -12))
        shot = Shot(origin, target)
        distance = shot._calculate_distance()
        self.assertEqual(distance, 13.0)
