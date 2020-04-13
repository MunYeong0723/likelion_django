from faker import Faker

myfake = Faker()
myfake_kor = Faker('ko_KR') # 한국말로 된 가짜데이터가 생성됨.

# Faker의 메소드를 통해 어떤 종류의 가짜데이터를 뽑아낼지 결정 가능

# Seed 파일 : 코드를 실행할 때마다 같은 faker 파일을 도출해주는 파일
# seed 번호 : 각각의 가짜 데이터의 데이터 번호
Faker.seed(1)

print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.sentence())
print(myfake.random_number())

print(myfake_kor.name())
print(myfake_kor.address())
print(myfake_kor.random_number())
