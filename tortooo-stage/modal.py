def about():
    html = """
    <h2><center>SOBRE O JOGO</center></h2>
    <span class="text-highlight">tort.ooo</span> é inspirado no jogo
    <b>Boggle</b>, distribuído no Brasil pela Estrela com o nome
    <b>Parole</b>. Também é semelhante ao passatempo <b>Torto</b> das
    revistas de palavras cruzadas.<br><br>

    Forme palavras unindo letras adjacentes, mas lembre-se que
    não pode haver repetição de letras. Palavras maiores valem mais pontos.
    <br><br>
    <center><span class="credit">
    2022 - Feito com ❤️ em Floripa por
    <a href="https://github.com/zelacerda/zelacerda.github.io" target="_blank">zelacerda</a>
    </span></center>
    """
    return html

def stats():
    games = 13
    points_avg = 32
    counts = [123, 112, 64, 34, 12, 9]
    pct = [int(i / sum(counts) * 100) for i in counts]

    html = f"""
    <h2><center>ESTATÍSTICAS</center></h2>
    <h3>Jogos concluídos: {games}</h3>
    <h3>Média de pontos: {points_avg}</h3>
    <b>Por quantidade de letras:</b><br><br>
    3 letras: <b>{counts[0]} - {pct[0]}%</b><br>
    4 letras: <b>{counts[1]} - {pct[1]}%</b><br>
    5 letras: <b>{counts[2]} - {pct[2]}%</b><br>
    6 letras: <b>{counts[3]} - {pct[3]}%</b><br>
    7 letras: <b>{counts[4]} - {pct[4]}%</b><br>
    +7 letras: <b>{counts[5]} - {pct[5]}%</b>
    """
    return html