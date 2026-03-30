#4_operators.py
a= 132
b= 45

fmt0='{:<10}' #변수 + 공백 10개까지
fmt1='0b{:08b} 0x{:02x}{:3}' #0b________8개 2진법.0x__16진법 2개. 3개의 10진법

print(fmt0.format('a'),fmt1.format(a,a,a,))
print(fmt0.format('b'),fmt1.format(b,b,b,))

n=30
print('-'*n)

print(fmt0.format('a&b'), fmt1.format(a&b,a&b,a&b))

#bit or
print()
print(fmt0.format('a'),fmt1.format(a,a,a,))
print(fmt0.format('b'),fmt1.format(b,b,b,))
print('-'*n)
print(fmt0.format('a|b'), fmt1.format(a|b,a|b,a|b))

#bitXor^]or
print("\nbit XOR^")
print(fmt0.format('a'),fmt1.format(a,a,a,))
print(fmt0.format('b'),fmt1.format(b,b,b,))
print('-'*n)
print(fmt0.format('a^b'), fmt1.format(a^b,a^b,a^b))


#bit NOT~
print("\nbit NOT ~")
print(fmt0.format('a'),fmt1.format(a,a,a,))
print('-'*n)
print(fmt0.format('~a'), fmt1.format(~a&0XFF,~a&0XFF,~a&0XFF))

#bit 왼쪽 쉬프트
print("\nbit 왼쪽쉬프트 <<")
print(fmt0.format('a'),fmt1.format(a,a,a,))
print('-'*n)
print(fmt0.format('a<<2'), fmt1.format(a<<2&0XFF,a<<2&0XFF,a<<2&0XFF))

#bit 오른쪽  쉬프트
print("\nbit 오른쪽 쉬프트 >>")
print(fmt0.format('a'),fmt1.format(a,a,a,))
print('-'*n)
print(fmt0.format('a>>2'), fmt1.format(a>>2&0XFF,a>>2&0XFF,a>>2&0XFF))
