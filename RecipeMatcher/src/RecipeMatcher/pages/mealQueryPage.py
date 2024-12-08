import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
 
def create_meal_query_page(chatbot_instance):
    # State to track the current stage of user selection
    state = {"stage": 0}  # 0 = Meal Time, 1 = Flavor Profile, 2 = Nutrition Focus
    user_selections = {"meal_time": None, "flavor_profile": None, "nutrition_focus": None}
 
    # Option sets for each category
    option_sets = [
        (["Breakfast", "Lunch", "Dinner", "Dessert"], "meal_time"),
        (["Sweet", "Sour", "Salty", "Spicy"], "flavor_profile"),
        (["High Protein", "High Carbs", "Dairy Based", "Fruits"], "nutrition_focus")
    ]
 
    # Button colors for each option
    button_colors = ["lightpink", "lightgreen", "lightblue", "lightyellow"]
 
    # Main container for the page
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))
 
    # Title for the page
    title = toga.Label(
        "What shall we make?",
        style=Pack(font_size=24, font_weight="bold", text_align=CENTER, padding=(0, 20))
    )
 
    # Dynamic container for buttons and results
    content_area = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=10))
 
    # Result display area
    result_display = toga.MultilineTextInput(
        readonly=True,
        style=Pack(width=400, height=150, padding=(10, 0))
    )
 
    def update_content_area():
        """Update the content area based on the current stage."""
        # Clear existing widgets in the content area
        for child in content_area.children[:]:
            content_area.remove(child)
 
        # Check if all stages are complete
        if state["stage"] >= len(option_sets):
            # Show result after completing all stages
            generate_result()
        else:
            # Show the next set of buttons in a 2x2 grid
            options, key = option_sets[state["stage"]]
            grid_container = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=5))
 
            for i in range(0, len(options), 2):
                row = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding=5))
                for j in range(2):
                    if i + j < len(options):
                        option = options[i + j]
                        button_color = button_colors[i + j]  # Assign fixed colors
                        button = toga.Button(
                            option,
                            on_press=lambda widget, opt=option: select_option(key, opt),
                            style=Pack(
                                padding=5, width=150, height=80, background_color=button_color, text_align=CENTER
                            )
                        )
                        row.add(button)
                grid_container.add(row)
 
            content_area.add(grid_container)
 
    def select_option(category, option):
        """Handle selection of an option and proceed to the next stage."""
        user_selections[category] = option
        state["stage"] += 1
        update_content_area()
 
    def generate_result():
        """Generate the result using the ChatBot."""
        response = chatbot_instance.generate_meal_suggestion(
            user_selections["meal_time"],
            user_selections["flavor_profile"],
            user_selections["nutrition_focus"]
        )
        result_display.value = response
 
        # Display the result in the content area with a redo button
        content_area.add(result_display)
        redo_button = toga.Button(
            "Redo Meal Query",
            on_press=reset_query,
            style=Pack(padding=10, width=200, background_color="white", text_align=CENTER)
        )
        content_area.add(redo_button)
 
    def reset_query(widget=None):
        """Reset the meal query to allow the user to start over."""
        user_selections.clear()
        user_selections.update({"meal_time": None, "flavor_profile": None, "nutrition_focus": None})
        state["stage"] = 0
        update_content_area()
 
    # Initial setup
    main_box.add(title)
    main_box.add(content_area)
    update_content_area()
 
    return main_box