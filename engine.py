class Engine:
    def __init__(self, user, window) -> None:
        self.user = user
        self.window = window
        self.current_word = ""

    def updateLabels(self):

        self.setLabelValue("center", self.current_word)
        self.setLabelValue("leftUp", self.user.level)
        self.setLabelValue("leftBottom", self.user.score)
        self.setLabelValue("rightUp", self.user.next_level)
        self.setLabelValue("rightBottom", self.user.day_counter)

    def handleKeyPress(self, event):
        # Update the player
        self.update()
        key = event.name
        record = f"Key: {key}"
        if key == "space" or key == "backspace" or key == "enter":
            self.handle_score()
            
        else:
            self.current_word += key
        print(record)
        # Set the key to a value


    def handle_score(self):
        if len(self.current_word) >= 2:
            print("word is longer thgan 2")
            self.user.add_score()
            self.current_word = ""
    
    def update(self):
        self.updateLabels()
        self.user.update_user()
        
        
    
    
    def setLabelValue(self, position="leftUp", target="text here"):
        target_str = str(target)
        if position == "leftUp":
            self.window.label1.setText("LEVEL " + target_str)
        
        elif position == "leftBottom":
            self.window.label2.setText("SCORE " + target_str)

        elif position == "center":
            self.window.big_label.setText(target_str)
        
        elif position == "rightUp":
            self.window.label3.setText("NEXT LEVEL " + target_str)
        
        elif position == "rightBottom":
            self.window.label4.setText( "DAY " + target_str)

