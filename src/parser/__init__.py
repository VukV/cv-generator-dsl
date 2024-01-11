import os
from textx import metamodel_from_file


def basic_info_processor(basic_info):
    if basic_info.picture and not os.path.exists(basic_info.picture):
        raise ValueError(f"Picture file does not exist: {basic_info.picture}")


def init_cv_metamodel():
    cv_grammar_path = 'src/dsl/cv.tx'
    cv_metamodel = metamodel_from_file(cv_grammar_path)

    cv_metamodel.register_obj_processors({
        'BasicInfo': basic_info_processor
    })

    return cv_metamodel
