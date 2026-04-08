# Python Learning Journey

This repository documents my progress while learning Python step by step. Each day includes small exercises and mini projects.
## Week 1 – Python Basics

In the first week of my Python learning journey, I focused on fundamental programming concepts and built several small programs to practice them.

### Topics Covered
- Variables and data types
- User input
- Arithmetic operations
- Conditional statements (if, elif, else)
- Logical operators (and, or, not)
- For loops
- While loops

### Mini Programs
- User input and variable examples
- Simple calculator
- Even / Odd number checker
- Grade evaluation system
- Login system
- Multiplication table generator
- Number guessing game
- Password verification program
- ATM simulation project

### Files
- `day1_variables.py`
- `day2_math.py`
- `day3_conditions.py`
- `day4_login_system.py`
- `day5_loops.py`
- `day6_while_loops.py`
- `day7_atm_simulation.py`

This week helped me understand the core logic of programming in Python and build my first mini console applications.

## Week 2 – Mini Projects

### Day 8 – To-Do List Application

In this project, I built a console-based To-Do List application using Python. The program allows users to manage their tasks through a simple menu system.

#### Features
- View all tasks
- Add new tasks
- Mark tasks as completed
- Remove tasks
- Save tasks to a JSON file so they persist after the program closes

#### Concepts Practiced
- Lists and dictionaries
- Loops and conditional statements
- File handling
- JSON data storage
- Basic application structure

#### File
- `day8_todo_app.py`

### Day 9 – Password Generator
A Python program that generates secure random passwords based on user preferences.

**Features**
- User chooses password length
- Generate multiple passwords at once
- Ensures each password contains letters, numbers, and symbols
- Randomly shuffles characters for stronger security
- Option to save generated passwords to a file

**Concepts Practiced**
- Random module
- String module
- Lists and loops
- File writing
- Basic security logic

**File**
- `day9_password_generator.py`

### Day 10 – Ultra Guessing Game

An advanced terminal-based number guessing game with enhanced features.

**Features**
- Player Mode with scoring system  
- AI Mode (computer guesses your number)  
- Persistent stats: wins, losses, high score (saved in `game_data.json`)  
- Advanced hint system (very close, close, far)  
- Replayable, modular structure  

**Concepts Practiced**
- Loops and conditional logic  
- Functions and modular code  
- Random number generation  
- File handling and JSON persistence  
- Basic AI (binary search strategy)  
- Game design and user interaction  

**Files**
- `day10_guessing_game.py`  
- `game_data.json` (created automatically to store high score and stats)

### Day 11 – Quiz Game (GUI)

In this project, I built a graphical quiz game using Python and Tkinter. The application allows users to answer multiple-choice questions with different difficulty levels.

#### Features
- Graphical user interface (GUI) using Tkinter
- Multiple difficulty levels (Easy, Medium, Hard)
- Randomized questions
- Score tracking system
- High score saved to a JSON file
- Interactive buttons for user input

#### Concepts Practiced
- GUI development with Tkinter
- Object-oriented programming (OOP)
- Event-driven programming
- Lists and dictionaries
- File handling and JSON storage
- Randomization

#### Files
- `day11_quiz_game.py`
- `quiz_score.json` (stores high score)


### Day 12 – File Organizer

In this project, I developed a Python script that automatically organizes files in a selected folder based on their file types.

#### Features
- Scans a given directory
- Automatically creates folders by file type (images, documents, videos, etc.)
- Moves files into appropriate folders
- Handles unknown file types by placing them into an "others" folder

#### Concepts Practiced
- Working with the OS module
- File and directory management
- Automation scripts
- Using shutil for file operations
- Real-world problem solving

#### File
- `day12_file_organizer.py`

### Day 13 – Pomodoro Timer

In this project, I built a real-time Pomodoro timer that helps manage study and break sessions using the Pomodoro technique.

#### Features
- Work and break timer system (25/5 minutes)
- Real-time countdown display
- Automatic transition between work and break sessions
- Continuous cycle option

#### Concepts Practiced
- Time module usage
- Countdown logic
- While loops and control flow
- Real-time terminal output

#### File
- `day13_pomodoro_timer.py`


### Day 14 – Expense Tracker

In this project, I developed a console-based expense tracking application to manage daily spending.

#### Features
- Add and store expenses
- Categorize expenses (food, transport, etc.)
- View all expenses
- Calculate total spending
- Category-based summary
- Data persistence using JSON

#### Concepts Practiced
- Lists and dictionaries
- File handling and JSON storage
- Data aggregation and analysis
- User input handling
- Basic financial logic

#### Files
- `day14_expense_tracker.py`
- `expenses.json` (stores expense data)