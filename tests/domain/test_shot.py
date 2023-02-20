from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.domain.common.entity_factory import EntityFactory
from src.domain.shot.shot import Shot
from src.infrastructure.repositories.LaserRepository import LaserRepository
from src.infrastructure.repositories.TargetRepository import TargetRepository


class TestShot(TestCase):
    @patch('src.domain.shot.shot_checker.ShotChecker.can_fire')
    def setUp(self, mock_can_fire):
        self.mock_laser = MagicMock()
        self.mock_target = {"id": "some_id"}
        self.entity_factory = EntityFactory()
        self.target_repository = TargetRepository()
        self.laser_repository = LaserRepository()
        self.shot = Shot(self.target_repository, self.laser_repository, self.entity_factory)
        self.mock_can_fire = mock_can_fire

    def test_shot_can_fire(self):
        mock_laser_id = "some_id"
        mock_target_id = "some_id"
        mock_last_shot = datetime.utcnow() - timedelta(minutes=2)
        self.mock_laser.get_last_shot.return_value = mock_last_shot
        self.mock_laser.create_shot.return_value = mock_last_shot
        self.mock_can_fire.return_value = (True, timedelta())

        can_fire, time_to_wait, laser_id, target_id = self.shot.shot(mock_laser_id, mock_target_id)

        self.assertTrue(can_fire)
        self.assertEqual(time_to_wait, timedelta())
        self.assertEqual(laser_id, mock_laser_id)
        self.assertEqual(target_id, mock_target_id)
