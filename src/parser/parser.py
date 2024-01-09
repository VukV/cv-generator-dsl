from textx import metamodel_from_file
import os


CV_GRAMMAR_PATH = 'src/dsl/cv.tx'


def parse_cv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The CV file {file_path} was not found.")

    cv_metamodel = metamodel_from_file(CV_GRAMMAR_PATH)
    cv_model = cv_metamodel.model_from_file(file_path)

    return cv_model
