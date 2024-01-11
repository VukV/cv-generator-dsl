from src.parser import parser
from src.transform import generator
import logging


def main():
    cv_file_path = 'examples/example1.cv'

    try:
        cv_model = parser.parse_cv(cv_file_path)
        cv = generator.generate_cv(cv_model)
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()
