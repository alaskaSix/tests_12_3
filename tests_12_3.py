import unittest
from runner_and_tournament import Runner, Tournament

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        runner = Runner("Усэйн", speed=10)
        self.assertEqual(runner.speed, 10)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Андрей", speed=9)
        self.assertEqual(runner.speed, 9)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Ник", speed=3)
        self.assertEqual(runner.speed, 3)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Тесты будут заморожены

    @skip_if_frozen
    def test_first_tournament(self):
        usain = Runner("Усэйн", speed=10)
        nick = Runner("Ник", speed=3)
        tournament = Tournament(90, usain, nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[0].name, "Усэйн")

    @skip_if_frozen
    def test_second_tournament(self):
        andrey = Runner("Андрей", speed=9)
        nick = Runner("Ник", speed=3)
        tournament = Tournament(90, andrey, nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[0].name, "Андрей")

    @skip_if_frozen
    def test_third_tournament(self):
        usain = Runner("Усэйн", speed=10)
        andrey = Runner("Андрей", speed=9)
        nick = Runner("Ник", speed=3)
        tournament = Tournament(90, usain, andrey, nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[0].name, "Усэйн")