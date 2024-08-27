from langchain.output_parsers import ResponseSchema

choices_schema = ResponseSchema(name="choices",
                                type="list of strings",
                                description="List of strings containing the generated options.")

story_schema = ResponseSchema(name="story",
                              type="list of strings",
                              description="List of strings with only the new generated paragraphs of the story.")

title_schema = ResponseSchema(name="title",
                              type="string",
                              description="The title of the story.")