import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

def create_meal_query_page(chatbot_instance):
    state = {"stage": 0}
    user_selections = {"meal_time": None, "flavor_profile": None, "nutrition_focus": None}

    option_sets = [
        (["Breakfast", "Lunch", "Dinner", "Dessert"], "meal_time"),
        (["Sweet", "Sour", "Salty", "Spicy"], "flavor_profile"),
        (["High Protein", "High Carbs", "Dairy Based", "Fruits"], "nutrition_focus"),
    ]

    button_colors = ["lightpink", "lightgreen", "lightblue", "lightyellow"]

    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

    title = toga.Label("What shall we make?", style=Pack(font_size=24, padding=(0, 20)))

    content_area = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=10))

    result_display = toga.MultilineTextInput(
        readonly=True, style=Pack(width=400, height=150, padding=(10, 0))
    )

    def update_content_area():
        content_area.children.clear()
        if state["stage"] >= len(option_sets):
            generate_result()
        else:
            options, key = option_sets[state["stage"]]
            grid_container = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=5))

            for i in range(0, len(options), 2):
                row = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding=5))
                for j in range(2):
                    if i + j < len(options):
                        option = options[i + j]
                        button_color = button_colors[i + j]
                        button = toga.Button(
                            option,
                            on_press=lambda widget, opt=option: select_option(key, opt),
                            style=Pack(width=150, height=80, background_color=button_color),
                        )
                        row.add(button)
                grid_container.add(row)

            content_area.add(grid_container)

    def select_option(category, option):
        user_selections[category] = option
        state["stage"] += 1
        update_content_area()

    def generate_result():
        response = chatbot_instance.generate_meal_suggestion(
            user_selections["meal_time"],
            user_selections["flavor_profile"],
            user_selections["nutrition_focus"],
        )
        result_display.value = response
        redo_button = toga.Button(
            "Redo Meal Query",
            on_press=reset_query,
            style=Pack(padding=10, width=200, background_color="red"),
        )
        content_area.add(result_display)
        content_area.add(redo_button)

    def reset_query(widget=None):
        state["stage"] = 0
        user_selections.update({"meal_time": None, "flavor_profile": None, "nutrition_focus": None})
        update_content_area()

    main_box.add(title)
    main_box.add(content_area)
    update_content_area()

    return main_box
