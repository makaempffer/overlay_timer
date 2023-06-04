from settings import MAX_DAY

class User:
    def __init__(self):
        self.level = 0
        self.score = 0
        self.dayTimer = MAX_DAY
        self.next_level = 10
        self.last_level = 0
        self.next_event = 100
        self.max_day = MAX_DAY
        self.day_counter = 0
    
    def calculate_next_level(self):
        self.dayTimer += 1
        if self.score >= self.next_level:
            self.last_level = self.level
            self.next_level = self.score * 1.77
            self.level += 1
        
        if self.dayTimer >= self.max_day:
            self.day_counter += 1
            self.dayTimer = 0
        

    
    def add_score(self):
        print(self.score)
        self.score += 1
    
    def update_user(self):
        self.calculate_next_level()

    
        
