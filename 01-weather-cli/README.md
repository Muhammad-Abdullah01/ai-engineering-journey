## Features
- Fetches real-time weather data via OpenWeatherMap API
- Generates natural-language weather summaries using Google Gemini API
- Robust error handling for network, auth, and API failures

## What I learned
- Environment variable management with .env
- Debugging API authentication (401 errors)
- Swapping LLM providers (Anthropic → Gemini) with minimal code changes, thanks to modular design
- Reading Python tracebacks to fix real bugs (KeyError, wrong client methods)
