from bs4 import BeautifulSoup

# Sorgente HTML (puoi ottenere il tuo sorgente HTML da un file o da una richiesta HTTP)
html_source = """
<!DOCTYPE html>
<html>
<head>
    <title>Pagina di Esempio</title>
</head>
<body>
    <a href="https://www.link1.com">Link 1</a>
    <a href="https://www.link2.com">Link 2</a>
    <a href="https://www.link3.com">Link 3</a>
    <!-- Altri elementi HTML qui -->
</body>
</html>
"""

# Parsing del sorgente HTML con BeautifulSoup
soup = BeautifulSoup(html_source, 'html.parser')

# Trova tutti i tag 'a' (i link) nella pagina
links = soup.find_all('a')

# Nome del file di testo in cui verranno salvati i link
file_name = "links.txt"

# Apri il file in modalità scrittura
with open(file_name, 'w', encoding='utf-8') as file:
    # Itera sui link e scrivi ciascun link nel file di testo
    for link in links:
        href = link.get('href')
        if href:
            file.write(href + "\n")

print(f"I link sono stati salvati in {file_name}")
