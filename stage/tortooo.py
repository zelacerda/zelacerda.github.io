from json import loads
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
        self.init_game()
        self.render_page()
        self.check_state()


    def init_game(self):
        self.game = get_day_game()
        self.letters = get_letters(8, 8, random_seed=self.game)
        self.act_letters = [False for _ in range(16)]
        self.last_pos = None
        self.played = False
        self.state = State.PLAY
        game = storage.get_value("game")
        if game == self.game: # Game in progress
            self.score = storage.get_value("score")
            self.countdown = storage.get_value("countdown")
            self.guesses = storage.get_guesses()
            self.word_counts = storage.get_word_counts()
            self.area_content = storage.get_area()
        else: # A new game
            self.score = 0
            storage.set_value("score", self.score)
            self.countdown = 180
            storage.set_value("countdown", self.countdown)
            self.guesses = []
            storage.set_guesses(self.guesses)
            self.word_counts = [0 for i in range(6)]
            storage.set_word_counts(self.word_counts)
            self.area_content = ""
            storage.set_value("area", self.area_content)


    def render_page(self):
        # Header container
        about = Div("?", id="about", Class="top-button")
        title = Div("tort.ooo", id="title")
        stats = Div("+", id="stats", Class="top-button")

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
        self.area = Div(self.area_content, id="word-area")

        # Modal box
        self.modal = Div(id="modal", Class="hidden")
        self.modal_content = Div()
        self.modal.append(Div("X", id="modal-close"))
        self.modal.append(self.modal_content)

        # Putting all containers together and render page
        all = Div(id="all-container")
        for c in [header, tp_line, grid, guess_line, self.area, self.modal]:
            all.append(c)

        self.page = Page()
        self.page.append(all)


    def check_state(self):
        game = storage.get_value("game")
        if not game: # User never played tort.ooo before
            self.about()
        elif self.countdown == 0: # User already played today
            self.state = State.GAME_OVER
            self.game_over()
        storage.set_value("game", self.game)


    def about(self):
        self.modal_content.innerHTML = modal.show_about()
        self.modal.class_name = "visible"
        self.state = State.MODAL


    def game_over(self):
        self.clear_guess("game-over")
        record = storage.get_and_update_record(self.score)
        self.modal_content.innerHTML = modal.show_game_over(self.game,
                                                            self.score,
                                                            record,
                                                            self.word_counts)
        if self.state == State.PLAY:
            storage.update_stats(self.word_counts, self.score)
        self.modal.class_name = "visible"
        self.played = True
        self.state = State.GAME_OVER


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
            self.about()

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
            storage.set_guesses(self.guesses)
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


    def check_response(self, word):
        if word:
            l = len(word)
            s = self.update_score(l)
            self.update_area(word, s)


    def update_time(self):
        if self.state == State.PLAY:
            self.countdown -= 1
            storage.set_value("countdown", self.countdown)
            self.timer.textContent = count2sec(self.countdown)

        if self.countdown == 0 and self.state == State.PLAY:
            self.game_over()


    def update_score(self, length):
        idx = min(8, length) - 3
        keys = ["w3", "w4", "w5", "w6", "w7", "w8"]
        scores = [1, 1, 2, 3, 5, 11]
        self.score += scores[idx]
        storage.set_value("score", self.score)
        self.word_counts[idx] += 1
        storage.increment_key(keys[idx])
        self.score_label.textContent = f"PONTOS: {self.score}"
        return scores[idx]


    def update_area(self, word, s):
        self.area_content += f"{word}-{s} "
        self.area.textContent = self.area_content
        storage.set_value("area", self.area_content)


@bind("body", "click")
def click(event):
    game.click_handler(event)


def check(req):
    word = loads(req.responseText)['result']
    game.check_response(word)


def main():
    global game
    game = Game()
    timer.set_interval(game.update_time, 1000)
