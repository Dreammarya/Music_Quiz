print("🎶 Fill-in the blank Lyrics! 🎵")
print("🤔 Can you guess the missing words? Let's find out!\n")

songs = [
    {"lyrics": "Never going to ___ you up.", "word": "give", "artist": "Rick Astley"},
    {"lyrics": "We will, we will ___!", "word": "rock", "artist": "Queen"},
    {"lyrics": "Is this the real ___?", "word": "life", "artist": "Queen (Bohemian Rhapsody)"},
    {"lyrics": "I got a feeling that tonight's going to be a good ___.", "word": "night", "artist": "The Black Eyed Peas"},
    {"lyrics": "Let it ___, let it ___!", "word": "go", "artist": "Idina Menzel (Frozen)"},
    {"lyrics": "Hit me baby one more ___!", "word": "time", "artist": "Britney Spears"},
    {"lyrics": "Oops!... I did it ___!", "word": "again", "artist": "Britney Spears"},
]

for song in songs:
    while True:
        print(f"   {song['lyrics']} (Artist: {song['artist']}) 🎤")
        missed_word = input("What is the missing word? ").lower()
        if missed_word != song["word"].lower():
            print("❌ Nope, try again!")
        else:
            print("🎉 Yes, Bingo! 😊")
            break  

print("\n🎊 Great job! You guessed all the lyrics! 🥳")
