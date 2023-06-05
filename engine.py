from settings import *
import json


class Engine:
    def __init__(self, user, window) -> None:
        self.user = user
        self.window = window
        self.current_word = ""
        self.settings = None
        load_read_save_JSON('user_settings.json', self, "user")
        self.load_user()
        
    def load_user(self):
        self.user.level = self.settings['level']
        self.user.score = self.settings['score']
        self.user.next_level = self.settings['next_level']
        self.user.next_event = self.settings['next_event']
        self.user.day_counter = self.settings['day']
        print("[ENGINE-USER] - USER LOADED")
    
    def save_user(self):
        if self.settings != None:
            print("[ENGINE-USER] - SAVING USER...")
            with open('user_settings.json', 'w') as file:
                json.dump(self.settings, file, indent=4)
                print("[ENGINE-FILE] - USER SAVED")


    def updateLabels(self):
        self.setLabelValue("center", "",self.window.timer)
        self.setLabelValue("leftUp", "LEVEL: ",self.user.level)
        self.setLabelValue("leftBottom", "SCORE: ",self.user.score)
        self.setLabelValue("rightUp", "NEXT LVL: ",self.user.next_level)
        self.setLabelValue("rightBottom", "DAY: ",self.user.day_counter)

    def handleKeyPress(self, event):
        # Update the player
        self.update()
        key = event.name
        record = f"Key: {key}"
        if key == "space" or key == "backspace" or key == "enter":
            self.handle_score()
            
        else:
            self.current_word += key
        # Set the key to a value


    def handle_score(self):
        if len(self.current_word) >= 2:
            self.user.add_score()
            self.current_word = ""
    
    def update(self):
        self.updateLabels()
        self.user.update_user()
        
        
    
    
    def setLabelValue(self, position="leftUp",label_text="",target="text here"):
        target_str = str(target)
        if position == "leftUp":
            self.window.label1.setText(label_text + target_str)
        
        elif position == "leftBottom":
            self.window.label2.setText(label_text + target_str)

        elif position == "center":
            self.window.big_label.setText(label_text + target_str)
        
        elif position == "rightUp":
            self.window.label3.setText(label_text + target_str)
        
        elif position == "rightBottom":
            self.window.label4.setText(label_text + target_str)
    
    def timer_logic(self):
        print("[ENGINE-TIMER] - UPDATE")
        self.updateLabels()
        if int(self.window.last_save) > 10:
            self.save_user()
            self.window.last_save = 0

def load_read_save_JSON(path, consumer_self, property="user"):
    target_file = open(path)
    data = json.load(target_file)
    consumer_self.settings = data[property]
    print(consumer_self.settings)
    target_file.close()

