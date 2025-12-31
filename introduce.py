"""
이름, 나이, 전공, MBTI, 취미, 특기, 지원목적, 지역, 좋아하는 음식, 싫어하는음식, 좋아하는 색상, 좋아하는 영화배우, 
키, 좋아하는 운동, 좋아하는 영화, 생일, 노트북 종류, 핸드폰 기종, 부먹/찍먹, 퍼스털 컬러
"""
[Name, age, major, MBTI, 
 hobbies, special_skills, 
purpose_of_application,
region, favorite_food, 
disliked_food, favorite_color, 
favorite_actor,
Height, favorite_sport, 
favorite_movie, birthday, 
laptop_type, phone_model, 
side_dish_dipping, personal_color]=["김우진", 26, "메카트로닉스", "ISTP", "헬스", "도전적이고 열정적인 모습", 
                                    "스마트 팩토리 기술력 증진을 위해", "경기도 고양시", "치킨", "가지볶음"
                                    , "검은색", "황정민", 178, "축구", "서울의 봄", "2000년 3월 1일", 
                                    "Asus zenbook", "아이폰 16e", "찍먹", "쿨톤"]
print(f"""안녕하세요 제 이름은 {Name}이고 저는 {birthday}생이어서  올해 {age}살이고 키는 {Height}입니다. 제 전공은
{major}이고 저의 MBTI는 {MBTI}입니다.저의 취미와 특기는 {hobbies}와 {special_skills}이고 제가 이번 스마트 팩토리 
고급과정에 지원한 이유는{region}입니다. 저는 {region}에서 왔고 이번 기회에 저의 역량을 더 발전시켜 좋은 성과를 거두고 싶습니다. 
제가 좋아하는 음식은{favorite_food}이고 제가 싫어하는 음식은 {disliked_food}입니다. 저의 퍼스털 컬러는 {personal_color}이어서
제가 제일 좋아하는 색은 {favorite_color}입니다. 저는 {favorite_actor}배우를 좋아하며 가장 인상깊게 본 영화는 {favorite_movie}입니다. 
가장 좋아하는 운동은 {favorite_sport}입니다. 저는 부먹보단 {side_dish_dipping}을 더 좋아합니다. 제 노트북 사양은{laptop_type}이고 
핸드폰 기종은 {phone_model}입니다. 짧지만 제 자소서를 읽어주셔서 감사합니다.""")
