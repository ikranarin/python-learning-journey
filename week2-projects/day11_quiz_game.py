import tkinter as tk
import random
import json
import os

# ---------------- DATA ----------------
questions = {
    "easy": [
        {"q": "Python'da liste?", "options": ["()", "{}", "[]", "<>"], "a": "[]"},
        {"q": "print() ne yapar?", "options": ["Yazdırır", "Sil", "Açar", "Kapattırır"], "a": "Yazdırır"}
    ],
    "medium": [
        {"q": "Fonksiyon tanımı?", "options": ["fun", "def", "function", "define"], "a": "def"},
        {"q": "Hangisi döngü?", "options": ["if", "for", "class", "int"], "a": "for"}
    ],
    "hard": [
        {"q": "JSON ne için?", "options": ["Oyun", "Veri saklama", "Grafik", "Ses"], "a": "Veri saklama"},
        {"q": "list comprehension nedir?", "options": ["Loop kısa yolu", "Hata", "Tip", "Fonksiyon"], "a": "Loop kısa yolu"}
    ]
}

FILE = "quiz_score.json"


# ---------------- SCORE ----------------
def load_score():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {"highscore": 0}


def save_score(score):
    with open(FILE, "w") as f:
        json.dump({"highscore": score}, f)


# ---------------- APP ----------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.score_data = load_score()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.show_menu()

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def show_menu(self):
        self.clear()

        tk.Label(self.frame, text="QUIZ GAME", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.frame, text=f"High Score: {self.score_data['highscore']}").pack()

        tk.Button(self.frame, text="Easy", width=20, command=lambda: self.start("easy")).pack(pady=5)
        tk.Button(self.frame, text="Medium", width=20, command=lambda: self.start("medium")).pack(pady=5)
        tk.Button(self.frame, text="Hard", width=20, command=lambda: self.start("hard")).pack(pady=5)

    def start(self, level):
        self.questions = questions[level][:]
        random.shuffle(self.questions)
        self.index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear()

        if self.index >= len(self.questions):
            self.show_result()
            return

        q = self.questions[self.index]

        tk.Label(self.frame, text=q["q"], wraplength=300).pack(pady=10)

        for option in q["options"]:
            tk.Button(
                self.frame,
                text=option,
                width=25,
                command=lambda opt=option: self.check(opt)
            ).pack(pady=3)

    def check(self, answer):
        correct = self.questions[self.index]["a"]

        if answer == correct:
            self.score += 1

        self.index += 1
        self.show_question()

    def show_result(self):
        self.clear()

        tk.Label(self.frame, text=f"Score: {self.score}", font=("Arial", 16)).pack(pady=10)

        if self.score > self.score_data["highscore"]:
            save_score(self.score)
            tk.Label(self.frame, text="NEW HIGH SCORE! 🔥").pack()

        tk.Button(self.frame, text="Menu", command=self.show_menu).pack(pady=10)


# ---------------- RUN ----------------
root = tk.Tk()
app = QuizApp(root)
root.mainloop()