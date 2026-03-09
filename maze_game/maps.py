
class Maps:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.map = []
    def generate_map(self, difficulty):
        if difficulty == 1:
            with open('easy.txt', 'r') as easy:
                for line in easy:
                    self.map.append(list(line))
        elif difficulty == 2:
            with open('medium.txt', 'r') as medium:
                for line in medium:
                    self.map.append(list(line))
        elif difficulty == 1:
            with open('hard.txt', 'r') as hard:
                for line in hard:
                    self.map.append(list(line))
        for line in map:
            if '\n' in line:
                line.remove('\n')
        
        
