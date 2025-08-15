# Aura-Meter: A Dynamic Discord Bot for Community Engagement

Welcome to Aura-Meter! This isn't just another Discord bot; it's a unique tool designed to bring a new level of interaction and fun to your server. Developed by a team of two passionate second-year computer science students at Gustave Eiffel University, Aura-Meter introduces a captivating "aura" system that lets your community members shine.

## ✨ What is Aura-Meter?

Aura-Meter allows users on a Discord server to have a unique "aura" score. This score isn't static—it's a living reflection of a user's presence and reputation within the community. Through a series of interactive commands, users can check their aura, give aura to others, and even participate in community-wide votes to influence aura scores. It's a fantastic way to boost engagement, encourage positive interactions, and have a great time with friends.

## 🚀 Key Features

*   **Aura Tracking:** Every user gets their own aura score, which can be viewed by anyone on the server.
*   **Peer-to-Peer Aura Transfer:** Share the love! Users can give a portion of their own aura to others.
*   **Democratic Voting System:** Engage the entire community with a weekly vote to collectively decide whose aura should be increased or decreased.
*   **Massive Vote Events:** For moments that truly shake the server, initiate a "massive vote" to grant or remove a large amount of aura from a user, for a specific reason.
*   **Slash Commands:** The bot uses modern Discord slash commands for a seamless and intuitive user experience.
*   **Easy to Set Up:** Get Aura-Meter running on your server in just a few simple steps.

## ⚙️ Getting Started

Ready to bring Aura-Meter to your server? Here’s how to set it up:

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    ```

2.  **Install Dependencies:**
    Make sure you have Python and `pip` installed. Then, install the required libraries from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` File:**
    In the root directory of the project, create a file named `.env` and add your Discord bot token:
    ```
    DISCORD_TOKEN=YourDiscordBotTokenHere
    ```

4.  **Configure the Channel ID:**
    Open `main.py` and replace the placeholder value for `channel_id` with the ID of the Discord channel where you want the bot to post announcements (like vote results).
    ```python
    channel_id = "YourChannelIdHere"
    ```

5.  **Run the Bot:**
    ```bash
    python main.py
    ```
    And that's it! The bot should now be online and ready to use on your server.

## 🎮 How to Use Aura-Meter

Interact with the bot using these simple slash commands:

*   `/salut`: Get a friendly greeting from the bot.
*   `/my_aura`: Check your own aura score.
*   `/aura <user>`: See the aura score of another user.
*   `/show_aura`: Display the aura scores of all users in the server.
*   `/total_aura`: View the combined total of all auras on the server.
*   `/give_aura <user> <amount>`: Give a specified amount of your aura to another user.
*   `/vote_aura`: Kick off the weekly aura vote for all users.
*   `/vote_massive <user> <amount> <reason>`: Start a special vote to add or remove a large amount of aura from a user for a stated reason.
*   `/dire <message>`: Make the bot repeat a message.

## 💻 Tech Stack

*   **Python**
*   **discord.py:** The Python wrapper for the Discord API.
*   **python-dotenv:** For managing environment variables.

---

*This project was created for fun by a group of friends one evening.*
