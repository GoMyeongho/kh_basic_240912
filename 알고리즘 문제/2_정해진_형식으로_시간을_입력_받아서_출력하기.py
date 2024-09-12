hour, min, sec = map(int,input("시간을 입력하시오(hh:mm:ss) : ").split(':'))




if hour > 12:
    hour -= 12
    if min < 10:
        if sec < 10:
            print(f"오후{hour}시0{min}분0{sec}초")
        else:
            print(f"오후{hour}시0{min}분{sec}초")
    else:
        if sec < 10:
            print(f"오후{hour}시{min}분0{sec}0초")
        else:
            print(f"오후{hour}시{min}분{sec}초")
else:
    if min < 10:
        if sec < 10:
            print(f"오전{hour}시0{min}분0{sec}초")
        else:
            print(f"오전{hour}시0{min}분{sec}초")
    else:
        if sec < 10:
            print(f"오전{hour}시{min}분0{sec}0초")
        else:
            print(f"오전{hour}시{min}분{sec}초")














