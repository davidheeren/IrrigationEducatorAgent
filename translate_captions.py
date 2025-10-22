#!/bin/env python

import webvtt
import time
import argparse
from pathlib import Path
from src import agent_helper, path_helper
from agents import Runner, Agent


def translate(agent: Agent, language: str, caption: str, prev_caption: str, next_caption: str) -> str:
    # prompt = f"""
    #     Translate the following caption text into the {language} language.
    #     Do not translate the previous and next captions. Only use them for context.
    #     Previous: {prev_caption}
    #     Caption: {caption}
    #     Next: {next_caption}
    # """
    # return Runner.run_sync(agent, prompt).final_output
    time.sleep(1)
    return "".join(c.swapcase() if c != "\f" else c for c in caption)


def get_args():
    parser = argparse.ArgumentParser(
        description="Simple CLI tool to tranlate .vtt files into other languages using the Irrigation Educator Agent")

    # Positional args use metavar whats shown and optional args use dest

    parser.add_argument(
        "input_path", help="The path to the vtt file", metavar="input-path")

    parser.add_argument("-o", "--output-dir",
                        help="The path to the output directory",
                        dest="output_dir",
                        default="./")

    parser.add_argument("-l", "--languages",
                        help="List of languages seperated by commas",
                        default="Spanish,French")

    parser.add_argument("-n", "--num-lines",
                        help="How many lines of text are to be translated in one request",
                        dest="num_lines",
                        type=int,
                        default="5")

    return parser.parse_args()


def main():

    args = get_args()

    output_dir = Path(args.output_dir).resolve()
    languages = args.languages.replace(" ", "").split(",")
    config_path = path_helper.get_config_path(__file__, "agent_translate.json")

    agent = agent_helper.get_and_configure_agent(config_path, [])

    for lang_index, language in enumerate(languages):
        vtt = webvtt.read(args.input_path)

        for i in range(0, len(vtt), args.num_lines):
            block = vtt[i:i+args.num_lines]
            caption = "\f".join(c.text for c in block)
            prev_caption = vtt[i-1].text if i > 0 else ""
            next_caption = vtt[i+args.num_lines].text if i + \
                args.num_lines < len(vtt) else ""

            # print(f"PREVIOUS: {prev_caption}")
            # print(f"CURRENT: {caption}")
            # print(f"NEXT: {next_caption}")
            # print("--------")

            chunk_num = i // args.num_lines
            progress = 100 * (lang_index + chunk_num /
                              len(languages)) / len(languages)
            print(f"Progress: {progress:.1f}%", end="\r")

            translation = translate(
                agent, language, caption, prev_caption, next_caption)
            translated_lines = translation.split("\f")

            for c, t in zip(block, translated_lines):
                c.text = t

        # for caption in vtt:
            # print(caption.identifier)
            # print(caption.start)
            # print(caption.end)
            # caption.text += f" -- test::{language}"
            # print(caption.text)
            # print(caption.voice)

        file_name = Path(args.input_path).stem + f"_{language}.vtt"
        path = output_dir / file_name
        print(f"Saving file: {path}")
        vtt.save(path)


if __name__ == "__main__":
    main()
