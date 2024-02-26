import ratemyprofessor
import requests
import ratemyprofessor
from bs4 import BeautifulSoup
from collections import Counter

INFO_NOT_AVAILABLE = "Info currently not available"
 
class rate_my_prof():

    def __init__(self, name="staff"):
        self.name = name
        self.department = ""
        self.school = ""
        self.rating = ""
        self.difficulty = ""
        self.num_ratings = ""
        self.id = ""
        self.would_take_again = ""
        self.tags = ""
        self.reviews = ""

    def retrieveRMPInfo(self):
        professor = ratemyprofessor.get_professor_by_school_and_name(
        ratemyprofessor.get_school_by_name("Duke University"), self.name)
        if professor is not None:
            self.name = professor.name
            self.department = professor.department
            self.school = professor.school.name
            self.rating = professor.rating
            self.difficulty = professor.difficulty
            self.num_ratings = professor.num_ratings
            self.id = professor.id
            self.would_take_again = professor.would_take_again
            self.tags = self.getTags()
            self.reviews = self.getReviews()
        else:
            self.name = INFO_NOT_AVAILABLE
            self.department = INFO_NOT_AVAILABLE
            self.school = INFO_NOT_AVAILABLE
            self.rating = INFO_NOT_AVAILABLE
            self.difficulty = INFO_NOT_AVAILABLE
            self.num_ratings = INFO_NOT_AVAILABLE
            self.id = INFO_NOT_AVAILABLE
            self.would_take_again = INFO_NOT_AVAILABLE
            self.tags = INFO_NOT_AVAILABLE
            self.reviews = INFO_NOT_AVAILABLE

    # Get tags
    def getTags(self):
        
        url = ("https://www.ratemyprofessors.com/professor/%s" % self.id)

        page = requests.get(url=url)
        page_data = page.text
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(page_data, 'html.parser')

        # Find all occurrences of the specified span tag
        tag_spans = soup.find_all('span', class_='Tag-bs9vf4-0 hHOVKF')

        # Extract and count the occurrences of each tag
        tag_counter = Counter(span.text.strip() for span in tag_spans)

        # Create a dictionary and sort it by values
        sorted_tags_dict = dict(sorted(tag_counter.items(), key=lambda item: item[1], reverse=True))

        return sorted_tags_dict

    def getReviews(self):
        url = ("https://www.ratemyprofessors.com/professor/%s" % self.id)

        page = requests.get(url=url)
        page_data = page.text
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(page_data, 'html.parser')

        review_tags = soup.find_all('div', class_='Comments__StyledComments-dzzyvm-0 gRjWel')

        ALL_REVIEWS = []
        for tag in review_tags:
            tag_text = tag.text.strip()
            ALL_REVIEWS.append(tag_text)
        
        return ALL_REVIEWS