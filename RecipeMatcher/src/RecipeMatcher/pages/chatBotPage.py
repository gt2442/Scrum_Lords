import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, LEFT, RIGHT
from RecipeMatcher.pages.style import LABEL_STYLE, BUTTON_STYLE, CONTAINER_STYLE

def create_chatbot_page(chatbot_instance):
    # Main container with styling from the first file
    main_box = toga.Box(style=CONTAINER_STYLE)

    title = toga.Label(
        "Generate a Meal with AI",
        style=Pack(
            font_family="sans-serif",
            color="#1E90FF",
            font_size=20,
            font_weight="bold",
            padding=10,
            text_align=CENTER
        )
    )

    # Text input for user queries
    user_input = toga.TextInput(
        placeholder="Type your meal request or question",
        style=Pack(width=300, padding=(10, 0))
    )

    # Multiline text input for chat display
    result_display = toga.MultilineTextInput(
        value="",
        readonly=True,
        style=Pack(
            width=300,        # Adjusted width to 300
            height=200,       # Adjusted height to 200
            padding=(10, 0),
            background_color="#E6F7FF"
        )
    )

    # Functionality for persona selection
    def set_persona(selected_persona):
        personas = {
            "Default Chef": "You are a helpful chef that generates meal plans and recipes.",
            "Batman": "You are a helpful chef that generates meal plans and recipes. Respond in the tone of Batman.",
            "Elmer Fudd": "You are a helpful chef that generates meal plans and recipes. Take the persona of Elmer Fudd.",
            "Quick Conversation": "You are a helpful chef that generates meal plans and recipes. Ask the user questions.",
        }
        chatbot_instance.set_persona(personas[selected_persona])
        result_display.value = f"Persona set to: {selected_persona}\n"

    # Persona selection dropdown
    persona_dropdown = toga.Selection(
        items=["Default Chef", "Batman", "Elmer Fudd", "Quick Conversation"],
        on_change=lambda widget: set_persona(widget.value),
        style=Pack(
            width=300,        # Adjusted width to 300
            padding=(10, 0),
            font_size=14,
            color="#228B22",
            alignment=CENTER
        )
    )

    # Functionality for chatting with the AI
    def chat_with_gpt_action(widget):
        query = user_input.value.strip()
        if query:
            response = chatbot_instance.chat_with_ai(query)
            result_display.value += f"User: {query}\nChatGPT: {response}\n\n"
            user_input.value = ""
        else:
            result_display.value += "Please enter a valid input.\n"

    # Functionality for clearing chat history
    def clear_history_action(widget):
        chatbot_instance.clear_conversation()
        result_display.value = "Conversation cleared.\n"

    # Send button with styling
    chat_button = toga.Button(
        "Send to ChatGPT",
        on_press=chat_with_gpt_action,
        style=Pack(
            width=150,                  # Adjusted width to 150
            padding=(10, 0),
            background_color="#1E90FF",
            color="white",
            text_align=CENTER
        )
    )

    # Clear button with styling
    clear_button = toga.Button(
        "Clear Conversation",
        on_press=clear_history_action,
        style=Pack(
            width=150,                  # Adjusted width to 150
            padding=(10, 0),
            background_color="#104E8B",
            color="white",
            text_align=CENTER
        )
    )

    # Container for buttons to place them side by side
    button_container = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding=10))
    button_container.add(chat_button)
    button_container.add(clear_button)

    # Add components to the main container
    main_box.add(title)
    main_box.add(persona_dropdown)
    main_box.add(result_display)
    main_box.add(user_input)
    main_box.add(button_container)

    return main_box
