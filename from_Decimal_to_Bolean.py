
def convertType(number, type):         #מחשב את המספר בצורתו הבינארית
    output = ""
    count = 0
    while number > 0:
        if number % 2 == 0:
            output += "0"
        else:
            output += "1"
    
        number //= 2
        count += 1
    while type - count > 0:
        output += "0"
        count += 1
    
    return output[::-1]


def mashlimLeShtaim(number):                     # מחשב את המספר הבינארי השלילי

    num_list = list(number)                        
#מכיוון שמחרוזות אי־אפשר לשנות ישירות, אנחנו הופכים את המחרוזת לרשימה של תווים      
#לדוגמה: "0101" יהפוך ל־["0", "1", "0", "1"]
#כך נוכל לשנות כל תו (ביט) בנפרד

    for j in range(len(num_list)):               # הופך את התווים (מ-0 ל-1 ומ-1 ל-0)
        if num_list[j] == "0":
            num_list[j] = "1"
        else:
            num_list[j] = "0"


#מוסיף בסוף 1 בבינארי
    count = 0
    for i in range(len(num_list) - 1, -1, -1):           #לולאה מיוחדת שרצה מהסוף להתחלה (מהתו הכי ימני).  
 
											
        if num_list[i] == "0":
            break

        count += 1
        num_list[i] = "0"
    
    if(int(number) > 0):
        num_list[len(num_list)-count-1] = "1"

    return "".join(num_list)
#לבסוף אנחנו מחזירים את התוצאה כרצף תווים (מחרוזת אחת)
#במקום רשימה של תווים.
#לדוגמה, ["1","1","1","1","1","0","1","1"] יחזור כ־"11111011".

