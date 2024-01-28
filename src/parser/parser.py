import os
from .config import init_cv_metamodel


cv_metamodel = init_cv_metamodel()


def parse_cv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The CV file {file_path} was not found.")

    cv_model = cv_metamodel.model_from_file(file_path)

    return cv_model
