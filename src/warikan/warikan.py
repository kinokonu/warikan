
#支払額の詳細を書いた配列を与える 　例. {"A": 100, "B": 500, "C":600}
def warikan(detail: dict) -> str:
    #1人当たり支払額を計算
    average = sum(detail.values()) / len(detail) 

    diff = {}

    #不足・超過額の配列を作成
    for member in detail.keys():
        diff[member] = detail[member] - average 

    ans = []
    #支払いが最も少ない人の差額と名前を取得
    min_person, min_value = min(diff.items(), key=lambda x: x[1])
    