

# Review Classification and Adjustment Tool

This app is meant to assess and address bias in restaurant reviews and it meant to be used in conjunction with the Review Classification Dashboard.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)

## Introduction

Restaurant Reviews on the internet suffer from bias where the text of the review does not correspond with the number rating assign. The goal of this dashboard is for restaurant owners and costumers can input a written review and obtain an accurate number rating for their review.

Additionally, the webiste can also take text and adjust it to be appropriate for that given rating.

## Features

- Review Classification
- Review Adjustment

## Installation

### Prerequisites

- Python 3.6 or higher
- pip

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/johanbarreiro/review_reviewer.git
   cd review_reviewer
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   pip install -r streamlit_app/requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. In either tab enter your review text to obtain output.

## Configuration

In the streamlit_app folder of the repository you must create a .env file and enter your OpenAI API Key:

- `OPENAI_API_KEY`=`YourKeyHere` 
