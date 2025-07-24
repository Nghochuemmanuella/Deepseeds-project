import random

ascii_art_diagram = [...]

story_prompts = [...]


while True:
    user_input = input("\n Type 'draw', 'write', or 'exit': ").strip().lower()
    
    if user_input == "exit":
        print("Goodbye")
        break
    elif user_input.startswith("draw"):
        selected_art = random.choice(ascii_art_diagram)
        print("\n Here is your randam ASCII drawing: ")
        print(selected_art)
    elif user_input.startswith("write"):
        selected_prompts = random.choice(story_prompts)
        print("\n Here is your randam ASCII prompt: ")
        print(selected_prompts)
        
    else:
        print("invalid command. try 'draw', 'wrrite', or 'exit'")
        