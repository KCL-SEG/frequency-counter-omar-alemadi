"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        key = str(item) if not isinstance(item, str) else item
        frequencies[key] = frequencies.get(key, 0) + 1
    
    return frequencies
