import gradio as gr

def ping():
    return "pong!"

with gr.Blocks() as demo:
    btn = gr.Button("Ping")
    out = gr.Textbox(label="Result")

    # Python 함수 실행
    btn.click(
        fn=ping,
        outputs=out
    )

    # JS 이벤트 바인딩 (Gradio 4.x: js= )
    demo.load(
        js="""
        () => {
            // 버튼 클릭 시 alert 실행
            document.querySelector('button').addEventListener('click', () => {
                alert("Pong!");
            });
        }
        """
    )

demo.launch()
