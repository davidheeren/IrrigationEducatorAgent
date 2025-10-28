# SRT to VTT Conversion

This script converts SubRip (`.srt`) caption files to WebVTT (`.vtt`) format.

## Command-Line Examples

### Show Help

To see all available command-line options, use the `--help` flag:

```bash
python srt2vtt.py --help
```

### Basic Usage

Convert a single `.srt` file. The output `.vtt` file will be created in the current directory.

```bash
python srt2vtt.py captions_test/example_close_captions.srt
```

### Advanced Usage

Convert multiple `.srt` files using a glob pattern and specify an output directory.

```bash
python srt2vtt.py captions_test/*.srt -o captions_test/
```
