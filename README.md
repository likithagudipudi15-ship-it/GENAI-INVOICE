# AI Invoice Analyzer

An AI-powered invoice analysis application built with Streamlit and Google's Gemini API. Upload an invoice image or PDF to automatically extract key information, interpret invoice details, and generate structured insights using Generative AI.

---

## Features

- 🧾 Upload invoice images or PDF documents
- 🤖 AI-powered invoice understanding using Google Gemini
- 📄 Extracts and interprets invoice details
- 💬 Generates structured and easy-to-read responses
- ⚡ Interactive Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
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

1. Upload an invoice image or PDF.
2. The application processes the document using Google Gemini.
3. AI extracts and interprets invoice information.
4. The results are displayed in a clear and structured format.

---

## Future Enhancements

- Automatic field extraction (vendor, invoice number, date, total amount)
- Export extracted data to CSV or Excel
- Multi-invoice processing
- OCR integration for scanned invoices
- Dashboard for invoice management

---

## License

This project is intended for educational and learning purposes.