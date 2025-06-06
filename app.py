import streamlit as st
from agents import Agent, Runner
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  # Load OPENAI_API_KEY from .env if present

# Mermaid Agent
mermaid_agent = Agent(
    name="mermaid_assistant",
    instructions="""
    You are a Business Process Visualization Assistant.

    Your task is to:
    1. Read a natural-language conversation between a business analyst and a client.
    2. Understand the key steps, decisions, and participants involved in the process discussed.
    3. Extract the workflow and convert it into a `Mermaid flowchart` using appropriate Mermaid syntax.
    4. Ensure nodes are labeled clearly and logically represent the process.
    5. Use decisions where applicable with "yes/no" branches.

    Input: A business conversation or meeting transcript.

    Output: A Mermaid flowchart code block that accurately represents the process.

    Example Output Format:
    ```mermaid
    flowchart TD
        A[Start] --> B[Step 1]
        B --> C{Decision?}
        C -- Yes --> D[Action for Yes]
        C -- No --> E[Action for No]
        D --> F[End]
        E --> F
    ```
    """,
    model="gpt-4o"
)

# Mermaid Renderer
def render_mermaid(mermaid_code: str):
    mermaid_code = mermaid_code.strip().replace("```mermaid", "").replace("```", "")
    html_code = f"""
    <div class="mermaid">
        {mermaid_code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    """
    st.components.v1.html(html_code, height=600, scrolling=True)

# Streamlit UI
st.set_page_config(page_title="Mermaid Diagram Generator", layout="wide")
st.title("🧠 Business Process to Mermaid Diagram")

with st.expander("ℹ️ Instructions"):
    st.markdown("""
    - Paste your **initial business discussion or transcript** in the first box.
    - If needed, provide **additional prompt** or clarification below.
    - Click **Generate Flowchart** to update the Mermaid diagram.
    """)

# Text areas
discussion = st.text_area("📝 Initial Business Discussion", height=300)
followup_prompt = st.text_area("➕ Additional Prompt / Clarification (optional)", height=150)

if st.button("🚀 Generate Flowchart"):
    if not discussion.strip():
        st.warning("Please enter a business conversation.")
    else:
        # Combine discussion and follow-up
        combined_input = discussion.strip()
        if followup_prompt.strip():
            combined_input += "\n\nAdditional Note:\n" + followup_prompt.strip()

        with st.spinner("Thinking and drawing..."):
            result = asyncio.run(Runner.run(mermaid_agent, input=combined_input))
            output = result.final_output

            if "```mermaid" in output:
                st.success("✅ Mermaid diagram generated!")
                st.subheader("🧾 Mermaid Code")
                st.code(output, language="mermaid")
                st.subheader("📊 Diagram")
                render_mermaid(output)
            else:
                st.warning("❗ The output doesn't contain valid Mermaid syntax.")
                st.text(output)
