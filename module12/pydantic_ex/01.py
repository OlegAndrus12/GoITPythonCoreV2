from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class Person(BaseModel):
    model_config = ConfigDict(strict=True, alias_generator=to_camel)

    first_name: str
    last_name: str
    age: int

data = """
        {   
            "yearsOfExperience": 20, 
            "firstName": "Isaac",
            "lastName": "Newton",
            "age": 44
        }
        """

user = Person.model_validate_json(data)
print(user.age)
