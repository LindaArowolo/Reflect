IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()


def is_valid_image_file(filename):
    return '.' in filename and get_file_extension(filename) in IMAGE_EXTENSIONS
