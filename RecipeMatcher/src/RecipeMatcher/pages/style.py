from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

# Primary Colors
PRIMARY_BLUE = "#1E90FF" #for headers and labels
LIGHT_BLUE = "#ADD8E6"
DARK_BLUE = "#104E8B"
BACKGROUND_BLUE = "#E6F7FF" #background color

# Accent Colors
ACCENT_GREEN = "#104E8B" #important buttons and info
SOFT_GREEN = "#98FB98"
DARK_GREEN = "#228B22"

# Neutrals for text and borders
LIGHT_GRAY = "#F5F5F5" 
MEDIUM_GRAY = "#D3D3D3"
DARK_GRAY = "#A9A9A9"

LABEL_STYLE = Pack(color=PRIMARY_BLUE, font_size=18)
BUTTON_STYLE = Pack(background_color=DARK_BLUE, color="white", padding=10, flex = 1)
CONTAINER_STYLE = Pack(background_color=BACKGROUND_BLUE, direction = COLUMN, padding=20, alignment=CENTER)