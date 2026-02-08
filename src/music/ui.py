from pathlib import Path
import gradio as gr

def launch_report_ui(output_dir: str):
    out = Path(output_dir)
    if not out.exists():
        raise FileNotFoundError(f"Output dir not found: {out}")

    md_files = sorted(out.glob("*.md"))
    if not md_files:
        raise FileNotFoundError(f"No .md files found in: {out}")

    with gr.Blocks(title=f"Music Crew Reports - {out.name}") as demo:
        gr.Markdown(f"# 🎧 Music Crew Reports\n\n**Folder:** `{out}`")

        with gr.Tabs():
            for f in md_files:
                title = f.stem.replace("_", " ").replace("-", " ").title()
                with gr.Tab(title):
                    content = f.read_text(encoding="utf-8", errors="ignore")
                    gr.Markdown(content)

    demo.launch()
