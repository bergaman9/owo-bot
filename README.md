# OwO Bot

## About

OwO Bot is a Discord bot project that automatically runs "OwO" commands in a specified channel. The bot keeps track of wins and losses and executes commands at specific time intervals.

## Features

- Automatic execution of "OwO" commands
- Tracking of wins and losses
- Execution of commands at specific time intervals

## Installation

### Requirements

- Python 3.x
- discord.py
- python-dotenv
- requests

### Steps

1. Install the required packages using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file and add the necessary variables:
    ```env
    TOKEN=Your_Discord_Bot_Token
    CHANNEL_ID=Your_Channel_ID
    AUTH=Your_Auth_Token
    ```

3. Run the bot:
    ```bash
    python main.py
    ```

## Usage

After running the bot, it will automatically execute "OwO" commands in the Discord channel you specified.
