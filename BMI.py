def main():
    tz=float(input("please input your weight:(kg)"))
    sg=float(input("please input your height:(m)"))
    BMI=tz/(sg**2)
    if BMI<18.5:
        print("偏瘦,BMI is ",BMI)
    elif (BMI>=18.5) and (BMI<25):
        print("正常，BMI is ",BMI)
    elif (BMI>=25) and (BMI<30):
        print("偏胖，BMI is ",BMI)
    else:
        print("肥胖，BMI is ",BMI)
main()
