from bs4 import BeautifulSoup
from testT import g

g = """
<button disabled="" aria-label="Next" id="ember5964" class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary artdeco-button--disabled ember-view">  <li-icon aria-hidden="true" type="chevron-right-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" width="16" height="16" focusable="false">
  <path d="M9 8L5 2.07 6.54 1l4.2 6.15a1.5 1.5 0 010 1.69L6.54 15 5 13.93z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Next
</span></button>
"""
soup = BeautifulSoup(g,"lxml")

button = soup.find("button", {"class": "artdeco-pagination__button--next" })
print(button.get("disabled"))

