# Task 3: Templates and Dynamic Content

A beginner-friendly Flask project showing how to use Jinja2 templates, template inheritance, and dynamic data passed from Python to HTML.

## What You'll Learn
- What templates are and why they are useful
- How Flask uses the Jinja2 templating engine
- How to pass data from Python to HTML templates
- How to create reusable layouts with template inheritance

## Features
- Shared navigation and footer in `base.html`
- Child templates that extend the base template
- Dynamic username and current date
- A list generated using a Jinja2 `for` loop
- Home and About routes
- Responsive CSS styling

## Technologies
- Python
- Flask
- Jinja2
- HTML
- CSS

## Setup and Run

1. Install Python 3.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the required package:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## Project Structure

```text
task-3-flask-templates/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   └── about.html
└── static/
    └── style.css
```

## Routes
- `/` — Home page with dynamic content
- `/about` — About page using the shared base template

## Expected Outcome
A website with a consistent layout and dynamic content rendered using data supplied by Python.

**Note:** Debug mode is enabled for local development only. Do not use Flask's development server in production.
