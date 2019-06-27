link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_is_presented(browser):
    browser.get(link)
    basket_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert basket_button, "There isn' basket button"
