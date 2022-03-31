import json
from enum import Enum

#from browser import window
from browser import bind, timer, ajax

from dom import Page, Div
import modal
import storage
from utils import get_day_game, get_letters, count2sec, is_adjacent


class State(Enum):
    PLAY = 0
    MODAL = 1
    GAME_OVER = 2


class Game:
    def __init__(self):
        self.game = get_day_game()
        self.letters = get_letters(16, random_seed=self.game)
        self.act_letters = [False for _ in range(16)]
        self.state = State.PLAY
        self.played = False
        self.countdown = 3
        self.score = 0
        self.guesses = []
        self.last_pos = None
        self.page = Page()

        self.render_page()
        storage.set_value("countdown", self.countdown)


    def render_page(self):

        # Header container
        about = Div("?", id="about", Class="top-button")
        title = Div("tort.ooo", id="title")
        stats = Div("%", id="stats", Class="top-button")

        header = Div(id="header-container")
        for d in [about, title, stats]:
            header.append(d)

        # Timer and points line container
        self.score_label = Div(f"PONTOS: {self.score}", id="score")
        self.timer = Div(f"{count2sec(self.countdown)}", id="timer")

        tp_line = Div(id="timer-points-container")
        tp_line.append(self.score_label)
        tp_line.append(self.timer)

        # Grid container
        grid = Div(id="grid-container")
        self.div_letters = []
        for i, letter in enumerate(self.letters):
            div_id = "letter-" + str(i)
            d = Div(letter, id=div_id, Class="grid-item inactive")
            self.div_letters.append(d)
            grid.append(d)

        # Guess line container
        self.guess = Div(id="word")
        self.cancel = Div("✘", id="cancel")
        self.send = Div("✔", id="send")

        guess_line = Div(id="word-guess-container")
        for d in [self.guess, self.cancel, self.send]:
            guess_line.append(d)

        # Found words area
        self.area = Div(id="word-area")

        # Modal box
        self.modal = Div(id="modal", Class="hidden")
        self.modal_content = Div()
        self.modal.append(Div("X", id="modal-close"))
        self.modal.append(self.modal_content)

        # Putting all containers together and render page
        all = Div(id="all-container")
        for c in [header, tp_line, grid, guess_line, self.area, self.modal]:
            all.append(c)

        self.page.append(all)

    def click_handler(self, event):
        id = event.target.id

        if id[:6] == "letter" and self.state == State.PLAY:
            div_id = int(id[7:])
            self.check_letter(div_id)

        elif id == "cancel" and self.state == State.PLAY:
            self.clear_guess("inactive")

        elif id == "send" and self.state == State.PLAY:
            self.send_word()

        elif id == "about" and self.modal.class_name == "hidden":
            self.modal_content.innerHTML = modal.show_about()
            self.modal.class_name = "visible"
            self.state = State.MODAL

        elif id == "stats" and self.modal.class_name == "hidden":
            self.modal_content.innerHTML = modal.show_stats()
            self.modal.class_name = "visible"
            self.state = State.MODAL

        elif id == "modal-close":
            self.modal.class_name = "hidden"
            if self.played:
                self.state = State.GAME_OVER
            else:
                self.state = State.PLAY


    def send_word(self):
        word = self.guess.textContent.lower()
        if len(word) > 2 and word not in self.guesses:
            self.guesses.append(word)
            print(f"Mandando {word}")
            ajax.get(f"https://app-pkmnt5mjza-rj.a.run.app/{word}",
                     oncomplete=check)
        self.clear_guess("inactive")


    def check_letter(self, div_id):
        if not self.act_letters[div_id] and is_adjacent(self.last_pos, div_id):
            self.last_pos = div_id
            self.act_letters[div_id] = True
            self.div_letters[div_id].class_name = "grid-item active"
            self.guess.textContent += self.letters[div_id]


    def clear_guess(self, state):
        self.guess.textContent = ""
        self.last_pos = None
        for i in range(16):
            self.act_letters[i] = False
            self.div_letters[i].class_name = f"grid-item {state}"


    def update(self):
        if self.state == State.PLAY:
            self.countdown -= 1
            storage.set_value("countdown", self.countdown)
            self.timer.textContent = count2sec(self.countdown)

        if self.countdown == 0 and self.state == State.PLAY:
            self.clear_guess("game-over")
            self.modal_content.innerHTML = modal.show_game_over()
            self.modal.class_name = "visible"
            self.played = True
            self.state = State.GAME_OVER


    def check_word(self, word):
        if word:
            l = len(word)
            if l < 5:
                p = 1
            elif l == 5:
                p = 2
            elif l == 6:
                p = 3
            elif l == 7:
                p = 5
            else:
                p = 8

            self.score += p
            self.area.textContent += f"{word}-{p} "
            self.score_label.textContent = f"PONTOS: {self.score}"


@bind("body", "click")
def click(event):
    game.click_handler(event)


def check(req):
    word = json.loads(req.responseText)['result']
    game.check_word(word)


def main():
    global game
    game = Game()
    timer.set_interval(game.update, 1000)
