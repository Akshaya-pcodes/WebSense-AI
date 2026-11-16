WebSense AI – AI Website Summarizer

WebSense AI is a web application designed to extract readable content from websites and generate concise, meaningful summaries using Google's Gemini AI.

The application helps users understand lengthy website content quickly by converting it into structured summaries.

Overview

Reading lengthy web pages can be time-consuming. WebSense AI simplifies this process by allowing users to enter a website URL and receive an AI-generated summary.

The application uses Flask as the backend framework, BeautifulSoup for website content extraction, and Google's Gemini API for AI-powered summarization.

Key Features

- Website URL Input
- Automatic Website Content Extraction
- HTML Parsing using BeautifulSoup
- AI-Based Content Summarization
- Short Summary
- Detailed Summary
- Key Points Summary
- Dedicated Summary Results Page
- URL Validation
- Website Connection Error Handling

Technologies Used

Technology| Purpose
Python| Backend Programming
Flask| Web Framework
Google Gemini API| AI Summarization
BeautifulSoup| HTML Parsing
Requests| Website Content Retrieval
HTML5| Page Structure
CSS3| User Interface
JavaScript| Frontend Interactions

Project Structure

WebSense-AI/
│
├── app.py
├── config.py
├── website_extractor.py
├── gemini_service.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md

How It Works

1. The user enters a website URL.
2. Flask receives the submitted URL.
3. The website extractor retrieves the webpage HTML.
4. BeautifulSoup removes unnecessary HTML elements.
5. Readable website content is extracted.
6. The extracted content is passed to the Gemini AI service.
7. Gemini generates a summary based on the selected summary type.
8. The application displays the result on a separate results page.

Installation and Setup

1. Clone the Repository

git clone https://github.com/Akshaya-pcodes/WebSense-AI.git

2. Navigate to the Project Folder

cd WebSense-AI

3. Create a Virtual Environment

python -m venv venv

4. Activate the Virtual Environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

5. Install Dependencies

pip install -r requirements.txt

6. Configure Gemini API

Create a ".env" file in the project root directory.

GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash
FLASK_SECRET_KEY=your_secret_key

Get your API key from:

https://aistudio.google.com/apikey

Important: Never upload your ".env" file or expose your API key publicly.

7. Run the Application

python app.py

8. Open in Browser

http://127.0.0.1:5000

Application Modules

1. Flask Backend – "app.py"

Handles HTTP requests, receives website URLs, coordinates extraction and summarization, and renders the result page.

2. Website Extractor – "website_extractor.py"

Uses Requests and BeautifulSoup to retrieve and parse webpage content.

3. Gemini Service – "gemini_service.py"

Connects to Google's Gemini API and generates summaries from extracted website content.

4. Configuration – "config.py"

Loads application configuration and environment variables.

Summary Types

Type| Description
Short Summary| Concise overview of website content
Detailed Summary| More descriptive summary with headings
Key Points| Main information presented as bullet points

Error Handling

The application includes handling for:

- Invalid website URLs
- Website connection failures
- Request timeouts
- Non-HTML responses
- Empty extracted content
- AI summarization errors

Limitations

- Some websites may block automated requests.
- JavaScript-rendered content may not be extracted.
- Summarization requires a valid Gemini API key and available API quota.
- Extracted content is limited to a configured character length.

Future Improvements

- PDF Summary Export
- TXT Summary Export
- Improved Dynamic Website Extraction
- Enhanced URL and Network Security

Author

Akshaya P

GitHub: https://github.com/Akshaya-pcodes

---

Developed as an AI-integrated web development project using Python, Flask, web scraping, and Google's Gemini API.
