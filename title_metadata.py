import logging

class TitleMetadata():
  def __init__(self):
    """
    title: str
      Title
    description: str
      Description
    categories: Set[str]
      Categories
    chapter_numbers: List[str]
      Chapter numbers, uses a list because
      we care about the order they appear on the site
      rather than simple sorting
    chapter_urls: List[str]
      Urls corresponding to the chapter_numbers
    """
    self.title = None
    self.description = None
    self.categories = set()
    self.chapter_numbers = []
    self.chapter_urls = []
  
  def set_title(self, title):
    self.title = title
  
  def set_description(self, description):
    self.description = description
  
  def add_category(self, category):
    self.categories.add(category.lower())
  
  def add_chapter_number(self, chapter_number, url):
    self.chapter_numbers.append(chapter_number)
    self.chapter_urls.append(url)
  
  def dump(self):
    logging.info("Title: " + str(self.title))
    logging.info("==========")
    
    logging.info("Description: " + str(self.description))
    logging.info("==========")

    categories_str = ""
    for c in sorted(list(self.categories)):
      categories_str += "\t" + c + "\n"
    logging.info("Categories:\n" + categories_str)
    logging.info("==========")

    chapters_str = ""
    for n, u in zip(self.chapter_numbers, self.chapter_urls):
      chapters_str += "\t" + n + ":" + u + "\n"
    logging.info("Chapter Numbers:\n" + chapters_str)

