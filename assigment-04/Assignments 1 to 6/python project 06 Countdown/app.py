import time

def countdown_timer(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        # Timer format (05:34)
        timer = f'{mins:02}:{secs:02}'
        print(f"\r⏳ Timer: {timer}", end="")  # Timer display
        time.sleep(1)  # 1 second wait
        seconds -= 1  # Seconds decreament

    print("\n⏰ Time's up!")  # Timer end msg

try:
    total_seconds = int(input("Enter time in seconds for the countdown: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Please enter a valid number!")
