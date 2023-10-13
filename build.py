import os
import platform


def construct_pyinstaller_command():
    # Get the system name (e.g., 'Windows', 'Linux', 'Darwin' for macOS, etc.)
    system_name = platform.system()

    # Get the architecture
    arch_name = platform.architecture()[0]

    # Construct the output name
    output_name = f"pandora-cloud-{system_name.lower()}-{arch_name}"

    # Determine the appropriate path separator for --add-data based on the OS
    path_separator = ";" if system_name == "Windows" else ":"

    # Construct the PyInstaller command
    command = (f'pyinstaller --onefile --name {output_name} '
               f'--add-data "src/pandora_cloud/flask/static{path_separator}flask/static" '
               f'--add-data "src/pandora_cloud/flask/templates{path_separator}flask/templates" main.py')

    return command


if __name__ == "__main__":
    pyinstaller_command = construct_pyinstaller_command()
    print(pyinstaller_command)
    os.system(pyinstaller_command)
