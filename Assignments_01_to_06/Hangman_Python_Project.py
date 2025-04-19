import random
import string

words = [
    "python", "variable", "function", "loop", "string", "integer", "boolean", "syntax",
    "operator", "condition", "debug", "compile", "execute", "parameter", "argument",
    "recursion", "exception", "library", "module", "package", "framework", "object",
    "class", "method", "inheritance", "encapsulation", "polymorphism", "abstraction",
    "algorithm", "array", "list", "tuple", "dictionary", "set", "stack", "queue",
    "binary", "search", "sort", "merge", "quick", "bubble", "hashmap", "graph",
    "tree", "node", "edge", "vertex", "matrix", "pointer", "memory", "compile",
    "interpreter", "constant", "keyword", "input", "output", "debugger", "source",
    "index", "element", "command", "argument", "file", "stream", "network", "socket",
    "thread", "process", "server", "client", "request", "response", "router",
    "protocol", "secure", "encrypt", "decrypt", "access", "control", "admin",
    "user", "login", "logout", "session", "cookie", "token", "backend", "frontend",
    "database", "schema", "query", "table", "column", "row", "relation", "join",
    "model", "view", "controller", "render", "route", "url", "form", "submit",
    "validate", "error", "exception", "try", "catch", "finally", "assert", "test",
    "mock", "unit", "integration", "deploy", "build", "branch", "commit", "merge",
    "push", "pull", "clone", "repository", "version", "history", "debug", "log",
    "config", "setup", "install", "uninstall", "update", "upgrade", "virtual",
    "environment", "shell", "terminal", "command", "prompt", "execute", "script",
    "automation", "schedule", "event", "trigger", "listener", "handler", "object",
    "attribute", "property", "instance", "static", "private", "public", "protected"
]


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives to complete your word, You used these letters :", " ".join(used_letters))

        word_list = [letters if letters in used_letters else "-" for letters in word]
        print("Current Word "," ".join(word_list))

        user_letters = input("Guess a letter : ").upper()
        if user_letters in alphabets - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

            else:
                lives -= 1
                print("Letter is not in the user word")

        elif user_letters in used_letters:
            print("You already used this character. Please try again")
            
        else:
            print("Invalid Character.") 

    if lives == 0:
        print("Sorry, You died. The word was ",word ,'!!')
    else:
        print("Congrats, You Guessed the word Correctly  ", word, " In ",lives)
 



hangman()
