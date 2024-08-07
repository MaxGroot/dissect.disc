class Error(Exception):
    pass


class NotADirectoryError(Error):
    pass


class FileNotFoundError(Error):
    pass


class NotASymlinkError(Error):
    pass


class NotAFileError(Error):
    pass


class NotUDFError(Error):
    pass


class NotRockridgeError(Error):
    pass
