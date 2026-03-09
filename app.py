from flask import Flask, render_template, abort

app = Flask(__name__)

BOOK_PAGES = [
    {
        "number": 1,
        "title": "Meet Pip the Programmer!",
        "emoji": "👧",
        "color": "#FFD700",
        "bg_color": "#FFF9C4",
        "content": (
            "Once upon a time, in a cozy little town, lived a curious girl named Pip. "
            "Pip loved to figure out how things worked — clocks, toys, even toasters!"
        ),
        "story": (
            "One day, Pip found a magical laptop glowing under her bed. "
            "On the screen were these words: <em>\"Hello! I am Python. I can help you talk to computers!\"</em>"
        ),
        "lesson_title": "What is Programming?",
        "lesson": (
            "Programming is giving instructions to a computer. "
            "Just like telling a friend step-by-step how to make a sandwich, "
            "we write steps (called <strong>code</strong>) for the computer to follow."
        ),
        "code_example": 'print("Hello, World!")',
        "code_result": 'Hello, World!',
        "fun_fact": "Python was named after Monty Python, a funny comedy show — not the snake! 🐍",
    },
    {
        "number": 2,
        "title": "Treasure Boxes — Variables!",
        "emoji": "📦",
        "color": "#FF8C00",
        "bg_color": "#FFF3E0",
        "content": (
            "Pip wanted to remember things. "
            "Python showed her magical treasure boxes called <strong>variables</strong>!"
        ),
        "story": (
            "\"Think of a variable like a labelled box,\" said Python. "
            "\"Put anything inside — a name, a number, even a whole sentence!\" "
            "Pip grabbed a box, wrote <em>my_name</em> on it, and popped her name inside."
        ),
        "lesson_title": "What is a Variable?",
        "lesson": (
            "A <strong>variable</strong> is a name that stores a value. "
            "You can put numbers, words, or True/False into a variable. "
            "Whenever you need that value, just use the variable's name!"
        ),
        "code_example": (
            'my_name = "Pip"\n'
            'my_age = 8\n'
            'print(my_name)\n'
            'print(my_age)'
        ),
        "code_result": "Pip\n8",
        "fun_fact": "Variable names can't have spaces. Use an underscore _ instead, like my_name! 🏷️",
    },
    {
        "number": 3,
        "title": "Words and Numbers — Strings & Integers!",
        "emoji": "🔢",
        "color": "#4CAF50",
        "bg_color": "#E8F5E9",
        "content": (
            "Python told Pip: \"There are different kinds of things you can store. "
            "Words are called <strong>strings</strong>, and whole numbers are called <strong>integers</strong>!\""
        ),
        "story": (
            "Pip tried storing her favourite animal: <em>\"cat\"</em>. "
            "Then she stored the number of cats she had: <em>3</em>. "
            "\"Can I join words together?\" she asked. "
            "\"Of course!\" said Python. \"That's called <em>concatenation</em>!\""
        ),
        "lesson_title": "Strings and Integers",
        "lesson": (
            "A <strong>string</strong> is text wrapped in quotes: <code>\"hello\"</code>. "
            "An <strong>integer</strong> is a whole number like <code>5</code> or <code>100</code>. "
            "You can join strings with <code>+</code> and do maths with integers!"
        ),
        "code_example": (
            'animal = "cat"\n'
            'num_cats = 3\n'
            'print("I have " + str(num_cats) + " " + animal + "s")'
        ),
        "code_result": "I have 3 cats",
        "fun_fact": "To join a number to a string, use str() to turn the number into text first! 🔤",
    },
    {
        "number": 4,
        "title": "Decisions, Decisions — If & Else!",
        "emoji": "🤔",
        "color": "#9C27B0",
        "bg_color": "#F3E5F5",
        "content": (
            "One morning, Pip woke up and wondered: <em>\"Should I bring an umbrella today?\"</em> "
            "Python smiled. \"Let me teach you how computers make decisions — with <strong>if</strong> and <strong>else</strong>!\""
        ),
        "story": (
            "\"If it is raining, bring an umbrella. Otherwise, wear sunglasses,\" explained Python. "
            "\"Computers think the same way! You just need to write it in code.\""
        ),
        "lesson_title": "If and Else",
        "lesson": (
            "An <strong>if</strong> statement checks whether something is true. "
            "If it <em>is</em> true, it runs one set of steps. "
            "If it is <em>not</em> true, the <strong>else</strong> part runs instead."
        ),
        "code_example": (
            'is_raining = True\n\n'
            'if is_raining:\n'
            '    print("Bring an umbrella! ☔")\n'
            'else:\n'
            '    print("Wear sunglasses! 😎")'
        ),
        "code_result": "Bring an umbrella! ☔",
        "fun_fact": "Python uses indentation (spaces) to know what belongs inside an if statement! 📐",
    },
    {
        "number": 5,
        "title": "Do It Again — Loops!",
        "emoji": "🔄",
        "color": "#2196F3",
        "bg_color": "#E3F2FD",
        "content": (
            "Pip wanted to say \"Good morning!\" to all five of her friends. "
            "\"That's a lot of typing,\" she groaned. "
            "Python laughed. \"Let me introduce you to <strong>loops</strong> — the lazy programmer's best friend!\""
        ),
        "story": (
            "\"A loop does the same thing over and over,\" said Python. "
            "\"Instead of writing the same line five times, write it once and tell the loop how many times to repeat it!\" "
            "Pip's eyes lit up. \"That's amazing!\""
        ),
        "lesson_title": "For Loops",
        "lesson": (
            "A <strong>for loop</strong> repeats steps a set number of times. "
            "<code>range(5)</code> counts from 0 to 4, giving you 5 turns. "
            "Each turn, the variable (<code>i</code>) holds the current count."
        ),
        "code_example": (
            'friends = ["Alice", "Bob", "Carlos", "Dana", "Eve"]\n\n'
            'for friend in friends:\n'
            '    print("Good morning, " + friend + "!")'
        ),
        "code_result": (
            "Good morning, Alice!\n"
            "Good morning, Bob!\n"
            "Good morning, Carlos!\n"
            "Good morning, Dana!\n"
            "Good morning, Eve!"
        ),
        "fun_fact": "Computers can run a loop millions of times in one second — much faster than Pip! ⚡",
    },
    {
        "number": 6,
        "title": "Magic Spells — Functions!",
        "emoji": "🪄",
        "color": "#F44336",
        "bg_color": "#FFEBEE",
        "content": (
            "Pip noticed she kept writing the same greeting code over and over. "
            "\"There must be a better way!\" she said. "
            "Python nodded. \"There is — it's called a <strong>function</strong>. Think of it as a magic spell you name and cast whenever you need it!\""
        ),
        "story": (
            "Pip wrote her greeting spell, named it <em>greet</em>, and cast it on all her friends. "
            "Each time she used the spell, the computer ran all the steps inside — instantly! "
            "\"This is like having a robot do my chores,\" Pip giggled."
        ),
        "lesson_title": "Functions",
        "lesson": (
            "A <strong>function</strong> is a named block of reusable code. "
            "Use <code>def</code> to define it, give it a name, and add parentheses. "
            "Call it by writing its name followed by <code>()</code>."
        ),
        "code_example": (
            'def greet(name):\n'
            '    print("Hello, " + name + "! 👋")\n\n'
            'greet("Pip")\n'
            'greet("Python")'
        ),
        "code_result": "Hello, Pip! 👋\nHello, Python! 👋",
        "fun_fact": "Functions can take inputs (called parameters) and give back results (called return values)! 📤",
    },
    {
        "number": 7,
        "title": "Collect Them All — Lists!",
        "emoji": "📋",
        "color": "#00BCD4",
        "bg_color": "#E0F7FA",
        "content": (
            "Pip had so many favourite colours she couldn't keep track! "
            "\"Put them in a <strong>list</strong>!\" said Python. "
            "\"A list holds many things together, in order, like a shopping list.\""
        ),
        "story": (
            "Pip wrote down all her colours. "
            "She could add new ones, remove old ones, and look up any colour by its position. "
            "\"The first item is always number zero,\" Python reminded her. "
            "Pip scratched her head. \"Zero? That's a funny way to count!\""
        ),
        "lesson_title": "Lists",
        "lesson": (
            "A <strong>list</strong> holds many values in order, inside square brackets <code>[]</code>. "
            "Each item has a position called an <strong>index</strong>. "
            "Python starts counting at <strong>0</strong>, so the first item is at index 0."
        ),
        "code_example": (
            'colours = ["red", "yellow", "blue", "green"]\n\n'
            'print(colours[0])   # first item\n'
            'print(colours[2])   # third item\n'
            'colours.append("purple")\n'
            'print(colours)'
        ),
        "code_result": (
            "red\n"
            "blue\n"
            "['red', 'yellow', 'blue', 'green', 'purple']"
        ),
        "fun_fact": "Lists can hold strings, numbers, or even other lists — lists inside lists! 🗂️",
    },
    {
        "number": 8,
        "title": "You Are a Programmer!",
        "emoji": "🎉",
        "color": "#FF4081",
        "bg_color": "#FCE4EC",
        "content": (
            "Pip had learnt so much! Variables, strings, if/else, loops, functions, and lists. "
            "\"Am I a real programmer now?\" she asked Python. "
            "Python beamed. \"You absolutely are! Every expert was once a beginner.\""
        ),
        "story": (
            "That evening, Pip wrote her very first real program — a quiz game for her little brother. "
            "He laughed and played for hours. "
            "Pip smiled proudly and opened her laptop again. "
            "\"I wonder what I will build next,\" she whispered."
        ),
        "lesson_title": "What You Learned",
        "lesson": (
            "⭐ <strong>Variables</strong> — store values in named boxes.<br>"
            "⭐ <strong>Strings &amp; Integers</strong> — text and numbers.<br>"
            "⭐ <strong>If / Else</strong> — make decisions.<br>"
            "⭐ <strong>Loops</strong> — repeat steps automatically.<br>"
            "⭐ <strong>Functions</strong> — reusable blocks of code.<br>"
            "⭐ <strong>Lists</strong> — collect many values together."
        ),
        "code_example": (
            '# Pip\'s first quiz game\n'
            'answer = input("What is 2 + 2? ")\n\n'
            'if answer == "4":\n'
            '    print("Correct! You are a star! ⭐")\n'
            'else:\n'
            '    print("Nice try! The answer is 4.")'
        ),
        "code_result": "Correct! You are a star! ⭐",
        "fun_fact": "Keep practising! The best programmers write code every single day. 💻",
    },
]

TOTAL_PAGES = len(BOOK_PAGES)


@app.route("/")
def cover():
    return render_template("cover.html", total_pages=TOTAL_PAGES)


@app.route("/page/<int:page_number>")
def page(page_number):
    if page_number < 1 or page_number > TOTAL_PAGES:
        abort(404)
    page_data = BOOK_PAGES[page_number - 1]
    prev_page = page_number - 1 if page_number > 1 else None
    next_page = page_number + 1 if page_number < TOTAL_PAGES else None
    return render_template(
        "page.html",
        page=page_data,
        prev_page=prev_page,
        next_page=next_page,
        total_pages=TOTAL_PAGES,
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    import os
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
