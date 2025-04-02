def vina_output_writer(box):
    content = ''
    for key, value in box.items():
        content += f'{key}={value}\n'
    return content.strip("\n")