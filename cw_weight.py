import sys

# Morse code weights for each character
# Add comments to these CW (Morse code weights) to show the . - symbols for each character. AI!
morse_weights = {
    'A': 5,
    'B': 9,
    'C': 11,
    'D': 7,
    'E': 1,
    'F': 9,
    'G': 9,
    'H': 7,
    'I': 3,
    'J': 13,
    'K': 9,
    'L': 9,
    'M': 7,
    'N': 5,
    'O': 11,
    'P': 11,
    'Q': 13,
    'R': 7,
    'S': 5,
    'T': 3,
    'U': 7,
    'V': 9,
    'W': 9,
    'X': 11,
    'Y': 13,
    'Z': 11,
    '0': 19,
    '1': 17,
    '2': 15,
    '3': 13,
    '4': 11,
    '5': 9,
    '6': 11,
    '7': 13,
    '8': 15,
    '9': 17,
}

def calculate_cw_weight(input_text):
    total_weight = 0
    for char in input_text.upper():
        if char in morse_weights:
            total_weight += morse_weights[char]
        total_weight += 3
    return total_weight

if __name__ == '__main__':
    input_text = sys.stdin.read().strip()
    weight = calculate_cw_weight(input_text)
    print(weight)
