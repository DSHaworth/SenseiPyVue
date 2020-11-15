class ResponseHandler():
    """Generic Response Handler for valid and invalid responses"""
    def __init__(self, payload = None, errorMessage = None):
        self.isValid = not errorMessage
        self.errorMessage = errorMessage
        self.payload = payload

    def toJSON(self):
        return self.__dict__
