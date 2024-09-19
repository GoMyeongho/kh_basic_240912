rod_length = int(input("지팡이의 길이(cm)를 입력하시오 :"))
rod_shadow_length = int(input("지팡이의 그림자의 길이(cm)를 입력하시오 :"))
pyramid_rod_distance = int(input("지팡이와 피라미드 사이 거리(m)를 입력하시오 :"))

pyramid_height = pyramid_rod_distance * rod_length / rod_shadow_length + rod_length/100
pyramid_height = round(pyramid_height,2)

print(f"피라미드의 높이는 {pyramid_height}m 입니다")



