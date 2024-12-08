import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, CENTER
from RecipeMatcher.pages.style import LABEL_STYLE, BUTTON_STYLE, CONTAINER_STYLE

def create_chatbot_page(chatbot_instance):
    # Main container
    main_box = toga.Box(style=CONTAINER_STYLE)

    title = toga.Label(
        "Generate a Meal with AI",
        style=Pack(font_family="sans-serif", color="#1E90FF", font_size=20, font_weight="bold", padding=10)
    )

    # Scrollable chat history container
    chat_history = toga.ScrollContainer(style=Pack(width=400, height=300, padding=10, background_color="#E6F7FF"))

    # Box to hold chat bubbles
    chat_bubble_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    chat_history.content = chat_bubble_box

    # Input box for user queries
    user_input = toga.TextInput(
        placeholder="Type your meal request or question",
        style=Pack(width=400, padding=(10, 0))
    )

    def add_chat_bubble(sender, message, is_user=True):
        """Add a chat bubble to the chat history."""
        # Calculate the approximate width of the bubble based on text length
        text_length = len(message)
        calculated_width = min(300, max(100, text_length * 5))
        # Style for the chat bubble
        bubble_style = Pack(
            padding=10,
            background_color="#1E90FF" if is_user else "#D3D3D3",  # User: Blue, AI: Gray
            color="white" if is_user else "black",
            #border_radius=10,  # Rounded corners for the bubble
            text_align=LEFT if is_user else RIGHT,
            width=calculated_width
        )
        # Alignment for the chat bubble
        alignment = Pack(alignment=LEFT if is_user else RIGHT, padding_right= 0, padding_top=5, padding_bottom=5)
        
        # Create bubble container
        bubble = toga.Box(style=alignment)
        bubble_content = toga.Label(message, style=bubble_style)
        bubble.add(bubble_content)
        
        # Add the bubble to the chat history box
        chat_bubble_box.add(bubble)


    def chat_with_gpt_action(widget):
        query = user_input.value.strip()
        if query:
            # Add user message bubble
            add_chat_bubble("User", query, is_user=True)

            # Generate AI response and add it as a bubble
            response = chatbot_instance.generate_meal_plan(query)
            add_chat_bubble("ChatGPT", response, is_user=False)

            # Clear input after sending
            user_input.value = ""
        else:
            add_chat_bubble("System", "Please enter a valid input.", is_user=False)

    def clear_history_action(widget):
        # Clear the conversation
        chatbot_instance.clear_conversation()
        chat_bubble_box.children.clear()  # Clear all chat bubbles

    # Persona selection dropdown
    persona_dropdown = toga.Selection(
        items=[
            "Default Chef",
            "Batman",
            "Elmer Fudd",
            "Quick Conversation",
        ],
        on_change=lambda widget: chatbot_instance.set_persona(widget.value),
        style=Pack(width=400, padding=(10, 0), font_size=14, color="#228B22", alignment=CENTER)
    )

    # Send button
    chat_button = toga.Button(
        "Send to ChatGPT",
        on_press=chat_with_gpt_action,
        style=Pack(width=200, padding=(10, 0), background_color="#1E90FF", color="white")
    )

    # Clear conversation button
    clear_button = toga.Button(
        "Clear Conversation",
        on_press=clear_history_action,
        style=Pack(width=200, padding=(10, 0), background_color="#104E8B", color="white")
    )

    # Decorative horizontal line for separation
    separator = toga.Box(
        style=Pack(
            height=10,
            width=600,
            background_color="#104E8B",
            padding_top=10,
            padding_bottom=0
        )
    )

    separator_top = toga.Box(
        style=Pack(
            height=2,
            width=500,
            background_color="#104E8B",
            padding_top=10,
            padding_bottom=0
        )
    )
    separator_bottom = toga.Box(
        style=Pack(
            height=2,
            width=500,
            background_color="#104E8B",
            padding_top=0,
            padding_bottom=10
        )
    )
    

    # Add widgets to the container
    main_box.add(title)
    main_box.add(persona_dropdown)
    main_box.add(separator_top)
    main_box.add(chat_history)
    main_box.add(separator_bottom)
    main_box.add(user_input)
    main_box.add(chat_button)
    main_box.add(clear_button)
    main_box.add(separator)
    return main_box
