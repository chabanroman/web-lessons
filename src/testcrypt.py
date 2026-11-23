"""Шифрування контрольних в учнівських виданнях.

Кожна контрольна шифрується своїм ключем (AES-256-GCM). Ключ виводиться з пароля вчителя,
тож без пароля його не відновити. Учнівська сторінка розшифровує контрольну лише тоді,
коли ключ є у файлі config/tests.json — його туди записує вчитель перемикачем
«Показати дітям» у виданні для вчителя.
"""
import os, sys, json, base64, secrets, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def _password():
    pw = os.environ.get("TEACHER_PASSWORD")
    if not pw:
        sys.exit("Вкажи пароль вчителя: TEACHER_PASSWORD='...' python3 src/<скрипт>.py")
    return pw

def test_key(course, n):
    return hashlib.pbkdf2_hmac("sha256", _password().encode(), f"web-lessons-test:{course}:{n}".encode(), 200_000, 32)

def secure(data, edition, course):
    b64 = lambda x: base64.b64encode(x).decode()
    data["courseKey"] = course
    keys = {}
    for t in data["tests"]:
        k = test_key(course, t["n"]); keys[str(t["n"])] = b64(k)
        if edition == "student":
            iv = secrets.token_bytes(12)
            ct = AESGCM(k).encrypt(iv, json.dumps(t["q"], ensure_ascii=False).encode(), None)
            t["enc"] = {"iv": b64(iv), "data": b64(ct)}
            del t["q"]
    if edition == "teacher":
        data["testKeys"] = keys
    return data
