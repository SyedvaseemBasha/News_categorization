from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

# Set Groq API key (you can also use st.secrets or .env for deployment)
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(groq_api_key=groq_api_key, model="llama-3.1-8b-instant")  # Use the appropriate model


def classify_news_article(article_text):
    # Classification Prompt
    classification_prompt = PromptTemplate(
            input_variables=["article"],
            template="""
        You are a strict classification model.

        Given the news article below, classify it into **one and only one** of the following categories:
        [Politics, Sports, Technology, Health, Entertainment, Science, Business]

        ⚠️ Very Important: Output ONLY the category name. NO explanation. NO sentences. NO justification.

        News Article:
        {article}

        ### CATEGORY:
        """
        )



    # Create the chain
    classification_chain = classification_prompt | llm | StrOutputParser()
    # Run the chain
    category = classification_chain.invoke({"article": article_text})
    return category
