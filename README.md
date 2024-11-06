# Segwise-Assignment

A Streamlit application that generates personalized LinkedIn connection requests by analyzing target users' profiles and recent posts.

## Tech Stack

- Python 3.9+
- Streamlit
- Selenium WebDriver
- OpenAI GPT API (for message generation)


## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/
segwise-assignment.git
cd segwise-assignment
```

2. Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate 
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create a .env file in the project root and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

Start the Streamlit server:

```
streamlit run app.py
```