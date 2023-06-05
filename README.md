
## LangChain Quickstart App Tutorial
In the dynamic landscape of artificial intelligence (AI), generative AI and large language models (LLMs) have emerged as game-changers, revolutionizing how we process and understand massive amounts of text data. LLMs can be used for various tasks such as text generation, sentiment analysis, question answering, text summarization, document translation, and document classification.

If you're captivated by the transformative powers of generative AI and LLMs, then this LangChain how-to tutorial series is for you. This tutorial will introduce the concept of LangChain and guide you through building a simple LLM-powered Streamlit app in four steps:

1. Get an OpenAI API key
2. Set up the coding environment
3. Build the app
4. Deploy the app

## LangChain Overview
LangChain is a framework that leverages LLMs to build applications for various use cases. It was created by Harrison Chase and first released as an open-source project in October 2022. LangChain has gained significant popularity with 41,900 stars on GitHub and over 800 contributors.

At a high level, LangChain connects LLM models, such as OpenAI and HuggingFace Hub, with external sources like Google, Wikipedia, Notion, and Wolfram. It provides abstractions (chains and agents) and tools (prompt templates, memory, document loaders, output parsers) to facilitate interaction between text input and output. LangChain orchestrates the LLM pipeline, making it easy for developers to prototype robust applications by linking LLM models and components into a pipeline "chain."

## LangChain consists of seven key modules:
Models: Closed or open-source LLMs
Prompts: Templates for accepting user input and output parsers to format LLM model output
Indexes: Structures and prepares data for optimal interaction with LLM models
Memory: Enables chains or agents to have short-term and long-term memory of previous interactions with users
Chains: Combines multiple components or other chains into a single pipeline
Agents: Based on input, agents decide on the appropriate course of action using available tools and data
Callbacks: Functions triggered at specific points during an LLM run
Now, let's explore the functionality of the app.

To see the app in action, copy and paste your API key (refer to Step 1 below), and enter the prompt "What are the three key pieces of advice for learning how to code?" Then, click the "Submit" button. The response will appear in the blue box.

### Under the hood, the app utilizes OpenAI (LLM), LangChain (LLM framework), and Streamlit (web framework).

## Step-by-Step Guide
### Step 1: Get an OpenAI API Key
To obtain an OpenAI API key, follow these steps:

Go to https://platform.openai.com/account/api-keys.
Click on the "+ Create new secret key" button.
Optionally, enter an identifier name, then click on the "Create secret key" button.
Copy the API key for use in this tutorial. (Note: The displayed key below has already been revoked.)

### Step 2: Set up the Coding Environment
Local Development
To set up the coding environment locally, ensure you have a functional Python environment (e.g., Python >3.7) and install the following three Python libraries using pip:

```
pip install -r requirements.txt
```
### Step 3: Build the App

```
import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
```

To begin, create the streamlit_app.py file and import the two prerequisite libraries: streamlit and langchain.

Next, use the st.title() method to display the app's title, "🦜🔗 Quickstart App".

The app accepts the OpenAI API key from the user, which is used to generate the response.

Then, define a custom function called generate_response(). This function takes a piece of text as input, uses the OpenAI() method to generate AI-generated content, and displays the output inside a blue box using st.info().

Finally, use st.form() to create a text box (st.text_area()) for users to provide a prompt input. When the user clicks the "Submit" button, the generate_response() function is called with the prompt input variable (text) as an argument. The AI-generated content is then displayed.

Congratulations! Your app is now deployed.

