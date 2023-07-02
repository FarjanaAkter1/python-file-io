
import re

def find_heritability_words(file_path, output_file_path):
    """
    Find heritability-related words in a text file and write occurrences to a new file.

    Args:
        file_path (str): Path to the input file.
        output_file_path (str): Path to the output file.
    """
    pattern = r'\b(herit(ab(le)?)?|inherit(ance)?|heritabilit(y|ies)?)\b'

    # pattern = r'\b(heritable|inheritance|inherit|heritability)\b'
    with open(file_path, 'r') as in_file, open(output_file_path, 'w') as out_file:
        for line_number, line in enumerate(in_file, start=1):
            matches = re.finditer(pattern, line, flags=re.IGNORECASE)
            for match in matches:
                word = match.group()
                out_file.write(f'{line_number}\t{word}\n')

if __name__ == '__main__':
    file_path = 'origin.txt'
    output_file_path = 'output.txt'
    find_heritability_words(file_path, output_file_path)
    print("Done!")
