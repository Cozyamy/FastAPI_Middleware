import magic

def get_file_mime_type(file):
    """
    Determines the MIME type of a file.

    Parameters:
        file (bytes): The content of the file as bytes.

    Returns:
        str: The MIME type of the file.
    """
    mime = magic.Magic(mime=True)
    return mime.from_buffer(file)