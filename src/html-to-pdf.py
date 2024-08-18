import pdfkit

# Define specifications
width_inch = 36
height_inch = 24

# Convert inches to points (1 inch = 72 points)
width_points = width_inch * 72
height_points = height_inch * 72

# Convert HTML to PDF with specified dimensions and ensure it fits
pdfkit.from_file(
    'UBC-MATH-ANNEX.html',
    'Sai_Pusuluri.pdf',
    options={
        'page-width': f'{width_inch}in',
        'page-height': f'{height_inch}in',
        'dpi': '500',  
        'no-outline': None, 
        'zoom': '0.8',  
        'viewport-size': '1280x1024',  
        'disable-smart-shrinking': '',  
        'margin-top': '1in',
        'margin-right': '1in',
        'margin-bottom': '0in',
        'margin-left': '1in',
    }
)

print(f"PDF created with dimensions {width_inch} inches x {height_inch} inches")
