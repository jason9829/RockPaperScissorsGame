import unittest
from unittest.mock import patch
from rockpaperscissors import verifyUserPlayOption
from rockpaperscissors import isTheGameTied
from rockpaperscissors import gameNotTiedHandler


# Added alphabet because the test run in alphabetical order (a-first to z-last)
class TestverifyUserPlayOption(unittest.TestCase):
    def test_e_verifyUserPlayOption_given_rock_expect_rock(self):
        # The function will return "Rock", "Paper", "Scissors" (case-insenstive)
        # if the argument spelling fall under these threee terms else
        # it will return invalid
        #               (EXPECTED, ACTUAL)
        self.assertEqual("rock", verifyUserPlayOption("rock"))

    def test_f_verifyUserPlayOption_given_PaPer_expect_PaPer(self):
        # The function will return "Rock", "Paper", "Scissors" (case-insenstive)
        # if the argument spelling fall under these threee terms else
        # it will return invalid
        #               (EXPECTED, ACTUAL)
        self.assertEqual("PaPer", verifyUserPlayOption("PaPer"))

    def test_g_verifyUserPlayOption_given_SciSSORs_expect_SciSSORs(self):
        # The function will return "Rock", "Paper", "Scissors" (case-insenstive)
        # if the argument spelling fall under these threee terms else
        # it will return false
        #               (EXPECTED, ACTUAL)
        self.assertEqual("SciSSORs", verifyUserPlayOption("SciSSORs"))

    def test_h_verifyUserPlayOption_given_Apple_expect_false(self):
        # The function will return "Rock", "Paper", "Scissors" (case-insenstive)
        # if the argument spelling fall under these threee terms else
        # it will return false
        #               (EXPECTED, ACTUAL)
        self.assertEqual(False, verifyUserPlayOption("Apple"))


class TestisTheGameTied(unittest.TestCase):
    def test_i_isTheGameTied_given_paper_and_paper_expect_True(self):
        # The function will return True if the play options between player
        # and computer are the same else it will return false (case-insensitive)
        #               (EXPECTED, ACTUAL)
        self.assertEqual(True, isTheGameTied("paper", "paper"))

    def test_j_isTheGameTied_given_RoCk_and_rOcK_expect_True(self):
        # The function will return True if the play options between player
        # and computer are the same else it will return false (case-insensitive)
        #               (EXPECTED, ACTUAL)
        self.assertEqual(True, isTheGameTied("RoCk", "rOcK"))

    def test_k_isTheGameTied_given_SCISSORs_and_ApplE_expect_False(self):
        # The function will return True if the play options between player
        # and computer are the same else it will return false (case-insensitive)
        #               (EXPECTED, ACTUAL)
        self.assertEqual(False, isTheGameTied("SCISSORs", "ApplE"))

    def test_l_isTheGameTied_given_paper_and_random_symbol_expect_False(self):
        # The function will return True if the play options between player
        # and computer are the same else it will return false (case-insensitive)
        #               (EXPECTED, ACTUAL)
        self.assertEqual(False, isTheGameTied("paper", "!@#&*^*()()_%%"))


class TestgameNotTiedHandler(unittest.TestCase):
    def test_m_gameNotTiedHandler_given_paper_and_scissors_expect_you_lose_message(self):
        # Player    : Paper
        # Computer  : Scissors
        # Message   : You lose! Scissors beats Paper.
        #               (EXPECTED, ACTUAL)                                   (User, Computer)
        self.assertEqual("You lose! Scissors beats Paper.", gameNotTiedHandler("paper", "scissors"))

    def test_n_gameNotTiedHandler_given_pAPeR_and_RocK_expect_you_lose_message(self):
        # Player    : pAPeR
        # Computer  : RocK
        # Message   : "You win! Paper beats Rock."
        #               (EXPECTED, ACTUAL)                                   (User, Computer)
        self.assertEqual("You win! Paper beats Rock.", gameNotTiedHandler("pAPeR", "RocK"))


if __name__ == '__main__':
    unittest.main()
