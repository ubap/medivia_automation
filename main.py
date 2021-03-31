import random

import pyautogui


def center(located_image):
    c = pyautogui.center(located_image)
    return pyautogui.Point(c.x / 2, c.y / 2)


def find_inventory():
    inventory = None
    while not inventory:
        print('looking for inventory')
        inventory = pyautogui.locateOnScreen('inventory_image.png')
    return center(inventory)


def right_hand(inventory):
    return inventory + pyautogui.Point(180, 185)


def arrow_slot(inventory):
    return inventory + pyautogui.Point(180, 235)


def find_blank_rune():
    print('looking for blank rune')
    blank_rune = pyautogui.locateOnScreen('blank_rune.png')
    if blank_rune:
        return center(blank_rune)
    else:
        return None


def wait_for_mana():
    mana = None
    while not mana:
        print('waiting for mana')
        mana = pyautogui.locateOnScreen('mana.png')
        pyautogui.sleep(10)


def move_up_bp():
    move_up = pyautogui.locateOnScreen('move_up.png')
    pyautogui.click(center(move_up), button='left')


if __name__ == '__main__':

    while True:
        wait_for_mana()
        pyautogui.sleep(random.randint(1, 20))
        blank_rune = find_blank_rune()
        if not blank_rune:
            print('blank rune not found, moving up')
            move_up_bp()
            pyautogui.sleep(random.randint(1, 3))
            blank_rune = find_blank_rune()

        if not blank_rune:
            print('blank rune not found after moving bp up. halting')
        pyautogui.moveTo(blank_rune)

        inventory = find_inventory()
        pyautogui.dragTo(right_hand(inventory), button='left')
        pyautogui.sleep(random.randint(1, 10))
        pyautogui.press('f6')

        # eat food from arrow slot
        pyautogui.sleep(random.randint(1, 10))
        inventory = find_inventory()
        pyautogui.click(arrow_slot(inventory), button='right')

