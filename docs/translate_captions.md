# Translating Captions

This script uses the AI agent to translate WebVTT (`.vtt`) caption files into one or more languages.

## Usage Example

To translate a file named `captions.vtt` into Spanish and French, and save the output to a `translated/` directory:

```bash
python translate_captions.py captions.vtt -l "Spanish,French" -o translated/
```

## Command-Line Options

| Option        | Long Option                      | Description                                           | Default                       |
|---------------|----------------------------------|-------------------------------------------------------|-------------------------------|
| `input_paths` | *(positional)*   | One or more paths to the `.vtt` files to translate.   | *(required)*                  |
| `-o`          | `--output-dir`   | The directory where translated files will be saved.   | `./`                          |
| `-t`          | `--test`         | Run in test mode without calling the AI API.          | False                      |
| `-l`          | `--languages`    | Comma-separated list of languages for translation.    | `Spanish,French,Portuguese,Arabic,Chinese,Hindi,Swahili,German,Persian,Russian`   |
| `-n`          | `--num-captions` | The number of captions to batch in a single request.  | `20`                           |
