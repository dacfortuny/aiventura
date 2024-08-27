from omegaconf import OmegaConf

PATH_TO_API_KEY = "api_key.yaml"


def get_api_key(path_to_api_key=PATH_TO_API_KEY):
    return OmegaConf.load(path_to_api_key)["API_KEY"]


def is_int_in_range(s, N):
    if s.isdigit():
        num = int(s)
        if 1 <= num <= N:
            return True
    return False


def join_paragraphs(paragraphs):
    return "\n\n".join(paragraphs)
