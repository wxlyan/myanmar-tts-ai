from gtts import gTTS
import gradio as gr

def text_to_speech(text, voice):
    if not text.strip():
        return None

    filename = "output.mp3"

    tts = gTTS(
        text=text,
        lang="my",
        slow=False
    )

    tts.save(filename)

    return filename

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 🇲🇲 Myanmar TTS AI
        Convert Myanmar Text to Voice
        """
    )

    text_input = gr.Textbox(
        lines=8,
        label="Text Input",
        placeholder="မြန်မာစာ ရိုက်ထည့်ပါ..."
    )

    voice_select = gr.Dropdown(
        choices=[
            "Female Voice",
            "Male Voice"
        ],
        value="Female Voice",
        label="Voice Type"
    )

    generate_btn = gr.Button(
        "🎤 Generate Voice",
        variant="primary"
    )

    audio_output = gr.Audio(
        label="Generated Audio",
        type="filepath"
    )

    download_output = gr.File(
        label="⬇ Download MP3"
    )

    generate_btn.click(
        fn=text_to_speech,
        inputs=[text_input, voice_select],
        outputs=[audio_output, download_output]
    )

demo.launch()
