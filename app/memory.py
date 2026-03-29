class Memory:
    def __init__(self, max_history=5):
        self.history = []
        self.max_history = max_history

    def add(self, user, assistant):
        self.history.append((user, assistant))
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_context(self):
        context = ""
        for u, a in self.history:
            context += f"User: {u}\nAssistant: {a}\n"
        return context