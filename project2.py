
import sys


def read_file_content_to_dictionary(file_path):                   # פונקציה שמקבלת כאינפוט קובץ

    with open (file_path) as file:             #with פותח את הקובץ ומשאיר אותו פתוח לכל הזמן שבתוך הסוגריים של ה 

        d = {}                          #יוצר מילון בשביל להכניס אליו את המילים ולספור אותן
        
        for line in file:
            for word in line.split():          #מפרק את המילים שבשורה
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1

        return d

def sort_words_by_values(words_dict, n):

    sorted_dict = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse = True ))          
     #dict מחזיר רשימה ולכן נגדיר אותו בהתחלה כמילון עם המילה sorted
     #מעביר את כל הערכים של המילון אל הפונקציה הממיינת words_dict.items()
     #זה לפי איזה הגדרה ממיינים, מה עושים למילון key
     # זה פונקציה שממיינת לפי האובייקט במקום 1 שהוא מספר הפעמים שהמילה מופיעה ואובייקט מבפר 0 זה המילה lambda item: item[1]
     #הפונקציה מחזירה את המיון מקטן לגדול ולכן נכתוב לה להעביר מגדול לקטן reverse = True 

    l = list(sorted_dict)   #הופך את המילון לרשימה כי אי אפשר לחתוך מילון ורשימה כן
    l = l[:n]                   #מקומות הכי גבוהים בה n חותך את הרשימה לפי
    sorted_dict = dict(l)     #מחזיר את הרשימה ליומן
    print(sorted_dict)



if len(sys.argv) > 1:       
    n = int(sys.argv[1])

  #פונה לאוטפוט ויוצר רשימה של כל המשתנים שנתתי כאינפוט, אם נתתי משתנה אז הרשימה גדולה מאחת
  #אם הרשימה גדול מאחת לוקח את המשתנה במקום אחת ומשתמש בו להרצות הבאות שלי
  #ולא הכנסתי שום אינפוט ולכן מבקש ממני להכניס פעם ראשונה ואז קולט אותו ומריץ כל פעם איתו sys.argv אם הגודל של הרשימה הוא אחת אז יש רק

else:
    raise Exception("please enter number of words that you would like to see as sys argument ==> ")

file_path = "כאן מכניסים קובץ!!"
dictionary = read_file_content_to_dictionary(file_path)
dictionary = sort_words_by_values(dictionary, n)

for key, value in dictionary.items():                                #כותב את הערכים של המילון שהתקבלו
    print(f"the word {key} appears {list(value)} times")

