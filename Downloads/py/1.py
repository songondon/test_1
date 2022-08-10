def isEven_1(value):
    return value%2==0
def isEven_2(value):
    return not( (value & 0) + 1 << 1 == ( (value - (value >> 1 << 1) + 1) // 2 * 2 ) )
# преимущества isEven_1 над isEven_2: простота, скорость, память, читаемость
# Недостатки isEven_1 над isEven_2: не показывает уровень владения операторами <<,>>,& и проч.