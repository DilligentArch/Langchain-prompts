from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import os
import streamlit as st

load_dotenv()


st.header('Reasearch Tool')
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

api_key=os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(
    model="gpt-4",
    api_key=api_key,
    temperature=0.7
)



#  template=PromptTemplate(
#     template="""
# Please summerize the  research paper titled "{paper_input}" with the following specification:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1.Mathmetical Details:
# -Include relevent mathmetical equations if present in the paper.
# -Explain the mathmetical concepts using simple,intuitive code snippets where applicable.
# 2.Analogies:
# -Use relatble analogies to simplify complex ideas.
# If certain information is not available in the paper, respond with "Insufficient information available" instead of guessing.
# Ensure the summery is clear, accurate  and aligned with the provided style  and length.
# """,
# input_variables=['paper_input','style_input','length_input'],
# validate_template=True

# )

template=load_prompt("template.json")
prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})



if st.button('Summerize'):
    result=model.invoke(prompt)
    st.write(result.content)