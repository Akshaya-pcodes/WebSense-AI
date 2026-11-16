from flask import Flask, render_template, request
from website_extractor import extract_website_content
from gemini_service import generate_summary

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():

    website_url = request.form.get("url", "").strip()

    summary_type = request.form.get(
        "summary_type", "short"
    )

    if not website_url:
        return "Please enter a website URL."

    # Extract website content
    website_data = extract_website_content(website_url)

    if "error" in website_data:
        return website_data["error"]

    # Generate AI summary
    summary = generate_summary(
        website_data["content"],
        summary_type
    )

    return render_template(
        "result.html",
        title=website_data["title"],
        url=website_url,
        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)