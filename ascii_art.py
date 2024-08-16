from ascii_magic import AsciiArt
from bs4 import BeautifulSoup

desired_count = 92070  # Number of students, staff, faculty at UBC across both Campuses
columns = 330.6199999999983
width_ratio = 0.79
special_word = "UBC"
image = "UBC.png"

def generate_and_count_ubc(columns, width_ratio, special_word, image):
    """
    Generates an HTML file from the specified columns and width ratio to produce ASCII art 
    of the given image while counting the number of occurrences of the special word in the HTML.

    Args:
        columns (float): The number of columns for the ASCII art.
        width_ratio (float): The width ratio for scaling the ASCII art.
        special_word (str): The word to be used in place of the ASCII characters.
        image (str): The path to the image file.

    Returns:
        int: The count of the special word in the generated HTML.
    """
    my_art = AsciiArt.from_image(image)
    html_content = my_art.to_html(columns=columns, width_ratio=width_ratio, char=special_word)
    
    html_with_font = f'''
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Anton', Arial, sans-serif;
                white-space: pre-wrap;
                background-color: black;
                color: white;
            }}
            pre {{
                width: {columns * width_ratio}px;
                height: {columns}px;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    '''
    
    with open('ascii_art.html', 'w') as file:
        file.write(html_with_font)
    
    count = html_content.count(special_word)

    # Use BeautifulSoup to parse the HTML and extract width and height
    soup = BeautifulSoup(html_with_font, 'html.parser')
    pre_tag = soup.find('pre')
    if pre_tag:
        style = pre_tag.get('style', '')
        width_match = re.search(r'width:\s*(\d+)px', style)
        height_match = re.search(r'height:\s*(\d+)px', style)

        if width_match and height_match:
            width_px = int(width_match.group(1))
            height_px = int(height_match.group(1))
            aspect_ratio = width_px / height_px

            print(f"Image width: {width_px}px")
            print(f"Image height: {height_px}px")
            print(f"Aspect ratio: {aspect_ratio:.2f}")

    return count

ubc_count = generate_and_count_ubc(columns, width_ratio, special_word, image)
print(f"Initial count: {ubc_count}")

while ubc_count != desired_count:
    if ubc_count < desired_count:
        columns += 0.01
    else:
        width_ratio += 0.01

    ubc_count = generate_and_count_ubc(columns, width_ratio, special_word, image)
    print(f"New count: {ubc_count} (columns: {columns}, width_ratio: {width_ratio})")

print(f"Final count of 'UBC': {ubc_count}")
