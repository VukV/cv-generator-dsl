from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML


def generate_cv(cv_model):
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    match cv_model.style:
        case 'Elegant':
            template = env.get_template('elegant.html')
        case 'Modern':
            template = env.get_template('modern.html')
        case _:
            template = env.get_template('standard.html')

    if cv_model.output_format.format == 'HTML':
        return generate_html(cv_model, template)
    elif cv_model.output_format.format == 'PDF':
        return generate_pdf(cv_model, template)
    else:
        raise ValueError(f"Unknown format: {cv_model.output_format.format}")


def generate_html(cv_model, template):
    html_content = template.render(model=cv_model)
    output_file = 'output/cv.html'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return output_file


def generate_pdf(cv_model, template):
    html_content = template.render(model=cv_model)
    output_file = 'output/cv.pdf'
    HTML(string=html_content).write_pdf(output_file)

    return output_file
