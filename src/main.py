from src.parser import parser


def main():
    cv_file_path = 'examples/example1.cv'
    cv_model = parser.parse_cv(cv_file_path)

    print(cv_model.output_format.format)
    print(cv_model.contact_info.other_contacts)
    if cv_model.contact_info.other_contacts:
        for other_contact in cv_model.contact_info.other_contacts:
            print(f"{other_contact.name}: {other_contact.value}")

    # TODO: generate


if __name__ == '__main__':
    main()
