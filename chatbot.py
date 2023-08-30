{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPKbLyQ9U3RXHFU1n6EbvOh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Cyber-warrior-2026/IBM_project/blob/main/chatbot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install openai\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l-Y3bdrzjy3n",
        "outputId": "e632edc0-5794-4625-ea97-378a6e1bba68"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: openai in /usr/local/lib/python3.10/dist-packages (0.27.10)\n",
            "Requirement already satisfied: requests>=2.20 in /usr/local/lib/python3.10/dist-packages (from openai) (2.31.0)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from openai) (4.66.1)\n",
            "Requirement already satisfied: aiohttp in /usr/local/lib/python3.10/dist-packages (from openai) (3.8.5)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (3.2.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (2.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (2023.7.22)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (23.1.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (6.0.4)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (4.0.3)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.9.2)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.4.0)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.3.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install twilio"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eTudw8TJkPHf",
        "outputId": "6c61f542-5c8a-4dca-d851-be4761980521"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting twilio\n",
            "  Downloading twilio-8.7.0-py2.py3-none-any.whl (1.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.8/1.8 MB\u001b[0m \u001b[31m11.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: pytz in /usr/local/lib/python3.10/dist-packages (from twilio) (2023.3)\n",
            "Requirement already satisfied: requests>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from twilio) (2.31.0)\n",
            "Requirement already satisfied: PyJWT<3.0.0,>=2.0.0 in /usr/lib/python3/dist-packages (from twilio) (2.3.0)\n",
            "Requirement already satisfied: aiohttp>=3.8.4 in /usr/local/lib/python3.10/dist-packages (from twilio) (3.8.5)\n",
            "Collecting aiohttp-retry>=2.8.3 (from twilio)\n",
            "  Downloading aiohttp_retry-2.8.3-py3-none-any.whl (9.8 kB)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->twilio) (23.1.0)\n",
            "Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->twilio) (3.2.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->twilio) (6.0.4)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->twilio) (4.0.3)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->twilio) (1.9.2)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->twilio) (1.4.0)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp>=3.8.4->twilio) (1.3.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.0.0->twilio) (3.4)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.0.0->twilio) (2.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.0.0->twilio) (2023.7.22)\n",
            "Installing collected packages: aiohttp-retry, twilio\n",
            "Successfully installed aiohttp-retry-2.8.3 twilio-8.7.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install textblob"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e87qHzkxkRcG",
        "outputId": "08af325e-043e-4aba-f3bd-96247694cbfd"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: textblob in /usr/local/lib/python3.10/dist-packages (0.17.1)\n",
            "Requirement already satisfied: nltk>=3.1 in /usr/local/lib/python3.10/dist-packages (from textblob) (3.8.1)\n",
            "Requirement already satisfied: click in /usr/local/lib/python3.10/dist-packages (from nltk>=3.1->textblob) (8.1.7)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.10/dist-packages (from nltk>=3.1->textblob) (1.3.2)\n",
            "Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.10/dist-packages (from nltk>=3.1->textblob) (2023.6.3)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from nltk>=3.1->textblob) (4.66.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q8g97gu3jEp6",
        "outputId": "8ad7c8ed-0f26-463a-bb80-333503447387"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " * Serving Flask app '__main__'\n",
            " * Debug mode: on\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:werkzeug:\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
            " * Running on http://127.0.0.1:5000\n",
            "INFO:werkzeug:\u001b[33mPress CTRL+C to quit\u001b[0m\n",
            "INFO:werkzeug: * Restarting with stat\n"
          ]
        }
      ],
      "source": [
        "# Import required libraries\n",
        "from flask import Flask, request\n",
        "import openai\n",
        "from textblob import TextBlob  # for sentiment analysis\n",
        "from twilio.rest import Client  # for Twilio notifications\n",
        "\n",
        "# Initialize Flask app\n",
        "app = Flask(__name__)\n",
        "\n",
        "# Initialize OpenAI API\n",
        "openai.api_key = \"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\"\n",
        "\n",
        "# Initialize Twilio API\n",
        "twilio_account_sid = \"SKa2fb5d8c97a0e7a61686292fb3afcbdd\"\n",
        "twilio_auth_token = \"itcRe67am6kEIOWgcuSDFNt6yA2C1oLf\"\n",
        "twilio_client = Client(twilio_account_sid, twilio_auth_token)\n",
        "\n",
        "# Sample conversation history\n",
        "conversation_history = []\n",
        "\n",
        "# Define routes\n",
        "@app.route('/webhook', methods=['POST'])\n",
        "def webhook():\n",
        "    data = request.json\n",
        "\n",
        "    if data['source'] == 'whatsapp' or data['source'] == 'telegram':\n",
        "        user_message = data['message']\n",
        "        user_id = data['user_id']\n",
        "\n",
        "        # Perform sentiment analysis\n",
        "        sentiment = analyze_sentiment(user_message)\n",
        "\n",
        "        # Add user message to conversation history\n",
        "        conversation_history.append({'user_id': user_id, 'message': user_message, 'sentiment': sentiment})\n",
        "\n",
        "        # Determine user intent and provide a response\n",
        "        intent = determine_intent(user_message)\n",
        "        response = generate_response(user_message, intent)\n",
        "\n",
        "        # Send response back to the user\n",
        "        send_message_to_user(user_id, response)\n",
        "\n",
        "        # Check for high-risk keywords and send emergency notification\n",
        "        if sentiment < -0.7:\n",
        "            high_risk_keywords = [\"help\", \"emergency\", \"danger\", \"suicide\"]\n",
        "            if any(keyword in user_message for keyword in high_risk_keywords):\n",
        "                notify_support_staff(user_id, user_message)\n",
        "\n",
        "        return 'OK'\n",
        "\n",
        "    return 'Unsupported source'\n",
        "\n",
        "def analyze_sentiment(text):\n",
        "    blob = TextBlob(text)\n",
        "    return blob.sentiment.polarity\n",
        "\n",
        "def determine_intent(text):\n",
        "    # Implement your logic to determine user intent here\n",
        "    # You can use regex, keyword matching, or a more advanced NLP model\n",
        "    pass\n",
        "\n",
        "def generate_response(user_message, intent):\n",
        "    # Use the OpenAI GPT API to generate a response based on user message and intent\n",
        "    prompt = f\"User: {user_message}\\nIntent: {intent}\\nAI:\"\n",
        "    response = openai.Completion.create(\n",
        "        engine=\"davinci\",\n",
        "        prompt=prompt,\n",
        "        max_tokens=50\n",
        "    )\n",
        "    return response.choices[0].text.strip()\n",
        "\n",
        "def send_message_to_user(user_id, message):\n",
        "    # Use the WhatsApp or Telegram API to send a message to the user\n",
        "    # Implement the API-specific logic here\n",
        "    pass\n",
        "\n",
        "def notify_support_staff(user_id, message):\n",
        "    # Send an SMS or phone notification to support staff using the Twilio API\n",
        "    support_message = f\"High-risk message from user {user_id}: {message}\"\n",
        "    twilio_client.messages.create(\n",
        "        to=\"SUPPORT_PHONE_NUMBER\",\n",
        "        from_=\"TWILIO_PHONE_NUMBER\",\n",
        "        body=support_message\n",
        "    )\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run(debug=True)"
      ]
    }
  ]
}