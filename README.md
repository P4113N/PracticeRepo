# Marketing Budget Optimization Web App

This simple Flask application demonstrates how to use `pymc-marketing` for marketing mix modeling (MMM) and budget optimization.

## Setup

Install dependencies:

```bash
pip install Flask pandas pymc-marketing
```

## Running the App

```bash
python app.py
```

Open `http://localhost:5000` in your browser and enter a total budget and number of periods. The application returns an optimized allocation across TV, online and print channels based on a synthetic dataset generated at startup.
