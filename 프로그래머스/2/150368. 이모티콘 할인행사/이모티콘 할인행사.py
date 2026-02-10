def solution(users, emoticons):
    answers = []
    
    def check(discounts):
        new_emoticons = [(e * (1 - d * 0.01), d) for e, d in zip(emoticons, discounts)] # (할인된 가격, 할인률)
        
        plus, sales = 0, 0
        for rate, price in users:
            total = 0
            for new_e, d in new_emoticons:
                if d >= rate:
                    total += new_e
            if total >= price:
                plus += 1
            else:
                sales += total
        answers.append([plus, sales])
                
    def dfs(discounts):
        if len(discounts) == len(emoticons):
            check(discounts)
            return
        
        for d in [10, 20, 30, 40]:
            discounts.append(d)
            dfs(discounts)
            discounts.pop()
    
    dfs([])
    
    answers.sort(key=lambda x:(-x[0], -x[1]))
    return answers[0]
    
    