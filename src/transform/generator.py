import base64
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML, CSS
from textx import generator


def generate_cv(cv_model, output_dir='output'):
    env = Environment(
        loader=FileSystemLoader('src/transform/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    match cv_model.style.style:
        case 'Elegant':
            template = env.get_template('elegant.j2')
        case 'Modern':
            template = env.get_template('modern.j2')
        case _:
            template = env.get_template('standard.j2')

    if cv_model.basic_info.picture:
        image_path = cv_model.basic_info.picture
        cv_model.basic_info.picture = image_to_data_uri(image_path)

    if cv_model.output_format.format == 'HTML':
        return generate_html(cv_model, template, output_dir)
    elif cv_model.output_format.format == 'PDF':
        return generate_pdf(cv_model, template, output_dir)
    else:
        raise ValueError(f"Unknown format: {cv_model.output_format.format}")


def generate_html(cv_model, template, output_dir):
    html_content = template.render(model=cv_model)
    output_file = os.path.join(output_dir, 'cv.html')
    create_output_dir(output_dir)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return output_file


def generate_pdf(cv_model, template, output_dir):
    html_content = template.render(model=cv_model)
    output_file = os.path.join(output_dir, 'cv.pdf')
    create_output_dir(output_dir)

    HTML(string=html_content).write_pdf(output_file)

    return output_file


def create_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def image_to_data_uri(filepath):
    with open(filepath, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:image/png;base64,{encoded_string}"


@generator('cv', 'html/pdf')
def cv_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    if output_path:
        return generate_cv(model, output_path)
    else:
        return generate_cv(model)
