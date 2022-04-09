from storage import get_stats, get_value


def _plural(n):
    if n == 1:
        return "palavra"
    else:
        return "palavras"

def show_about():
    html = """
    <h2><center>SOBRE O JOGO</center></h2>
    <span class="text-highlight">tort.ooo</span> é inspirado no jogo de dados
    <i>Boggle</i>, distribuído no Brasil pela Estrela com o nome
    <i>Parole</i>. Também é semelhante ao passatempo <i>Torto</i> das
    revistas de palavras cruzadas.<br><br>

    Forme palavras unindo letras adjacentes, mas lembre-se que
    não pode haver repetição de letras. Palavras maiores valem mais pontos.
    <br><br>
    <center><span class="credit">
    De Floripa com ❤️ por
    <a href="https://github.com/zelacerda/zelacerda.github.io" target="_blank">zelacerda</a><br>
    versão 1.22.04 - Abr/2022
    </span></center>
    """
    return html

def show_stats():
    stats = get_stats()
    html = f"""
    <h2><center>ESTATÍSTICAS</center></h2>
    Recorde de pontos: <b>{stats["record"]}</b><br>
    Média de pontos por jogo: <b>{stats["mean"]}</b><br>
    Total de jogos: <b>{stats["games"]}</b><br><br>
    <b>Palavras por número de letras:</b><br><br>
    <center>
    3 letras: <b>{stats["counts"][0]} ({stats["pcts"][0]}%)</b><br>
    4 letras: <b>{stats["counts"][1]} ({stats["pcts"][1]}%)</b><br>
    5 letras: <b>{stats["counts"][2]} ({stats["pcts"][2]}%)</b><br>
    6 letras: <b>{stats["counts"][3]} ({stats["pcts"][3]}%)</b><br>
    7 letras: <b>{stats["counts"][4]} ({stats["pcts"][4]}%)</b><br>
    + letras: <b>{stats["counts"][5]} ({stats["pcts"][5]}%)</b>
    </center>
    """
    return html

def show_game_over(game, score, record, counts):
    if score > record:
        title = "NOVO RECORDE!"
    else:
        title = "FIM DO JOGO!"

    txt = f"Fiz {score} pontos e {sum(counts)} palavras "\
          + f"no tort.ooo de hoje (#{game})\\n\\n"\
          + f"3️⃣ {counts[0]} {_plural(counts[0])}\\n"\
          + f"4️⃣ {counts[1]} {_plural(counts[1])}\\n"\
          + f"5️⃣ {counts[2]} {_plural(counts[2])}\\n"\
          + f"6️⃣ {counts[3]} {_plural(counts[3])}\\n"\
          + f"7️⃣ {counts[4]} {_plural(counts[4])}\\n"\
          + f"8️⃣+ {counts[5]} {_plural(counts[5])}"

    js = f"javascript:share('{txt}')"

    html = f"""
    <h2><center>{title}</center></h2>
    Você fez <b>{score}</b> pontos e <b>{sum(counts)}</b> palavras.<br><br>
    <center>
    3 letras: <b>{counts[0]} {_plural(counts[0])}</b><br>
    4 letras: <b>{counts[1]} {_plural(counts[1])}</b><br>
    5 letras: <b>{counts[2]} {_plural(counts[2])}</b><br>
    6 letras: <b>{counts[3]} {_plural(counts[3])}</b><br>
    7 letras: <b>{counts[4]} {_plural(counts[4])}</b><br>
    + letras: <b>{counts[5]} {_plural(counts[5])}</b><br>
    </center>
    <br><center><a href="{js}">Compartilhe aqui seu resultado</a></center>
    <h3><center>E amanhã tem mais!</center></h3>
    """
    return html
