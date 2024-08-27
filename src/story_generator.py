from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import PromptTemplate

from src.schemas import choices_schema, story_schema, title_schema
from src.text_generator import TextGenerator


class StoryGenerator:
    PATH_TO_PROMPT_TITLE = "src/prompts/prompt_title.txt"
    PATH_TO_PROMPT_START = "src/prompts/prompt_start.txt"
    PATH_TO_PROMPT_CONTINUE = "src/prompts/prompt_continue.txt"
    PATH_TO_PROMPT_END = "src/prompts/prompt_end.txt"

    def __init__(self, model_name="open-mistral-7b", temperature=0.5):
        self.text_generator = TextGenerator(model_name, temperature)

    def generate_title(self):
        response_schemas = [title_schema]
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        prompt_title = PromptTemplate.from_file(StoryGenerator.PATH_TO_PROMPT_TITLE)
        prompt_title = prompt_title.format(format_instructions=format_instructions)
        response = self.text_generator.generate_text(prompt_title)

        response = output_parser.parse(response)

        return response["title"]

    def generate_beginning(self, title):
        response_schemas = [story_schema, choices_schema]
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        prompt_start = PromptTemplate.from_file(StoryGenerator.PATH_TO_PROMPT_START)
        prompt_start = prompt_start.format(title=title,
                                           format_instructions=format_instructions)
        response = self.text_generator.generate_text(prompt_start)

        response = output_parser.parse(response)

        return response

    def generate_continuation(self, story, choice):
        response_schemas = [story_schema, choices_schema]
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        prompt_continue = PromptTemplate.from_file(StoryGenerator.PATH_TO_PROMPT_CONTINUE)
        prompt_continue = prompt_continue.format(story=story,
                                                 choice=choice,
                                                 format_instructions=format_instructions)
        response = self.text_generator.generate_text(prompt_continue)

        response = output_parser.parse(response)

        return response

    def generate_end(self, story):
        response_schemas = [story_schema]
        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = output_parser.get_format_instructions()

        prompt_end = PromptTemplate.from_file(StoryGenerator.PATH_TO_PROMPT_END)
        prompt_end = prompt_end.format(story=story,
                                       format_instructions=format_instructions)
        response = self.text_generator.generate_text(prompt_end)

        response = output_parser.parse(response)

        return response
