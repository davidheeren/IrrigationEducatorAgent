# Translating Captions

This script uses the AI agent to translate WebVTT (`.vtt`) caption files into one or more languages.

*Note: If you have SubRip (`.srt`) files, you must first convert them to WebVTT format. See the [SRT to VTT Conversion](srt2vtt.md) documentation.*

## Command-Line Examples

### Show Help

To see all available command-line options, use the `--help` flag:

```bash
python translate_captions.py --help
```

### Basic Usage

Translate a single caption file into the default set of languages:

```bash
python translate_captions.py captions_test/example.vtt
```

### Advanced Usage

Translate multiple `.vtt` files using a glob pattern, specify a comma-separated list of languages, and set a custom output directory:

```bash
python translate_captions.py captions_test/*.vtt -l "Spanish,French" -o translated_captions/
```
