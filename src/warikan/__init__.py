from .warikan import warikan

def main() -> None:
    print("=== 割り勘計算ツール ===")
    data = {}
    
    while True:
        name = input("名前を入力してください (終了する場合は Enter のみ): ").strip()
        if not name:
            break
        
        try:
            amount = int(input(f"{name} さんの支払額を入力してください: "))
            data[name] = amount
        except ValueError:
            print("数字を入力してください！もう一度入力し直してください。")
            continue

    if not data:
        print("データが入力されませんでした。処理を終了します。")
        return

    result = warikan(data)

    print("\n--- 割り勘計算結果 ---")
    print(result)