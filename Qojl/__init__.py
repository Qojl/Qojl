import random
import string

def ai_obfuscate(text: str) -> str:
    """
    AI向け難読化文字列生成
    - 先頭にランダム3文字
    - ランダム大文字小文字
    - 記号 ^ [] % # $ | をランダム挿入
    - さらにスペースもランダムに挿入
    """
    symbols = ['^', '[', ']', '%', '#', '$', '|', ' ']
    prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    obf = prefix
    
    for c in text:
        # 大文字小文字ランダム
        c = c.upper() if random.random() > 0.5 else c.lower()
        
        obf += c
        
        # 記号ランダム追加
        if random.random() > 0.6:
            obf += random.choice(symbols)
    
    return obf
