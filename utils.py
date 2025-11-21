def encode_text(text: str) -> str:
    return text.replace("\n", "<br>") \
               .replace("\ufeff", "") \
               .replace("\u000b", "") \
               .replace("”", "\"") \
               .replace("“", "\"") \
               .encode("windows-1251")


def rgb_to_hex(r, g, b) -> str:
    if r == None: r = 0
    if g == None: g = 0
    if b == None: b = 0

    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)

    return f'#{r:02x}{g:02x}{b:02x}'
