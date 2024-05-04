import fitz

LAYER_CONFIG_NUM = -1

pdf = fitz.open("1869 Gradual Enfranchisement Act.pdf")
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

    print(page.rect)
    # add text to separate layer in a textbox
    page.insert_textbox((0,0,page.rect.width, page.rect.width), "\n\n".join(strings), rotate=-90, oc=ocg)
    

pdf.save("output.pdf")
pdf.close()

    
    