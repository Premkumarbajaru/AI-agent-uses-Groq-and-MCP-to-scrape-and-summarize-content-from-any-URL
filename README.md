---

# 🧠 AI Agent using Groq and MCP to scrape and summarize content from any URL


This Python-based CLI tool allows users to extract and summarize content from a URL (web pages) using a Groq-powered LLaMA 3.3 70B model, integrated with an MCP server.

---

## 🚀 Features

- ✅ **User Prompt Input** – Accepts any URL from the command line.
- 🤖 **AI-Powered Summarization** – Uses `groq:llama-3.3-70b-versatile` via `pydantic_ai`.
- 🔌 **Asynchronous Execution** – Fast, non-blocking operations using Python's `asyncio`.
- 🔐 **Secure API Key Handling** – Loads your Groq API key safely from a `.env` file.
- 🧩 **Modular Design** – Cleanly separates MCP server config, agent setup, and main logic.

---

## 📦 Installation

### 1. Clone this repository:
```bash
git clone https://github.com/Premkumarbajaru/AI-agent-uses-Groq-and-MCP-to-scrape-and-summarize-content-from-any-URL.git
cd main.py
```

### 2. Create and activate a virtual environment:
```bash
python -m venv venv
.\.venv\Scripts\activate
```

### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file:
Create a `.env` file in the root directory and add your Groq API key:
```
GROQ_API_KEY=gsk_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 🧪 Usage

Run the tool from your terminal:

```bash
python main.py
```

You'll be prompted to enter a URL. The AI will then extract and summarize the content of the page.

---

## 🛠 Dependencies

- `pydantic_ai`
- `python-dotenv`
- `asyncio`
- `Python 3.8+`
---

## 💡 Example

```bash
$ python main.py
Enter the URL to extract and summarize: https://en.wikipedia.org/wiki/History_of_artificial_intelligence
```

Output:
```bash
summarize: https://en.wikipedia.org/wiki/History_of_artificial_intelligence

The Wikipedia article on the "History of Artificial Intelligence" provides a comprehensive overview of the development of AI from its inception to the present day. Here's a summary of the content:

Early Beginnings (1950s-1960s)

1. The term "Artificial Intelligence" was coined in 1956 by John McCarthy.
2. The first AI program, called Logical Theorist, was developed in 1956 by Allen Newell and Herbert Simon.
3. The first AI conference was held in 1956 at Dartmouth College.
4. The development of the first AI languages, such as Lisp and Prolog, took place during this period.

Rule-Based Expert Systems (1970s-1980s)

1. The introduction of rule-based expert systems, which mimicked human decision-making abilities, marked a significant milestone in AI development.
2. The development of expert systems like MYCIN (1976) and DENDRAL (1969) demonstrated the potential of AI in various domains.      
3. The emergence of knowledge engineering and the use of rule-based systems in commercial applications.

AI Winter (1980s-1990s)

1. The AI winter, a period of reduced interest and funding in AI research, occurred due to the limitations of rule-based systems and the lack of significant progress.
2. The development of new approaches, such as machine learning and artificial neural networks, helped to revitalize AI research.    

Machine Learning and Resurgence (1990s-2000s)

1. The introduction of machine learning algorithms, such as support vector machines and random forests, enabled AI systems to learn from data.
2. The development of artificial neural networks, including convolutional neural networks (CNNs) and recurrent neural networks (RNNs), led to significant advancements in image and speech recognition.
3. The resurgence of interest in AI, driven by the success of machine learning and the availability of large datasets.

Deep Learning and Current Developments (2010s-present)

1. The development of deep learning techniques, such as deep neural networks (DNNs) and long short-term memory (LSTM) networks, has led to state-of-the-art performance in various AI tasks.
2. The application of AI in areas like natural language processing, computer vision, and robotics has become increasingly prevalent.
3. The emergence of new AI applications, such as autonomous vehicles, chatbots, and smart homes, has transformed various industries and aspects of daily life.

Key Milestones and Events

1. 1950: Alan Turing proposes the Turing Test to measure a machine's ability to exhibit intelligent behavior.
2. 1956: The first AI program, Logical Theorist, is developed.
3. 1965: The first AI language, Lisp, is developed.
4. 1969: The first expert system, DENDRAL, is developed.
5. 1980: The first AI winter begins.
6. 1997: IBM's Deep Blue defeats the world chess champion, Garry Kasparov.
7. 2011: IBM's Watson wins the Jeopardy! quiz show.
8. 2014: Google acquires DeepMind, a leading AI research organization.

The history of artificial intelligence is a rich and complex narrative, spanning multiple decades and involving the contributions of numerous researchers, scientists, and engineers. From its early beginnings to the current state-of-the-art, AI has evolved significantly, with ongoing advancements in machine learning, deep learning, and other areas continuing to shape the field.
```

---

## 📁 File Structure

```
.
├── main.py               # Main script to run the summarizer
├── .env                  # Environment file to store API key
├── requirements.txt      # Python package dependencies
└── README.md             # This file
```

---

## 🛡️ Security Note

Your Groq API key is sensitive — keep your `.env` file private and **never commit it to version control**.

---
