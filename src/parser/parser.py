from textx import metamodel_from_file
import os


def basic_info_processor(basic_info):
    if basic_info.picture and not os.path.exists(basic_info.picture):
        raise ValueError(f"Picture file does not exist: {basic_info.picture}")


cv_grammar_path = 'src/dsl/cv.tx'
cv_metamodel = metamodel_from_file(cv_grammar_path)

cv_metamodel.register_obj_processors({
    'BasicInfo': basic_info_processor
})


def parse_cv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The CV file {file_path} was not found.")

    cv_model = cv_metamodel.model_from_file(file_path)

    return cv_model
