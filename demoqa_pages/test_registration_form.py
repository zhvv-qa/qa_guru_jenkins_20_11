import os

import allure
from allure_commons.types import Severity
from selene import have, by


@allure.title("Successful fill form")
def setup_browser(request):
    browser = browser_settings
    my_picture = 'testpion.jpeg'

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element('#firstName').type('Vika')
        browser.element('#lastName').type('Zhuchkova')
        browser.element('#userEmail').type('vika.zh@gmail.com')
        browser.element('[for="gender-radio-2"]').click()
        browser.element('#userNumber').type('9881112345')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('[value="9"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('[value="1994"]').click()
        browser.element('[aria-label="Choose Saturday, October 1st, 1994"]').click()
        browser.element('#subjectsInput').type('English').press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(my_picture))
        browser.element('#currentAddress').type('Test address 789')
        browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
        browser.element('#react-select-4-input').type('Agra').press_enter()
        browser.element('#submit').click()

    with allure.step("Check form results"):
        browser.all('td').should(have.exact_texts(
            'Student Name', 'Vika Zhuchkova', 'Student Email',
            'vika.zh@gmail.com', 'Gender', 'Female', 'Mobile', '9881112345',
            'Date of Birth', '01 October,1994', 'Subjects', 'English',
            'Hobbies', 'Sports', 'Picture', 'testpion.jpeg', 'Address',
            'Test address 789', 'State and City', 'Uttar Pradesh Agra',
        )
        )

@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'zhsv')
@allure.feature('Issues_name')
@allure.story('Проверка названия Issue')
@allure.link('https://github.com', name='Testing')
def test_allure_labels():
    pass
