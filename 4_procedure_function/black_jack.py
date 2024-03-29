import random
import trump

trump.trump_printer(trump.trump_card)

player_card = []
cpu_card = []

number_hierarchy = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'joker': 10,
}

def point_calc(card_list):
    a_included = 0
    sum = 0
    for card in card_list:
        if card['number'] == 'A': a_included += 1
        sum += number_hierarchy[card['number']]
    # print('a included:', a_included)
    if sum > 21 and a_included > 0:
        sum = 0
        number_pattern = []
        for card in card_list:
            if card['number'] != 'A': sum += number_hierarchy[card['number']]
        tmp_sum = sum
        for i in range(a_included+1):
            # number_pattern.append(i)
            for j in range(a_included):
                if j < i: tmp_sum += 11
                else: tmp_sum += 1
            number_pattern.append(tmp_sum)
            tmp_sum = sum
        
        # print(number_pattern)
        while True:
            if len(number_pattern): sum = number_pattern.pop()
            else: break
            if sum <= 21: break
    return sum

        
if __name__ == '__main__':
    random.shuffle(trump.trump_card)
    
    for i in range(2):
        if len(trump.trump_card) > 0:
            player_card.append(trump.trump_drow())
        else: break
    for i in range(2):
        if len(trump.trump_card) > 0:
            cpu_card.append(trump.trump_drow())
        else: break
    cpu_card[0]["is_opened"] = True
    print("all cards")
    print(player_card)
    print(cpu_card)
    print("your turn")

    '''
    player turn
    '''
    while True:
        print('現在のあなたのカード')
        trump.trump_printer(player_card)
        print('現在の合計得点:', point_calc(player_card))
        print("カードを引きますか？: (y/N)")
        text = input()
        if text == 'y':
            if len(trump.trump_card) > 0:
                player_card.append(trump.trump_drow())
        else:
            break

    '''
    dealer turn
    '''

    while True:
        print('現在のCPUのカード')
        trump.trump_printer(cpu_card)
        print('現在の合計得点:', point_calc(cpu_card))
        
        if point_calc(cpu_card) >= 17:
            break
        else:
            if len(trump.trump_card) > 0:
                cpu_card.append(trump.trump_drow())


    print("最終的なあなたの得点: ", point_calc(player_card))
    print("最終的なディーラーの得点: ", point_calc(cpu_card))

    if point_calc(player_card) > 21:
        if point_calc(cpu_card) > 21:
            print("ドローです")
        else:
            print("ディーラーの勝ちです")
    elif point_calc(cpu_card) > 21:
        print("プレイヤーの勝ちです")
    else:
        if point_calc(player_card) == point_calc(cpu_card):
            print("ドローです")
        elif point_calc(player_card) > point_calc(cpu_card):
            print("プレイヤーの勝ちです")
        else:
            print("ディーラーの勝ちです")