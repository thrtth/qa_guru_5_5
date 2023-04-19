import os
from selene.support.shared import browser
from selene import be, have


def test_form_complete():
    browser.config.window_width = 1800
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('Ivan@Ivanov.me')
    browser.element('[for = gender-radio-1]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('March')
    browser.element('.react-datepicker__year-select').type('1990')
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for = hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/pic.jpg')
    browser.element('#currentAddress').type('Test str, 30, 20')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    browser.all('tbody tr').should(have.exact_texts((
                             'Student Name Ivan Ivanov',
                             'Student Email Ivan@Ivanov.me',
                             'Gender Male',
                             'Mobile 1234567890',
                             'Date of Birth 19 March,1990',
                             'Subjects English',
                             'Hobbies Reading',
                             'Picture pic.jpg',
                             'Address Test str, 30, 20',
                             'State and City NCR Delhi')))


