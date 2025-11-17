import gradio as gr
import os

def ping():
    return "pong!"

with gr.Blocks() as demo:
    btn = gr.Button("Ping")
    out = gr.Textbox(label="Result")

    btn.click(fn=ping, outputs=out)

    demo.load(
        js="""
        () => {
            document.querySelector('button').addEventListener('click', () => {
                alert("Pong!");
            });
        }
        """
    )

# Render 기본 포트 가져오기
port = int(os.environ.get("PORT", 10000))

demo.launch(
    server_name="0.0.0.0",
    server_port=port,
    show_error=True,
    quiet=False,
    inline=False  # <- 이것이 Render에서 매우 중요!
)
