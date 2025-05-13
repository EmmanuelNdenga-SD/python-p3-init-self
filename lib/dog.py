#!/usr/bin/env python3

# lib/dog.py

class Dog:
    def __init__(self, name, breed=None):
        self.name = name
        self.breed = breed if breed is not None else "Mutt"