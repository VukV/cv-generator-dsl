# DSL for generating CVs (Curriculum Vitae)
Python TextX project for Domain Specific Languages course at Faculty of Technical Sciences.

This DSL enables automatic CV generation and export as a PDF. The main purpose of this DSL is to save time by providing a way to quickly create and edit CVs, instead of manually editing files.

<br>

### Features:
* Specifying basic and contact info
  * name, surname, email, phone number
  * optional parameters such as CV picture, linkedin, etc.
* Specifying work experience
  * with company name, time period, and experience bullets to explain specified position
* Specifying education
  * with school name, title and time period
* Specifying skills, languages (optional) and interests (optional)
* Specifying output format
  * CV can be generated as PDF and HTML
* Specifying different CV styles
  * Standard, Elegant, Modern

<br>

### Instructions:
After installing the project, you can list languages and generators using TextX commands:
```
textx list-languages
textx list-generators
```
This way, you confirm that CV language and generator are registered properly. 

You can generate the CVs using the following TextX command:
```
textx generate [PATH TO .cv FILE] --target HTML/PDF
```
<br>

Alternatively, you can run `main.py`, but remember to change `cv_file_path` variable to your .cv file.

<br>

### Examples:

CV specified with DSL:
```
Basic Info:
    Name: 'John'
    Surname: 'Doe'
    Title: 'Senior Software Engineer'
    Picture: examples/images/john_doe.png

Contact Info:
    Email: john.doe@example.com
    Phone Number: +12345678901
    LinkedIn: https://www.linkedin.com/in/johndoe
    Other:
        GitHub: 'https://github.com/johndoe'

Experience:
    Title: 'Lead Developer'
    Company Name: 'Tech Innovations Inc.'
    Time Period:
        Start: Jan 2018
        End: Present
    Description:
        ExperienceBullet: 'Developed and maintained a suite of high-availability microservices.'
        ExperienceBullet: 'Led a team of 10 software engineers.'
        ExperienceBullet: 'Coordinated the successful migration of legacy systems to a modern cloud-based architecture.'

Experience:
    Title: 'Software Engineer'
    Company Name: 'DevSoft Solutions'
    Time Period:
        Start: Aug 2014
        End: Dec 2017
    Description:
        ExperienceBullet: 'Implemented new features for a range of client web applications.'
        ExperienceBullet: 'Improved system performance by optimizing existing code.'
        ExperienceBullet: 'Actively contributed to team meetings and provided valuable input during planning stages.'

//This is a comment before education
Education:
    School: 'University of Technology'
    Title: 'Bachelor of Science in Computer Science'
    Time Period:
        Start: Sep 2010
        End: Jun 2014

Skills:
    Skill: 'Python'
    //Java comment :)
    Skill: 'Java'
    Skill: 'Docker'
    Skill: 'Kubernetes'
    Skill: 'Continuous Integration/Continuous Deployment'

Languages:
    Language:
      Name: 'Italian'
      Proficiency: Native
    Language:
      Name: 'English'
      Proficiency: Professional

Interests:
    Interest: 'Open-Source Software'
    Interest: 'Travel'
    Interest: 'Photography'

Output Format: PDF

Style: Modern

```

Generated CV for given example: [cv.pdf](output/cv.pdf)
