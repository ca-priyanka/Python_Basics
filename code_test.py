def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
        
    pyramid_words = []
    for line in lines:
        number, word = line.split(maxsplit=1)
        pyramid_words.append(word.strip())
        
    decoded_message = " ".join(pyramid_words)
    return decoded_message

message_file_path = r'C:\Users\capri\Downloads\message_file.txt'
decoded_message = decode(message_file_path)
print(decoded_message)


def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Sort lines based on the numbers
    lines.sort(key=lambda x: int(x.split()[0]))

    pyramid_words = []
    for line in lines:
        number, word = line.split(maxsplit=1)
        pyramid_words.append(word.strip())

    decoded_message = " ".join(pyramid_words)
    return decoded_message

message_file_path = r'C:\Users\capri\Downloads\message_file.txt'
decoded_message = decode(message_file_path)
print(decoded_message)


def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    pyramid_numbers = [1, 3, 6]
    pyramid_words = []

    for line in lines:
        number, word = line.split(maxsplit=1)
        if int(number) in pyramid_numbers:
            pyramid_words.append(word.strip())

    decoded_message = " ".join(pyramid_words)
    return decoded_message

message_file_path = r'C:\Users\capri\Downloads\coding_qual_input.txt'
decoded_message = decode(message_file_path)
print(decoded_message)


def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    pyramid_numbers = [1, 3, 6]
    pyramid_words = []

    for line in lines:
        number, word = line.split(maxsplit=1)
        if int(number) in pyramid_numbers:
            pyramid_words.append(word.strip())

    decoded_message = " ".join(pyramid_words)
    return decoded_message

message_file_path = r'C:\Users\capri\Downloads\coding_qual_input.txt'
decoded_message = decode(message_file_path)
print(decoded_message)

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    pyramid_numbers = [1, 3, 6]
    pyramid_words = []

    for line in lines:
        number, word = line.split(maxsplit=1)
        if int(number) in pyramid_numbers:
            pyramid_words.append(word.strip())

    # Sort the pyramid_words based on the pyramid_numbers
    pyramid_words.sort(key=lambda x: pyramid_numbers.index(int(x.split()[0])))

    decoded_message = " ".join(pyramid_words)
    return decoded_message

message_file_path = r'C:\Users\capri\Downloads\coding_qual_input.txt'
decoded_message = decode(message_file_path)
print(decoded_message)
