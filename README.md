# Hamster Kombat Bot Slim Edition

This repository provides a streamlined version of the original [HamsterKombatBot](https://github.com/shamhi/HamsterKombatBot), designed for educational purposes with simplified functionalities.

## Disclaimer and Warning
- **No Responsibility**: The creators of this project bear no responsibility
- **Independent Research**: Users should conduct their research and consult professionals.
- **Compliance with Laws**: Ensure compliance with all applicable laws and regulations in your jurisdiction.
- You are responsible for anything you do with the this code, just as you are responsible for anything you do with any dangerous object such as a knife, gun, lighter, or car.
- You are responsible for the content you publish, and you cannot blame the model any more than you can blame the knife, gun, lighter, or car for what you do with it.

## Functionality

| Functional                                                     | Supported |
|----------------------------------------------------------------|:---------:|
| Multithreading                                                 |     ✅     |
| Auto-purchase of items if you have coins (tap, energy, charge) |     ✅     |
| Random sleep time between clicks                               |     ✅     |
| Random number of clicks per request                            |     ✅     |
| Support tdata / pyrogram .session / telethon .session          |     ✅     |

## Settings

Detailed settings can be configured in the `.env` file. An example can be found in the repository.

## Prerequisites

Ensure you have the following installed:
- [Python](https://www.python.org/downloads/) version 3.11
- Git

## Obtaining API Keys

1. Visit [my.telegram.org](https://my.telegram.org), log in using your phone number.
2. Select **"API development tools"** and fill out the form to register a new application.
3. Store your `API_ID` and `API_HASH` in the `.env` file.

## Installation

Clone the repository and install the required dependencies:

```shell
git clone git@github.com:SMARTSHEEP-IO/hamster-kombat-bot-slim-edition.git
cd hamster-kombat-bot-slim-edition
python -m venv .venv

.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS and Linux

pip install -r requirements.txt
cp .env-example .env  # Then configure your API_ID and API_HASH
python main.py
```
Also for quick launch you can use arguments, for example:
```shell
python3 main.py --action (1/2)
# Or
python3 main.py -a (1/2)

# i.e
python3 main.py -a 2

#1 - Create session
#2 - Run clicker
```
