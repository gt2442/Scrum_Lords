import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

def create_chatbot_page(chatbot_instance):
    main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))

    user_input = toga.TextInput(
        placeholder="Type your meal request or question", style=Pack(width=400, padding=(10, 0))
    )

    result_display = toga.MultilineTextInput(
        value="", readonly=True, style=Pack(width=400, height=150, padding=(10, 0))
    )

    def set_persona(selected_persona):
        personas = {
            "Default Chef": "You are a helpful chef that generates meal plans and recipes.",
            "Batman": "You are a helpful chef that generates meal plans and recipes. Respond in the tone of Batman.",
            "Elmer Fudd": "You are a helpful chef that generates meal plans and recipes. Take the persona of Elmer Fudd.",
            "Quick Conversation": "You are a helpful chef that generates meal plans and recipes. Ask the user questions.",
        }
        chatbot_instance.set_persona(personas[selected_persona])
        result_display.value = f"Persona set to: {selected_persona}\n"

    persona_dropdown = toga.Selection(
        items=["Default Chef", "Batman", "Elmer Fudd", "Quick Conversation"],
        on_change=lambda widget: set_persona(widget.value),
        style=Pack(width=400, padding=(10, 0)),
    )

    def chat_with_gpt_action(widget):
        query = user_input.value.strip()
        if query:
            response = chatbot_instance.chat_with_ai(query)
            result_display.value += f"User: {query}\nChatGPT: {response}\n\n"
            user_input.value = ""
        else:
            result_display.value = "Please enter a valid input."

    def clear_history_action(widget):
        chatbot_instance.clear_conversation()
        result_display.value = "Conversation cleared.\n"

    chat_button = toga.Button(
        "Send to ChatGPT",
        on_press=chat_with_gpt_action,
        style=Pack(width=200, padding=(10, 0), background_color="blue"),
    )

    clear_button = toga.Button(
        "Clear Conversation",
        on_press=clear_history_action,
        style=Pack(width=200, padding=(10, 0), background_color="red"),
    )

    main_box.add(persona_dropdown)
    main_box.add(user_input)
    main_box.add(chat_button)
    main_box.add(clear_button)
    main_box.add(result_display)

    return main_box
