# Common words mapped to single characters prefixed with underscore
word_mapping = {
    "the": "_a", 
    "and": "_b", 
    "say": "_c", 
    "she": "_d", 
    "her": "_e", 
    "that": "_f",
    "have": "_g", 
    "with": "_h", 
    "what": "_i", 
    "for": "_j", 
    "not": "_k", 
    "was": "_l",
    "very": "_m", 
    "Alice": "_n", 
    "thing": "_o", 
    "said": "_p", 
    "this": "_q", 
    "down": "_r",
    "you": "_s", 
    "how": "_t", 
    "but": "_u", 
    "from": "_v", 
    "went": "_w", 
    "get": "_x",
    "will": "_y", 
    "my": "_z", 
    "one": "_0", 
    "all": "_1", 
    "would": "_2", 
    "there": "_3",
    "their": "_4", 
    "if": "_5", 
    "about": "_6", 
    "which": "_7", 
    "out": "_8", 
    "so": "_9"
}

def compress_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            data = f_in.read()  # Read the input text
        
        compressed_data = ""
        word_buffer = ""
        for char in data:
            if char.isalpha(): # Since we're only compressing alphabetic characters
                word_buffer += char  # Build word character by character
            else:
                if word_buffer:
                    compressed_data += word_mapping.get(word_buffer, word_buffer)  # Replace common words with their mapped character or keep uncommon words as they are
                    word_buffer = ""
                compressed_data += char  # Add non-alphabetic characters as they are
        
        if word_buffer:
            compressed_data += word_mapping.get(word_buffer, word_buffer)  # Replace common words with their mapped character or keep uncommon words as they are
        
        with open(output_file, 'w') as f_out:
            f_out.write(compressed_data)  # Write compressed data
        
        print("File compressed successfully!")
    
    except FileNotFoundError:
        print("Input file not found.")

def decompress_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            compressed_data = f_in.read()  # Read the compressed data
        
        decompressed_data = ""
        word_buffer = ""
        for char in compressed_data:
            if char.isalpha() or char.isdigit() or char == "_":
                word_buffer += char  # Build word character by character
            else:
                if word_buffer:
                    for common_word, mapped_char in word_mapping.items():
                        if mapped_char == word_buffer:
                            decompressed_data += common_word  # Restore common words
                            break
                    else:
                        decompressed_data += word_buffer  # Keep mapped characters or uncommon words as they are
                    word_buffer = ""
                decompressed_data += char  # Add non-alphabetic characters as they are
        
        if word_buffer:
            for common_word, mapped_char in word_mapping.items():
                if mapped_char == word_buffer:
                    decompressed_data += common_word  # Restore common words
                    break
            else:
                decompressed_data += word_buffer  # Keep mapped characters or uncommon words as they are
        
        with open(output_file, 'w') as f_out:
            f_out.write(decompressed_data)  # Write decompressed data
        
        print("File decompressed successfully!")
    
    except FileNotFoundError:
        print("Input file not found.")

# Example usage:
input_file = 'example_original.txt'
compressed_file = 'example_compressed.txt'
decompressed_file = 'example_decompressed.txt'

# Compress file
compress_file(input_file, compressed_file)

# Decompress file
decompress_file(compressed_file, decompressed_file)