from pathlib import Path


# root_file arg should be the __file__ var from a script in the project root
def get_config_path(root_file: str, config_name: str) -> str:
    return Path(root_file).parent / f"config/{config_name}"
