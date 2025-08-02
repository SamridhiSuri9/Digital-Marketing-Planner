import gradio as gr
from workflows.campaign_workflow import run_campaign_workflow

def generate_plan(topic):
    status = "Processing... Please wait."
    yield status, ""  # Show processing message

    result = run_campaign_workflow(topic)
    output = f"""### 🎯 Target Audience
{result['Target Audience']}

### 🗓 Content Strategy
{result['Content Strategy']}

### ✍️ Marketing Posts
{result['Marketing Posts']}"""

    yield "", output  # Clear status and show result

with gr.Blocks(title="🧠 Digital Marketing Planner (CrewAI)") as demo:
    gr.Markdown("# 🧠 Digital Marketing Planner")
    gr.Markdown("Generate a complete marketing strategy including audience insights, content calendar, and social posts.")

    with gr.Row():
        topic_input = gr.Textbox(label="Enter a product or topic", placeholder="e.g. Eco-Friendly Water Bottles", lines=1)
        submit_btn = gr.Button("Generate")

    status_output = gr.Label(value="")
    markdown_output = gr.Markdown()

    submit_btn.click(fn=generate_plan, 
                     inputs=topic_input, 
                     outputs=[status_output, markdown_output],
                     show_progress=False)  # show_progress is optional

if __name__ == "__main__":
    demo.launch()
