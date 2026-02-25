import random

EASY_QUESTIONS = [
    ("2 + 2 = ?", 4),
    ("5 - 3 = ?", 2),
    ("3 + 4 = ?", 7),
    ("10 - 6 = ?", 4),
]

MEDIUM_QUESTIONS = [
    ("12 + 15 = ?", 27),
    ("20 - 8 = ?", 12),
    ("6 * 7 = ?", 42),
    ("36 / 4 = ?", 9),
]

HARD_QUESTIONS = [
    ("15 * 3 - 7 = ?", 38),
    ("144 / 12 = ?", 12),
    ("Square root of 81 = ?", 9),
    ("25% of 200 = ?", 50),
]

class Monster:
    def __init__(self, position, difficulty):
        self.position = position
        self.difficulty = int(difficulty)
        self.question = ""
        self.correct_answer = None
        self.is_defeated = False
        self.generate_question()
    
    def generate_question(self):
        if self.difficulty == 1:
            self.question, self.correct_answer = random.choice(EASY_QUESTIONS)
        elif self.difficulty == 2:
            self.question, self.correct_answer = random.choice(MEDIUM_QUESTIONS)
        elif self.difficulty == 3:
            self.question, self.correct_answer = random.choice(HARD_QUESTIONS)
    
    def ask_question(self):
        print(f"Монстр спрашивает: {self.question}")
    
    def check_answer(self, player_answer):
        if player_answer == self.correct_answer:
            self.is_defeated = True
            print("Победа!")
            return True
        else:
            print("ПОТРАЧЕНО")
            return False
            