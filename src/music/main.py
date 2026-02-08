#!/usr/bin/env python
import sys
import warnings
import argparse
from pathlib import Path
import re

from music.ui import launch_report_ui
from music.crew import Music

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)      # remove weird chars
    text = re.sub(r"[\s_-]+", "-", text)      # spaces -> hyphens
    return text.strip("-") or "run"

def run(topic: str,ui: bool):
    run_slug = slugify(topic)
    output_dir = Path("output") / run_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    inputs = {
        "topic": topic,
        "output_dir": str(output_dir),
    }

    result = Music().crew().kickoff(inputs=inputs)
    print(result.raw)

    if ui:
        launch_report_ui(str(output_dir))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the music crew")
    parser.add_argument("--topic", type=str, required=True, help="The topic of the music")
    parser.add_argument("--ui", action="store_true", help="Launch Gradio UI after run")
    args = parser.parse_args()

    
    run(args.topic, args.ui)