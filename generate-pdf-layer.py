import sys
import fitz

LAYER_CONFIG_NUM = -1

# Check if the PDF file name is provided as a command-line argument
if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} input_pdf_file.pdf")
    sys.exit(1)

# Get the PDF file name from the command-line argument
input_pdf = sys.argv[1]

try:
    # Open the PDF file
    pdf = fitz.open(input_pdf)
    ocg = pdf.add_ocg("text", config=LAYER_CONFIG_NUM, on=False)

    for i in range(pdf.page_count):
        # Full OCR
        page = pdf[i]
        full_tp = page.get_textpage_ocr(flags=0, dpi=300, full=True)
        
        # remove unwanted line breaks, get text in blocks, reads much better
        blocks = page.get_text("blocks", textpage=full_tp)
        
        # create a list of strings from the blocks
        strings = []
        for b in blocks:
            strings.append(b[4].replace("\n", " "))

        # add text to separate layer in a textbox
        page.insert_textbox((0,0,page.rect.width, page.rect.width), "\n\n".join(strings), rotate=-90, oc=ocg)
        
    # Save the modified PDF to a new file
    output_pdf = "output.pdf"
    pdf.save(output_pdf)
    pdf.close()
    print(f"Output saved as '{output_pdf}'")

except Exception as e:
    print("An error occurred:", str(e))
