import os
import pypdf

for filename in os.listdir("PDFs"):
    # filename = "[PDF]_Towards_a_catalog_of_prompt_patterns_to_enhance_the_discipline_of_prompt_engineering"
    pdfReader = pypdf.PdfReader(f"PDFs\\{filename}")
    with open(f"PDF_texts/{filename}.txt", "wt", encoding="utf-8") as f:
        for page in pdfReader.pages:
            text = page.extract_text()
            f.write(text)
