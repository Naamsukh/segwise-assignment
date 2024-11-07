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

## Production Cost Estimate

This section provides an estimated monthly cost for running the LinkedIn connection request generator in a 24x7 production environment using AWS and OpenAI API.

### Breakdown:
- **AWS (Compute & Storage)**: Approx. $6.07 per month
  - This includes an EC2 `t3a.micro` instance and minimal S3 storage for logs.
- **OpenAI API (GPT-4o)**: Approx. $3.98 per month
  - Based on 150 API calls per month, each with 5,000 input tokens and 100 output tokens.

### Total Monthly Estimate:
- **$10.05 per month**
