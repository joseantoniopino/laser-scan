from unittest import TestCase
from unittest.mock import MagicMock
from datetime import datetime

from src.domain.common.value_objects import Coordinates
from src.domain.laser.aggregates.shot import Shot
from src.domain.laser.interfaces.i_laser_shot import ILaserShot
from src.domain.laser.laser import Laser
from src.domain.target.target import Target


class TestLaser(TestCase):
    def setUp(self):
        self.origin = Coordinates(0, 0)
        self.target = Target(Coordinates(50, 50))
        self.shot = MagicMock(ILaserShot)
        self.shot.get_last_fire.return_value = datetime.now()
        self.laser = Laser(self.origin, self.target, self.shot)

    def test_initialization(self):
        origin = Coordinates(0, 0)
        target = Target(Coordinates(1, 1))
        shot = Shot(origin, target)
        laser = Laser(origin, target, shot)

        self.assertEqual(laser._origin, origin)
        self.assertEqual(laser._target, target)
        self.assertEqual(laser._shot, shot)

    def test_get_origin(self):
        laser = Laser(origin=self.origin, target=self.target, shot=self.shot)
        self.assertEqual(laser.get_origin(), self.origin)

    def test_fire(self):
        # Test fire
        self.laser.fire()
        self.shot.fire.assert_called_once()

        # Test last fire update
        last_fire = datetime.now()
        self.shot.get_last_fire.return_value = last_fire
        self.assertEqual(self.laser.get_last_fire(), last_fire)

    def test_get_last_fire(self):
        last_fire = datetime.now()
        self.shot.get_last_fire.return_value = last_fire
        self.assertEqual(self.laser.get_last_fire(), last_fire)
        self.shot.get_last_fire.assert_called_once()

    def test_str(self):
        expected_str = f"Laser(origin={self.origin}, target={self.target}, last_fire={self.shot.get_last_fire()})"
        self.assertEqual(str(self.laser), expected_str)

    def test_repr(self):
        expected_repr = f"Laser(origin={self.origin}, target={self.target}, last_fire={self.shot.get_last_fire()})"
        self.assertEqual(repr(self.laser), expected_repr)
