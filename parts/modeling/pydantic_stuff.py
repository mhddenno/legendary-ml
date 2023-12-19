import pydantic
from typing import Optional, List
import json
import logging
import pdb
from pydantic_core import PydanticCustomError
from icecream import ic

class ISBN10AndISBN13MissingError(Exception):
    def __init__(self, title:str, message:str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)
        

class ISBN10FormatError(Exception):
    def __init__(self, title:str, message:str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)

def process_topic(topic: dict) -> Optional[dict]:
    try:
        ic()
        return Topic(**topic)
    except pydantic.ValidationError:
        #pdb.set_trace()
        ic(f"Processing topic: {topic['title']} didn't work.")
        logging.error(f"Processing topic: {topic['title']} didn't work.")
        return None

class Co_author(pydantic.BaseModel):
    name: str
    age: int

class Topic(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    price: Optional[float]
    co_author: Optional[Co_author]

    @pydantic.model_validator(mode='after')
    def check_if_both_ibsn_exist(self) -> None:
        ic()
        try:
            if not hasattr(self,'isbn_10') or not hasattr(self, 'isbn_13'):
                raise ISBN10AndISBN13MissingError('Something', "Both ISBN10 and ISBN13 are missing.")
        except ISBN10AndISBN13MissingError as s:
            ic('check_if_both_ibsn_exist')
        return self
        
    @pydantic.model_validator(mode='before')
    @classmethod
    def check_if_title_is_so_long(cls, values: any) -> None:
        ic()
        try:
            if len(values['title']) > 15:
                raise PydanticCustomError('Title is too long','sdf')
        except:
            ic('check_if_title_is_so_long')
        return values




def main() -> None:
    data_path = "data/modeling.json"
    ic()
    with open(data_path, "r") as f:
        data = json.load(f)
        #[print(topic) for topic in data]
        topics = [Topic(**topic) for topic in data if process_topic(topic) is not None] 
        #topics=[]
        #for topic in data:
        #    topics.append(Topic(**topic))

        #print(Topic.__pydantic_decorators__)

if __name__ == "__main__":
    main()


# """Custom error that is raised when both ISBN10 and ISBN13 are missing."""
# """Custom error that is raised when ISBN10 doesn't have the right format."""
# """Make sure there is either an isbn_10 or isbn_13 value defined"""
# """Validator to check whether ISBN10 is valid"""