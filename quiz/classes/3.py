class MyShape:
    def __init__(self, color="black", is_filled=True):
        self.color = color
        self.is_filled = is_filled
    
    def __str__(self):
        return f"Shape color: {self.color}, Filled: {self.is_filled}"
