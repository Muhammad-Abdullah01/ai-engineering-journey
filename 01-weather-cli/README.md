<div align="center">

# 🌦️ Weather CLI — AI-Powered Weather Assistant

A command-line weather tool that fetches real-time weather data and turns it into a natural, conversational summary using Google's Gemini API.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat)

</div>

---

## 📖 Overview

This project started as a simple weather-fetching script and evolved into a small AI-integrated application — the first project in my [AI Engineering Journey](../README.md). It fetches live weather data from OpenWeatherMap and passes it to Google's Gemini model to generate a short, friendly, human-like description of the conditions.

**Example output:**
```
===================================
  Weather in Karachi
===================================
  Condition:   clear sky
  Temperature: 32°C
  Feels like:  35°C
  Humidity:    48%
===================================

💬 It's a scorcher out there in Karachi today — clear skies but 
   feels like 35°C, so definitely a day for sunglasses and 
   plenty of water!
```

---

## ✨ Features

- 🌍 **Real-time weather data** for any city worldwide via the OpenWeatherMap API
- 🤖 **AI-generated summaries** using Google Gemini — turns raw data into natural language
- 🛡️ **Robust error handling** for invalid cities, network failures, and API auth issues
- 🧩 **Modular architecture** — weather fetching and AI logic are fully decoupled
- 🔐 **Secure credential management** using environment variables (`.env`)

---

## 🛠️ Tech Stack

| Component        | Technology                |
|-------------------|---------------------------|
| Language           | Python 3.10+               |
| Weather Data       | OpenWeatherMap API          |
| AI Summary Engine  | Google Gemini API (`gemini-2.0-flash`) |
| Config Management  | `python-dotenv`             |
| HTTP Requests      | `requests`                  |

---

## 📁 Project Structure

```
01-weather-cli/
├── src/
│   ├── weather.py        # Fetches and parses weather data
│   ├── ai_summary.py     # Generates AI-powered weather descriptions
│   └── main.py           # CLI entry point
├── .env.example           # Template for required environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- A free [OpenWeatherMap API key](https://openweathermap.org/api)
- A free [Google Gemini API key](https://aistudio.google.com/apikey)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-engineering-journey.git
cd ai-engineering-journey/01-weather-cli

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root (use `.env.example` as a reference):

```env
WEATHER_API_KEY=your_openweathermap_key_here
GEMINI_API_KEY=your_gemini_key_here
```

### Run it

```bash
cd src
python main.py
```

Enter a city name when prompted. Type `quit` to exit.

---

## 🧠 What I Learned Building This

- Structuring a Python project professionally (`src/` layout, `.gitignore`, modular files)
- Managing secrets safely using environment variables instead of hardcoding
- Debugging real-world issues: `401` authentication errors, `KeyError` typos, and virtual environment misconfigurations
- Integrating an external AI API into a working application
- **Swapping AI providers with minimal friction** — this project originally used Anthropic's Claude API; switching to Gemini required changing only one file (`ai_summary.py`), thanks to keeping the AI logic decoupled from the rest of the app
- Writing clear documentation for future reference and portfolio presentation

---

## 🗺️ Roadmap / Ideas for Improvement

- [ ] Add support for multiple languages in AI summaries
- [ ] Cache recent city lookups to reduce API calls
- [ ] Add unit tests for `weather.py` and `ai_summary.py`
- [ ] Build a simple web UI version using Streamlit or FastAPI

---

## 👤 Author

<div align="center">

**Muhammad Abdullah**

Part of my [AI Engineering Journey](../README.md) — documenting my transition from a BS Data Science graduate into AI Engineering, one project at a time.

</div>

---

<div align="center">

## 📄 License

This project is open source and available under the [MIT License](../LICENSE).

</div>
