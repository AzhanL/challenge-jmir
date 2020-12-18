class Author(object):
    """
    Author object stores details about the author

    Attributes:
        first_name (str): First Name
        last_name (str): Last Name
        orcid (str): ORC ID
    """
    def __init__(self, first_name: str, last_name: str, orcid: str = None):
        # First Name
        self.first_name = first_name
        # Last Name
        self.last_name = last_name
        # ORC ID
        self.orcid = orcid
