from bs4 import BeautifulSoup

with open('pages_test/index.html', 'r', encoding='utf-8') as file_html:
    content = file_html.read()
    soup = BeautifulSoup(content, 'lxml')

    # formata o código
    #print(soup.prettify())
vacances = soup.find_all('h5')
#print(vacances)

cursos = soup.find_all('h5')
# for curso in cursos:
#     print(curso.text)

course_cards = soup.find_all('div', class_='card')

for course in course_cards:
    #print(course.h5.text)
    name = course.h5.text
    description = course.p.text
    price = course.a.text.split()[-1]
    print(f'{name} com descrição" {description} custa {price} R$')
