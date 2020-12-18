import logging

import requests
from requests import Response

from lib.author import Author

from typing import List


class InfoCollector(object):
    """
    Collects information from various data sources: CrossRef, Pubmed

    Attributes:
        title (str): Title of the work
        authors (List[Author]): Array of Author objects
    """
    # API URLs
    # Pubmed API URL
    api_pubmed = r"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    # CrossRef API URL
    api_crossref = r"https://api.crossref.org/works/"

    def __init__(self, DOI: str = "10.2196/12121"):
        """
        The constructor for InfoCollector class

        Parameters:
            DOI(str): Full DOI number
        """
        self.title: str = ""
        self.authors: List[Author] = []

        self.DOI = DOI

    def get_crossref_api_url(self) -> str:
        """
        Formulates the API URL using the API URL and DOI number

        Returns
            (str): Full API URL for request
        """
        return f"{self.api_crossref}{self.DOI}"

    def _collect_crossref_data(self) -> bool:
        """
        Collects data using various apis including: Crossref and Pubmed

        Returns: 
            (bool): Whether successful in collection
        """
        try:
            # Get the formalated URL
            url: str = self.get_crossref_api_url()

            # Make a request to the REST API
            response: Response = requests.get(url)

            if (response.status_code == 200):
                data: dict = response.json()

                if (data['status'] == 'ok'):
                    # Extract the main content (e.g. title, authors)
                    # and remove other info (type and version info)
                    message: dict = data['message']
                    # Extract the title from the resposne
                    self.title = message['title'][0]

                    # Go through all the authors in the
                    # response and create Author objects
                    for author in message['author']:
                        # Retreives the ORC ID from the URL
                        # provided (e.g. http://orcid.org/0000-0001-6056-6071)
                        orcid = author['ORCID'].split('/')[-1]

                        # Create new Author object
                        new_author: Author = Author(author['given'],
                                                    author['family'],
                                                    orcid)

                        # Append the author object
                        self.authors.append(new_author)

                    return True

            return False
        except BaseException:
            # Catch all errors for now
            logging.warn(
                'An exception was raised during getting information using the Crossref api'
            )
            return False

    def collect_info(self) -> bool:
        """
        Gathers information from the sources

        Returns:
            (bool): Whether successful in collecting data
        """

        # Use Crossref to collect data
        return self._collect_crossref_data()

    def toJSON(self) -> dict:
        """
        Converts the object to JSON Serializable Object

        Returns:
            json(dict): JSON serializable object
        """
        # Initialize it with self attributes
        json: dict = self.__dict__

        # Fix authors since they are Author objects
        # and won't output correctly
        json['authors'] = [author.__dict__ for author in self.authors]

        # Return the dictionary
        return json
