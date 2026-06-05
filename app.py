from gtts import gTTS
import gradio as gr
import os

def text_to_speech(text):
    if not text:
        return None

    filename = "output.mp3"

    tts = gTTS(
        text=text,
        lang="my"
    )

    tts.save(filename)

    return filename

app = gr.Interface(
    fn=text_to_speech,
    inputs=gr.Textbox(
        lines=8,
        label="မြန်မာစာရိုက်ပါ"
    ),
    outputs=gr.Audio(
        label="အသံထွက်"
    ),
    title="Myanmar TTS AI",
    description="မြန်မာစာကို အသံထွက်ပြောင်းပေးသော AI"
)

app.launch()
