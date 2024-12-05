# src/RecipeMatcher/pages/chatBotPage.py
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

def create_chatbot_page(result_display, chatbot_instance):
    # Main container
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

    # Input box
    user_input = toga.TextInput(
        placeholder="Type your meal request or question",
        style=Pack(width=400, padding=(10, 0))
    )

    # Persona selection dropdown
    persona_dropdown = toga.Selection(
        items=[
            "Default Chef",
            "Batman",
            "Elmer Fudd",
            "Quick Conversation",
        ],
        on_select=lambda widget: set_persona(widget.value),
        style=Pack(width=400, padding=(10, 0))
    )

    def set_persona(selected_persona):
        personas = {
            "Default Chef": "You are a helpful chef that generates meal plans and recipes.",
            "Batman": "You are a helpful chef that generates meal plans and recipes. Respond in the tone of Batman, randomly mentioning protecting Gotham.",
            "Elmer Fudd": "You are a helpful chef that generates meal plans and recipes. Take the persona of Elmer Fudd, randomly recommending rabbit dishes.",
            "Quick Conversation": "You are a helpful chef that generates meal plans and recipes. Ask the user a few questions to find the best meal for them.",
        }
        chatbot_instance.set_persona(personas[selected_persona])
        result_display.value = f"Persona set to: {selected_persona}\n"

    # Chat button action
    def chat_with_gpt_action(widget):
        query = user_input.value.strip()
        if query:
            response = chatbot_instance.generate_meal_plan(query)
            result_display.value += f"User: {query}\nChatGPT: {response}\n\n"
        else:
            result_display.value = "Please enter a valid input."

    # Clear history button
    def clear_history_action(widget):
        chatbot_instance.clear_conversation()
        result_display.value = "Conversation cleared.\n"

    # Send button
    chat_button = toga.Button(
        "Send to ChatGPT",
        on_press=chat_with_gpt_action,
        style=Pack(width=200, padding=(10, 0), background_color="blue", color="white")
    )

    # Clear button
    clear_button = toga.Button(
        "Clear Conversation",
        on_press=clear_history_action,
        style=Pack(width=200, padding=(10, 0), background_color="red", color="white")
    )

    # Result display (already styled)
    result_display.style = Pack(width=400, height=150, padding=(10, 0))

    # Add widgets to the container
    main_box.add(persona_dropdown)
    main_box.add(user_input)
    main_box.add(chat_button)
    main_box.add(clear_button)
    main_box.add(result_display)

    return main_box
