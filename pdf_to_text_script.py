import os
import pypdf


def process_string(input_string):
    # Replace newlines with spaces
    processed_string = input_string.replace('\n', ' ')
    # Strip trailing whitespace and newlines
    processed_string = processed_string.strip()
    return processed_string


def split_string(input_string, word_count):
    words = input_string.split()
    num_words = len(words)
    num_substrings = num_words // word_count
    remainder_words = num_words % word_count

    substrings = []
    start_index = 0
    for i in range(num_substrings):
        end_index = start_index + word_count
        substring = ' '.join(words[start_index:end_index])
        substrings.append(substring)
        start_index = end_index

    if remainder_words > 0:
        remainder = ' '.join(words[start_index:])
        substrings.append(remainder)

    return substrings

count = 0
for filename in os.listdir("PDFs"):
    # filename = "[PDF]_Towards_a_catalog_of_prompt_patterns_to_enhance_the_discipline_of_prompt_engineering"
    pdfReader = pypdf.PdfReader(f"PDFs\\{filename}")
    with open(f"PDF_texts/{filename}.txt", "wt", encoding="utf-8") as f:
        for page in pdfReader.pages:
            text = process_string(page.extract_text())
            chunks = split_string(text, 100)
            if count <= 0:
                print(text)

            for t in chunks:
                f.write("\n" + t)
            count += 1
