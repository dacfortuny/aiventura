from src.story_generator import StoryGenerator
from src.utils import is_int_in_range, join_paragraphs


class Story():

    def __init__(self):
        self.story_generator = StoryGenerator()
        self.end = False

        self.set_title()
        print(f"\n{self.title.upper()}\n")

        self.initialize_story()

    def initialize_story(self):
        response = self.story_generator.generate_beginning(self.title)
        self.story_paragraphs = response["story"]
        self.full_story_text = join_paragraphs(self.story_paragraphs)
        print(f"{self.full_story_text}\n")

        self.choices = response["choices"]
        for i, choice in enumerate(self.choices, start=1):
            print(f"Choice {i}: {choice}")
        self.choose()

    def set_title(self):
        title_input = input("\nWrite a title.\n")
        if title_input.strip() != "":
            self.title = title_input
        else:
            self.title = self.story_generator.generate_title()

    def choose(self):
        choice_input = input('\nWhich is your choice?\n')
        if is_int_in_range(choice_input, len(self.choices)):
            self.choice = self.choices[int(choice_input) - 1]

        elif choice_input.lower() == "end":
            response = self.story_generator.generate_end(self.full_story_text)
            story_paragraphs = response["story"]
            story_text = join_paragraphs(story_paragraphs)
            print(f"\n{story_text}\n")
            self.full_story_text = join_paragraphs(self.story_paragraphs)
            self.end = True
            print("THE END\n")

        else:
            self.choice = choice_input

        if not self.end:
            response = self.story_generator.generate_continuation(self.full_story_text, self.choice)
            story_paragraphs = response["story"]
            story_text = join_paragraphs(story_paragraphs)
            print(f"\n{story_text}\n")
            self.full_story_text = join_paragraphs(self.story_paragraphs)
            self.choices = response["choices"]
            for i, choice in enumerate(self.choices, start=1):
                print(f"Choice {i}: {choice}")
            self.choose()
