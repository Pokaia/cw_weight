import sys

# Morse code weights for each character
morse_weights = {
    'A': 1, 'B': 4, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 3, 'H': 4, 'I': 1, 'J': 5,
    'K': 2, 'L': 3, 'M': 3, 'N': 2, 'O': 3,
    'P': 3, 'Q': 5, 'R': 2, 'S': 3, 'T': 1,
    'U': 4, 'V': 5, 'W': 3, 'X': 5, 'Y': 5,
    'Z': 5, '0': 6, '1': 7, '2': 8, '3': 9,
    '4': 10, '5': 11, '6': 12, '7': 13, '8': 14,
    '9': 15, '.': 1, ',': 3, '?': 2, '!': 2,
    "'": 4, '/': 4, '(': 5, ')': 5, '&': 4,
    ':': 3, ';': 4, '=': 6, '+': 4, '-': 4,
    '_': 7, '"': 5, '$': 8, '@': 9
}

def calculate_cw_weight(input_text):
    total_weight = 0
    for char in input_text.upper():
        if char in morse_weights:
            total_weight += morse_weights[char]
    return total_weight

if __name__ == '__main__':
    input_text = sys.stdin.read().strip()
    weight = calculate_cw_weight(input_text)
    print(weight)
