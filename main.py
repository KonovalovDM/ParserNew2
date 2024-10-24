from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def print_paragraphs(paragraphs):
    for i, paragraph in enumerate(paragraphs):
        print(f"{i + 1}. {paragraph.text[:250]}...")  # вывод первых 250 символов каждого параграфа


def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    print_paragraphs(paragraphs)


def navigate_links(browser):
    links = browser.find_elements(By.XPATH, '//a[@href]')
    visible_links = [
        link for link in links
        if link.is_displayed() and link.text.strip() and not link.get_attribute('href').startswith('#')
    ]

    if not visible_links:
        print("Нет доступных ссылок для перехода.")
        return None

    for i, link in enumerate(visible_links[:15]):  # ограничиваем до первых 15 видимых ссылок
        print(f"{i + 1}. {link.text}")

    choice = int(input("Введите номер ссылки для перехода: ")) - 1
    if 0 <= choice < len(visible_links):
        try:
            link = visible_links[choice]
            link_href = link.get_attribute('href')
            return link_href
        except Exception as e:
            print(f"Не удалось получить ссылку: {e}")
            return None
    else:
        print("Некорректный выбор, попробуйте снова.")
        return None


def navigate_article_links(browser, url):
    browser.get(url)
    time.sleep(2)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Вернуться назад")

        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            list_paragraphs(browser)
        elif choice == '2':
            next_url = navigate_links(browser)
            if next_url:
                navigate_article_links(browser, next_url)
        elif choice == '3':
            return
        else:
            print("Некорректный выбор, попробуйте снова.")


def main():
    browser = webdriver.Firefox()
    browser.get("https://ru.wikipedia.org")
    assert "Википедия" in browser.title
    time.sleep(2)

    choice_article = input("Введите название статьи, которую мы ищем: ").strip()
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(choice_article)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            list_paragraphs(browser)
        elif choice == '2':
            next_url = navigate_links(browser)
            if next_url:
                navigate_article_links(browser, next_url)
        elif choice == '3':
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    main()