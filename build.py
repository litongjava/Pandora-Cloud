import os
import platform


def construct_pyinstaller_command():
    # Get the system name (e.g., 'Windows', 'Linux', 'Darwin' for macOS, etc.)
    system_name = platform.system()

    # Get the detailed architecture identifier
    arch_name = platform.machine()

    output_name="pandora-cloud"
    # Construct the output name
    output_folder_name = f"{output_name}-{system_name.lower()}-{arch_name}"

    # Determine the appropriate path separator for --add-data based on the OS
    path_separator = ";" if system_name == "Windows" else ":"

    # Specify the output directory for the bundled app
    dist_path = f"dist/{output_folder_name}"

    # Construct the PyInstaller command
    command = (f'pyinstaller --onefile --name {output_name} '
               f'--distpath {dist_path} '
               f'--add-data "src/pandora_cloud/flask/static{path_separator}flask/static" '
               f'--add-data "src/pandora_cloud/flask/templates{path_separator}flask/templates" main.py')

    return command


if __name__ == "__main__":
    pyinstaller_command = construct_pyinstaller_command()
    print(pyinstaller_command)
    os.system(pyinstaller_command)
