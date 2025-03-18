import random


def guess_the_number():
    print("🎮 بازی حدس عدد 🎮")
    print("یک عدد بین ۱ تا ۱۰۰ انتخاب شده، آن را حدس بزن!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("حدس بزن (۱ تا ۱۰۰): "))
            attempts += 1

            if guess < secret_number:
                print("🔻 عدد بزرگ‌تر است!")
            elif guess > secret_number:
                print("🔺 عدد کوچک‌تر است!")
            else:
                print(
                    f"🎉 تبریک! عدد {secret_number} را در {attempts} تلاش حدس زدی!")
                break
        except ValueError:
            print("⚠️ لطفاً یک عدد معتبر وارد کن.")


if __name__ == "__main__":
    guess_the_number()
