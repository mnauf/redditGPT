import gradio as gr
from sample import generate_text

badges = """
<div style="display: flex">
<span style="margin-right: 5px"> 
<a href="https://www.linkedin.com/in/mnauf/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/LinkedIn_Logo.svg/2560px-LinkedIn_Logo.svg.png" alt="Linkedin" width=100 height=auto> </a>
</span>
<span style="margin-right: 5px"> 
 <a href="https://github.com/mnauf/redditGPT" target="_blank"> <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="Github"> </a>
</span>
<span style="margin-right: 5px"> 
 <a href="https://twitter.com/MNaufil" target="_blank"> <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white" alt="Twitter"> </a>
</span>
</div>
"""

description="""GPT2 finetuned on recent public anonymous conversations from Reddit to capture public sentiments regarding the recent unfolding events in Pakistan. Since the genaral public is afraid of speaking publicly with their identities exposed because of the crackdown, Reddit is the most genuine source we can get to understand the public sentiments. Data is collected from Pakistan, AskMiddleEast and WorldNews Reddit communities from last year until 25th May 2023."""
with gr.Blocks() as block:
    # gr.Markdown("""![Imgur](https://i.imgur.com/iPZlUa8.png)""")
    gr.HTML("<img src=https://i.imgur.com/iPZlUa8.png width=auto height=200>")
    gr.Markdown(badges)
    gr.Markdown(description)
    with gr.Row():
        input_text = gr.Textbox(
            label="Input Text",
            lines=1,
            value="Imran Khan arrest",
            elem_id="input_text"
        )

        output_text = gr.Textbox(
            label="Output",
            lines=10,
            value="",
            elem_id="input_text"
        )

    inputs = [input_text]
    outputs = [output_text]

    run_button = gr.Button(
        value="Generate Text",
    )

    run_button.click(
        fn=generate_text,
        inputs=inputs,
        outputs=outputs,
        queue=True
    )
block.queue(concurrency_count=5).launch(server_name="localhost", share=True)