"""Шифрує видання для вчителя паролем → папка teacher/ (AES-GCM + PBKDF2).

Запуск:  TEACHER_PASSWORD='твій пароль' python3 src/protect.py
Пароль ніде не зберігається. Без нього вміст файлів у teacher/ прочитати не можна.
"""
import os, sys, json, base64, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

HERE = os.path.dirname(os.path.abspath(__file__))
pw = os.environ.get("TEACHER_PASSWORD")
if not pw:
    sys.exit("Вкажи пароль: TEACHER_PASSWORD='...' python3 src/protect.py")

ITER = 250_000
COURSES = [("course25", "Веб-майстерня · 25 уроків"), ("course38", "Веб-майстерня · 38 уроків"),
           ("sheets", "Таблиці-майстерня · Google Sheets"), ("python", "Python-майстерня · 24 уроки")]
dst = os.path.join(HERE, "..", "teacher")
os.makedirs(dst, exist_ok=True)
for key, title in COURSES:
    html = open(os.path.join(HERE, "out", f"{key}-teacher.html"), "rb").read()
    salt, iv = secrets.token_bytes(16), secrets.token_bytes(12)
    k = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(pw.encode())
    ct = AESGCM(k).encrypt(iv, html, None)
    b64 = lambda x: base64.b64encode(x).decode()
    json.dump({"title": title, "iter": ITER, "salt": b64(salt), "iv": b64(iv), "data": b64(ct)}, open(os.path.join(dst, f"{key}.json"), "w"))
    print("🔒", key, len(ct))
