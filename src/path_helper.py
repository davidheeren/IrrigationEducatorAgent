from pathlib import Path


def get_config_path(root_file: str, config_name: str) -> str:
    # root_file arg should be the __file__ var from a script in the project root
    return Path(root_file).parent / f"config/{config_name}"
