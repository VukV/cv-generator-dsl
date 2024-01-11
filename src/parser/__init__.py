import os
from textx import metamodel_from_file
from src.parser.model import EndDate, Date


def date_processor(date):
    return Date(month=date.month, year=date.year)


def end_date_processor(end_date):
    if end_date.month and end_date.year:
        return EndDate(month=end_date.month, year=end_date.year)
    else:
        return EndDate(present=True)


def basic_info_processor(basic_info):
    if basic_info.picture and not os.path.exists(basic_info.picture):
        raise ValueError(f"Picture file does not exist: {basic_info.picture}")


def init_cv_metamodel():
    cv_grammar_path = 'src/dsl/cv.tx'
    cv_metamodel = metamodel_from_file(cv_grammar_path)

    cv_metamodel.register_obj_processors({
        'BasicInfo': basic_info_processor,
        'Date': date_processor,
        'EndDate': end_date_processor
    })

    return cv_metamodel
