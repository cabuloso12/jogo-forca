import random

temas = {
    "jogos": ["minecraft", "fortnite", "tetris", "valorant", "roblox"],
    "tecnologia": ["python", "algoritmo", "internet", "computador", "software"],
    "escola": ["professor", "caderno", "biblioteca", "caneta", "recreio"],
    "filmes": ["avatar", "titanic", "shrek", "vingadores", "matrix"]
}

FORCA_ART = [
    """
       +---+

       |   |
       O   |
      /|\\  |
      / \\  |

           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |

           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |

           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
      /|   |

           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |

       |   |
           |

           |
    =========
    """,
    """
       +---+
       |   |
       O   |

           |
           |
           |
    =========
    """,
    """
       +---+

       |   |
           |

           |
           |
           |
    =========
    """
]

def escolher_palavra():
    """Permite ao usuário escolher o tema e retorna uma palavra aleatória."""
    print("Temas disponíveis:", ", ".join(temas.keys()))
    
    while True:
        tema_escolhido = input("Escolha um tema: ").lower()
        if tema_escolhido in temas:
            
            return random.choice(temas[tema_escolhido]), tema_escolhido
        print("Tema inválido. Tente novamente.")

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra com as letras já acertadas."""
    resultado = [letra if letra in letras_acertadas else "_" for letra in palavra]
    return " ".join(resultado)

def jogar():
    
    palavra_secreta, tema = escolher_palavra() 
    letras_acertadas = set()
    letras_tentadas = []
    vidas = 6
    pontos = 0

    print("=" * 40)
    print(f"        JOGO DA FORCA - TEMA: {tema.upper()}")
    print("=" * 40)
    print("Descubra a palavra secreta!")
    print()

    while vidas > 0:
        print(FORCA_ART[vidas])
        print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))
        print("Letras já tentadas:", ", ".join(letras_tentadas))
        print(f"Vidas: {vidas} | Pontos: {pontos}")
        print("-" * 40)

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida! Digite apenas UMA letra.")
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra_secreta:
            print("Boa! A letra existe na palavra.")
            letras_acertadas.add(letra)
            pontos += 10
        else:
            print("Ops! Essa letra não está na palavra.")
            vidas -= 1
            pontos = max(0, pontos - 2)

        print()

       
        if set(palavra_secreta).issubset(letras_acertadas):
            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU!")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)
            print("=" * 40)
            break

    if vidas == 0:
        print(FORCA_ART[0])
        print("=" * 40)
        print("FIM DE JOGO!")
        print("A palavra era:", palavra_secreta)
        print("Pontuação final:", pontos)
        print("=" * 40)

jogar()
