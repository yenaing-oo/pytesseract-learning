import pytesseract

print("\n-----------------------------\n")

# PSM 3: Fully automatic page segmentation, but no OSD. (Default)
# path to image can be relative or absolute
print(pytesseract.image_to_string('image1.png'))

print("\n-----------------------------\n")

# PSM 0: Orientation and script detection (OSD) only (meta data).
print(pytesseract.image_to_osd('image2.png'))

print("\n-----------------------------\n")

# PSM 1 and 2 not useful

# PSM 4: Assume a single column of text of variable sizes
# Suitable for column data, and require text to be concatenated row-wise (spreadsheet, recipts)
print(pytesseract.image_to_string('image3.png', config='--psm 4'))

print("\n-----------------------------\n")

# PSM 5: Not useful

# PSM 6: Assume a single uniform block of text
# Suitable for pages in book that use a single, consistent font
print(pytesseract.image_to_string('novel-page.jpg', config='--psm 6'))

print("\n-----------------------------\n")

# PSM 7: Treat the image as a single text line
# Suitable for images that contain a single line of text

print(pytesseract.image_to_string('license-plate.png', config='--psm 7'))

print("\n-----------------------------\n")

