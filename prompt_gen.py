from langchain_core.prompts import PromptTemplate
template=PromptTemplate(
    template="""
Please summerize the  research paper titled "{paper_input}" with the following specification:
Explanation Style: {style_input}
Explanation Length: {length_input}
1.Mathmetical Details:
-Include relevent mathmetical equations if present in the paper.
-Explain the mathmetical concepts using simple,intuitive code snippets where applicable.
2.Analogies:
-Use relatble analogies to simplify complex ideas.
If certain information is not available in the paper, respond with "Insufficient information available" instead of guessing.
Ensure the summery is clear, accurate  and aligned with the provided style  and length.
""",
input_variables=['paper_input','style_input','length_input'],
validate_template=True

)
template.save("template.json" )