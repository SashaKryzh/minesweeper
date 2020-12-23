from enum import Enum


class Difficulty(Enum):
	"""
		value: width, height, mines
	"""
	EASY = 10, 10, 5
	MEDIUM = 16, 16, 20
	HARD = 10, 90, 5
