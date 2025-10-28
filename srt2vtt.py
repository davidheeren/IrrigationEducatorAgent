#!/bin/env python

from srt_to_vtt import srt_to_vtt
from pathlib import Path
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Convert srt files to vtt")

    parser.add_argument("input_paths",
                        nargs='+',  # one or more args
                        help="List paths to the srt files",
                        metavar="input-paths")

    parser.add_argument("-o", "--output-dir",
                        help="The path to the output directory",
                        dest="output_dir",
                        default="./")

    return parser.parse_args()


def main():
    args = get_args()

    output_dir = Path(args.output_dir).resolve()
    if not output_dir.is_dir():
        print(f"Error: output directory {output_dir} does not exist. Exiting")
        return

    for path in args.input_paths:
        path = Path(path).resolve()
        if not path.is_file():
            print(f"Error: input path {path} does not exist. Skipping")
            continue

        # convert 'path' extension to .vtt and and in output_dir
        output_path = output_dir.joinpath(path.name).with_suffix(".vtt")

        srt_to_vtt(path, output_path)

        print(f"converted: {output_path}")


if __name__ == "__main__":
    main()
