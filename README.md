# AI Multilingual Invoice Analyzer

An AI-powered invoice understanding application built with Streamlit and Google's Gemini API. Upload an invoice image and ask questions in natural language to receive accurate, context-aware answers about the invoice contents.

---

## Features

- 📄 Upload invoice images (PNG, JPG, JPEG)
- 🌍 Multilingual invoice understanding
- 🤖 Ask natural language questions about invoice details
- 💡 AI-powered responses using Google Gemini
- ⚡ Interactive Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Pillow
- python-dotenv

---

## Project Structure

```
GENAI-INVOICE/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
│── .env          # Not uploaded
│── venv/         # Not uploaded
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/GENAI-INVOICE.git
```

Navigate to the project

```bash
cd GENAI-INVOICE
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## How It Works

1. Upload an invoice image.
2. Enter a question about the invoice.
3. Google Gemini analyzes the invoice image.
4. The application generates an accurate, context-aware response based on the invoice contents.

---

## Example Questions

- What is the total invoice amount?
- Who is the vendor?
- What is the invoice date?
- What is the invoice number?
- What products or services were billed?
- What is the payment due date?

---

## Future Enhancements

- Support for PDF invoices
- Automatic extraction of invoice fields
- Export results to CSV or Excel
- OCR support for scanned invoices
- Invoice history and search

---

## License

This project is intended for educational and learning purposes.