#!/bin/env python

import webvtt
import time
import argparse
from pathlib import Path
from src import agent_helper, path_helper
from agents import Runner, Agent

DELIMTITER = "|||"


def translate(agent: Agent, language: str, caption: str, args) -> str:
    prompt = f"""
        The following text contains multiple captions separated by the string {DELIMTITER}.
        Translate each caption into the {language} language.
        The ONLY occurrences of {DELIMTITER} in your output MUST be as separators between translated captions. You MUST ensure that the number of {DELIMTITER} strings in your output is EXACTLY one less than the number of captions provided in the input. **IMPORTANT: Each translated caption MUST retain its original internal newlines. Do NOT remove or replace newlines within a caption.**

        Caption text to translate:
        {caption}
    """
    if (args.test):
        time.sleep(.75)
        # Split the caption by the delimiter, swap case of each part, then re-join
        parts = caption.split(DELIMTITER)
        translated_parts = [p.swapcase() for p in parts]
        return DELIMTITER.join(translated_parts)
    else:
        return Runner.run_sync(agent, prompt).final_output


def get_args():
    parser = argparse.ArgumentParser(description="Simple CLI tool to tranlate .vtt files into other languages using the Irrigation Educator Agent")

    # Positional args use metavar whats shown and optional args use dest

    parser.add_argument("input_paths",
                        nargs='+',  # one or more args
                        help="List paths to the vtt files",
                        metavar="input-paths")

    parser.add_argument("-o", "--output-dir",
                        help="The path to the output directory",
                        dest="output_dir",
                        default="./")

    parser.add_argument("-t", "--test",
                        help="Flag to not call the api. Flips character case instead",
                        action="store_true")

    parser.add_argument("-l", "--languages",
                        help="List of languages seperated by commas",
                        # default="Spanish")
                        default="Spanish,French,Portuguese,Arabic,Chinese,Hindi,Swahili,German,Persian,Russian")

    parser.add_argument("-n", "--num-captions",
                        help="Number of captions to be translated in one request",
                        dest="num_captions",
                        type=int,
                        default="20")

    return parser.parse_args()


def main():
    args = get_args()

    output_dir = Path(args.output_dir).resolve()
    if not output_dir.is_dir():
        print(f"Error: output directory {output_dir} does not exist. Exiting")
        return

    languages = args.languages.replace(" ", "").split(",")

    config_path = path_helper.get_config_path(__file__, "agent_translate.json")
    if not Path(config_path).is_file():
        print(f"Error: config path {config_path} does not exist. Exiting")
        return

    agent = agent_helper.get_and_configure_agent(config_path, [])

    # how many captions above and below the current block for context
    num_padding = 1

    progress = 0

    ignore_paths = set()

    # find total captions for progress
    total_captions = 0
    for input_path in args.input_paths:
        if not Path(input_path).is_file():
            ignore_paths.add(input_path)
            continue

        for language in languages:
            vtt = webvtt.read(input_path)
            total_captions += len(webvtt.read(input_path))

    for input_index, input_path in enumerate(args.input_paths):
        if input_path in ignore_paths:
            print(f"Error: path '{input_path}' does not exist. Skipping to next path")
            continue

        for lang_index, language in enumerate(languages):
            vtt = webvtt.read(input_path)

            for i in range(0, len(vtt), args.num_captions):
                # list slices end will clamp to length but if start is negative it will wrap
                # end in list slices are exclusive

                # start and end vars for the captions block including padding
                start = max(0, i - num_padding)
                end = i + args.num_captions + num_padding
                block = vtt[start:end]

                # join all captions in block sperated by delimiter
                caption = DELIMTITER.join(c.text for c in block)

                # start and end for the non padding slice of the current block
                # took forever to figure out the logic here. there might be a better way to structure this
                start_range = i - start
                end_range = min(len(vtt), i + args.num_captions) - start

                # print progress
                print(f"\rProgress: {progress:5.0f}%", end="\r", flush=True)
                progress += (end_range - start_range) / total_captions * 100
                progress = min(100, progress)

                translation = translate(agent, language, caption, args)
                # split on delimiter and strip leading and trailing whitespace
                translated_lines = [
                    line.strip() for line in translation.split(DELIMTITER)]

                # double check same amount of delimiters. AI can be finicky
                if (len(translated_lines) != len(block)):
                    print(f"ERROR: Mismatch in delimiter count. AI has messed up. Aborting current file: {
                        input_path} language: {language}")
                    return

                # update the vtt object
                for c, t in zip(block[start_range:end_range], translated_lines[start_range:end_range]):
                    c.text = t

            # save vtt object to file
            file_name = output_dir / f"{Path(input_path).stem}_{language}.vtt"
            path = output_dir / file_name
            print(f"Saving file: {path}")
            vtt.save(path)


if __name__ == "__main__":
    main()
