import os

input_folder = 'input'
output_file = 'export.txt'

def get_relative_path(file_path):
    return './' + os.path.relpath(file_path, input_folder)

with open(output_file, 'w', encoding='utf-8') as export_file:
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = get_relative_path(file_path)

            export_file.write(f'{relative_path}\n')

            with open(file_path, 'r', encoding='utf-8') as current_file:
                export_file.write(current_file.read() + '\n')
