import random

questions = [
    {
        "question": "Python'da liste oluşturmak için hangisi kullanılır?",
        "options": ["()", "{}", "[]", "<>"],
        "answer": "[]"
    },
    {
        "question": "Hangisi bir döngüdür?",
        "options": ["if", "for", "def", "print"],
        "answer": "for"
    },
    {
        "question": "Python'da fonksiyon nasıl tanımlanır?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Hangisi veri tipi değildir?",
        "options": ["int", "str", "loop", "list"],
        "answer": "loop"
    },
    {
        "question": "print() ne yapar?",
        "options": ["Girdi alır", "Ekrana yazdırır", "Dosya açar", "Silme yapar"],
        "answer": "Ekrana yazdırır"
    }
]


def run_quiz():
    score = 0
    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])

        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Cevabın (1-4): "))
            selected = q["options"][choice - 1]

            if selected == q["answer"]:
                print("Doğru!")
                score += 1
            else:
                print(f"Yanlış! Doğru cevap: {q['answer']}")
        except:
            print("Geçersiz giriş.")

    print(f"\nSkorun: {score}/{len(questions)}")

    if score == len(questions):
        print("Mükemmel! 🔥")
    elif score >= len(questions) // 2:
        print("İyi iş 👍")
    else:
        print("Daha çok çalış 😄")


def main():
    while True:
        print("\n--- QUIZ GAME ---")
        print("1. Başla")
        print("2. Çıkış")

        choice = input("Seç: ")

        if choice == "1":
            run_quiz()
        elif choice == "2":
            print("Görüşürüz!")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()