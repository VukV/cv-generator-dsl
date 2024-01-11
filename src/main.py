from src.parser import parser
import logging


def main():
    cv_file_path = 'examples/example1.cv'

    try:
        cv_model = parser.parse_cv(cv_file_path)
        # TODO: generate
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()
