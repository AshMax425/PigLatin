# Pig Latin Translator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A small Python program that converts English sentences into Pig Latin.

This repository contains a simple Pig Latin translator written for a class exercise. The script reads a sentence from the user, removes punctuation, and converts each word into Pig Latin before printing the result.

**Features**
- **Simple CLI**: Prompts the user for a sentence and prints Pig Latin output. 🐷
- **Punctuation-safe**: Strips punctuation before translation. ✂️
- **Handles words without vowels**: Appends `ay` when no vowel is present. 🔤
- **Vowel-first rule**: Adds `yay` when a word begins with a vowel. 🎵
- **Clear, single-file implementation**: Easy to read and modify. 📄

**Installation**
- **Prerequisites**: Python 3.8 or newer installed. Use `python --version` to check.
- Clone or download this repository into a directory on your machine.

Step-by-step (bash):

```bash
# clone (if applicable)
git clone https://github.com/AshMax425/PigLatin.git

# (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate 
source venv/Scripts/activate # on Windows

```

**Usage**

Quick start:

```bash
python PigLatinTranslator.py
# then type: Hello, world!
# Output: Your sentence in Pig Latin is: ellohay orldway
```

Code examples / common use cases:

Run interactively (default behavior)

```bash
python PigLatinTranslator.py
# Enter: This is a test.
# Output: Your sentence in Pig Latin is: isthay isyay ayay esttay
```


```

**API Overview**
- **`PigLatinTranslator.py`**: Single-file script used as a CLI. Contains `main()` which prompts for input, strips punctuation, converts words to Pig Latin, and prints the result.

Full documentation: This is a small class assignment; no separate docs are included.


**Contributing**
- Fork the repository, create a feature branch, and open a pull request. For small improvements (tests, refactor to expose `translate()`), include a short description and an example.

**Contact**
- **Name**: Ashley Maxam
- **Email**: s-ashley.maxam@lwtech.edu
- **Repository**: `https://github.com/AshMax425/PigLatin.git`
