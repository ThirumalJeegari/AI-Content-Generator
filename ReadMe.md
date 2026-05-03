# ✍️ AI Content Generator (Blog • LinkedIn • Twitter)

## 🚀 Overview

The **AI Content Generator** is a web application that creates high-quality content for blogs, LinkedIn posts, and Twitter/X threads using AI.

Built with **Python**, **Streamlit**, and the **Groq API**, this tool helps content creators, marketers, and professionals generate engaging content in seconds.

---

## 🎯 Features

* 📝 Generate content from a single topic input
* 🎭 Multiple tone options:

  * Formal
  * Casual
  * Technical
  * Creative
* 📊 Output formats:

  * Blog Post
  * LinkedIn Post
  * Twitter/X Thread
* 🔢 Word limit control
* ⚡ Fast AI responses
* 🎨 Simple and user-friendly UI

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM API:** Groq
* **Model:** llama3-8b-8192

---

## 📂 Project Structure

```id="g5l8ru"
AI-Content-Generator/
│
├── app.py               # Main Streamlit app
├── llm_helper.py        # AI response logic
├── config.py (optional) # API client setup
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```id="h3pzbc"
git clone https://github.com/your-username/ai-content-generator.git
cd ai-content-generator
```

### 2. Install dependencies

```id="1rm38v"
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

### Windows (PowerShell)

```id="ttdtnz"
$env:GROQ_API_KEY="your_api_key_here"
```

### Windows (CMD)

```id="q3jgm4"
set GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```id="kwpf3y"
streamlit run app.py
```

---

## 💡 Usage

1. Enter a **topic** (e.g., "Benefits of AI in Education")
2. Select a **tone**
3. Choose **content type** (Blog / LinkedIn / Twitter)
4. Set **word limit**
5. Click **Generate**

---

## 🧪 Example Input

```id="nc7f2g"
Topic: Future of Artificial Intelligence  
Tone: Professional  
Format: Blog Post  
Word Limit: 500
```

---

## ⚠️ Common Errors & Fixes

### ❌ `client not defined`

✔ Ensure `client` is initialized in `llm_helper.py`

---

### ❌ API Key Error

✔ Set `GROQ_API_KEY` correctly

---

### ❌ Model Decommissioned

✔ Use a valid model:

```id="tq0mtn"
llama3-8b-8192
```

---

## 📌 Future Improvements

* Content templates (SEO blogs, product descriptions)
* Hashtag suggestions for social media
* Image generation support
* Save & download content
* Multi-language generation

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Groq API
* Streamlit
* Open-source community

---

## 📧 Contact

**Thirumal Jeegari**
📍 India
📧 [thirumaljeegari21@example.com](mailto:thirumaljeegari21@example.com)

---

⭐ If you found this project useful, give it a star on GitHub!
