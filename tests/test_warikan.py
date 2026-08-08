from warikan import warikan

#一般的な場合
def test_three():
    result = warikan({"A": 100, "B": 500, "C": 600})
    assert "AさんはCさんに200円支払う" in result
    assert "AさんはBさんに100円支払う" in result

#１人が全員分建て替えた場合
def test_tatekae():
    result = warikan({"A": 0, "B": 0, "C": 3000})
    assert "AさんはCさんに1000円支払う" in result
    assert "BさんはCさんに1000円支払う" in result

#全員が同額を支払っている場合
def test_dougaku():
    assert warikan({"A": 1000, "B": 1000, "C": 1000}) == ""

#参加者が１人だけ
def test_one():
    assert warikan({"A": 1000}) == ""




