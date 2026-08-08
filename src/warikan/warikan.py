#支払額の詳細を書いた配列を与える 　例. {"A": 100, "B": 500, "C":600}
def warikan(detail: dict) -> str:
    #1人当たり支払額を計算
    average = sum(detail.values()) / len(detail) 

    #割り勘額からの乖離を格納した配列　 例. {"A": -300, "B": 100, "C":200}
    diff = {}

    #不足・超過額の配列を作成
    for member in detail.keys():
        diff[member] = detail[member] - average 

    #最終結果の配列　　例. [{"from": A, "to": B, "amount": 100}]
    ans = []

    #差額計算ループ
    while True:
        #支払いが最も少ない人の差額と名前を取得
        min_person, min_value = min(diff.items(), key=lambda x: x[1])

        #支払いが最も多い人の差額と名前を取得
        max_person, max_value = max(diff.items(), key=lambda x: x[1])

        #diffの全員の額が0になったら終了
        if min_value >= 0:
            break

        #支払額を計算
        pay_amount = min(abs(min_value), max_value)

        #ansに支払額を追加
        ans.append({"from": min_person, "to": max_person, "amount": pay_amount})

        #diffを更新
        diff[min_person] += pay_amount
        diff[max_person] -= pay_amount

    ans_text = ""
    for i in ans:
        #結果文を作成
        ans_text += f'{i["from"]}さんは{i["to"]}さんに{i["amount"]}円支払う\n' 

    return ans_text
