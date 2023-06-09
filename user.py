from settings import MAX_DAY

class User:
    def __init__(self):
        self.level = 0
        self.score = 0
        self.day_timer = MAX_DAY
        self.next_level = 10
        self.last_level = 0
        self.next_event = 100
        self.max_day = MAX_DAY
        self.day_counter = 0
        self.total_score = 0
    
    def calculate_next_level(self):
        print(self.level)
        if int(self.score) > int(self.next_level):
            self.score = 0
            self.last_level = self.level
            self.next_level = self.next_level * 1.25
            self.level += 1
        
        if self.day_timer >= self.max_day:
            self.day_counter += 1
            self.day_timer = 0
        

    
    def add_score(self):
        self.score += 1
        self.total_score += 1
    
    def update_user(self):
        self.calculate_next_level()

    
        
