import pandas as pd
import matplotlib.pyplot as plt 
from PIL import Image
from colorama import Fore

Nov=pd.read_csv("C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/NOVELS.csv") 
His=pd.read_csv("C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/HISTORY.csv") 
Bio=pd.read_csv("C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/BIOGRAPHIES.csv") 
Thr=pd.read_csv("C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/THRILLERS.csv") 
Chi=pd.read_csv("C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/CHILDREN_S BOOKS.csv") 
Sales=pd.read_csv("C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/SALES.csv")

def mainmenu(): 
    category=0
    while category!=4: 
        print('')
        print(Fore.WHITE +'========================================')
        print(Fore.CYAN +' THE BOOKSTORE ') 
        print(Fore.WHITE +'========================================')
        print(Fore.YELLOW +' 1. Catalogue ') 
        print(Fore.YELLOW +' 2. Sales Statistics') 
        print(Fore.YELLOW +' 3. Reader\'s Favourites') 
        print(Fore.YELLOW +' 4. Exit')
        print(Fore.WHITE +'========================================')
        print('')
        category=int(input(Fore.WHITE +'Choose an option number from the menu :'))
        if category==1: 
            submenu1()
        elif category==2: 
            submenu2()
        elif category==3: 
            submenu3()
        else:
            print(Fore.MAGENTA +' ')
            print('| Thank you for executing our Program |') 
            print('| ~ Regards |')
            print('| The Team |')
            print(Fore.MAGENTA +'| |') 
            break
        break 
    mainmenu()
    

def submenu1():
    genre=0
    while genre!=6: 
        print('')
        print(Fore.WHITE +'========================================') 
        print(Fore.CYAN +'                CATALOGUE                ') 
        print(Fore.WHITE +'========================================')
        print(Fore.YELLOW +' 1. Novels') 
        print(Fore.YELLOW +' 2. History') 
        print(Fore.YELLOW +' 3. Biographies') 
        print(Fore.YELLOW +' 4. Thrillers') 
        print(Fore.YELLOW +' 5. Children\'s Books') 
        print(Fore.YELLOW +' 6. Go Back')
        print(Fore.WHITE +'========================================')
        print('')
        genre=int(input('Choose an option from the Catalogue :'))
        print('')
        if genre==1:
            print(Fore.CYAN +' NOVELS ') 
            print(Nov)
        elif genre==2:
            print(Fore.CYAN +' HISTORY ') 
            print(His)
        elif genre ==3:
            print(Fore.CYAN +' BIOGRAPHIES')
            print(Bio) 
        elif genre==4:
            print(Fore.CYAN +' THRILLERS ')
            print(Thr) 
        elif genre==5:
            print(Fore.CYAN +' CHILDREN\'S BOOKS ')
            print(Chi) 
        else:
            mainmenu()
            
def submenu2(): 
    types=0
    while type!=3:
        print('')
        print(Fore.WHITE +'========================================')
        print(Fore.CYAN +' SALES STATISTICS ') 
        print(Fore.WHITE +'========================================')
        print(Fore.YELLOW +' 1. Line Graph - Books sold under each') 
        print(Fore.YELLOW +' genre : Month-wise ') 
        print(Fore.YELLOW +' 2. Pie Chart - Total books sold ') 
        print(Fore.YELLOW +' : Genre-wise ') 
        print(Fore.YELLOW +' 3. Go Back ') 
        print(Fore.WHITE +'========================================')
        print('')
        types=int(input('Choose an option from Sales Statistics :')) 
        if types==1:
            linegraph()
        elif types==2: 
            piechart()
        else:
            mainmenu()
    
def submenu3(): 
    one=0
    while one!=6:
        print(Fore.WHITE +'========================================') 
        print(Fore.CYAN +' READER\'S FAVOURITES ') 
        print(Fore.WHITE +'========================================')
        print(Fore.YELLOW +' 1. Novels')
        print(Fore.YELLOW +' 2. History') 
        print(Fore.YELLOW +' 3. Biographies') 
        print(Fore.YELLOW +' 4. Thrillers')
        print(Fore.YELLOW +' 5. Children\'s Books') 
        print(Fore.YELLOW +' 6. Go Back')
        print(Fore.WHITE +'========================================')
        one=int(input(Fore.WHITE +'Choose a genre from the options:')) 
        print('')
        if one==1:
            subsubmenu1() 
        elif one==2:
            subsubmenu2()
        elif one==3:
            subsubmenu3() 
        elif one==4:
            subsubmenu4() 
        elif one==5:
            subsubmenu5() 
        else:
            mainmenu()
    
def subsubmenu1(): 
    rev1=0
    while rev1!=3: 
        print(Fore.WHITE+'============================================')
        print(Fore.CYAN +'The Reader\'s Favourites are:') 
        print(Fore.WHITE+'============================================')
        print(Fore.MAGENTA +' 1. Jane Eyre by Charlotte Bronte') 
        print(Fore.MAGENTA +' 2. To Kill a Mockingbird by Harper Lee') 
        print(Fore.MAGENTA +' 3. Go Back')
        print(Fore.WHITE+'============================================')
        rev1=int(input('Choose a book to view their reviews :')) 
        if rev1==1:
            nov1 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/Jane eyer.webp') 
            print(nov1.format)
            print(nov1.mode) 
            print(nov1.size) 
            nov1.show()
        elif rev1==2:
            nov2 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/To kill a mockingbird.jpg') 
            print(nov2.format)
            print(nov2.mode) 
            print(nov2.size) 
            nov2.show()
        else:
            submenu3()
        
def subsubmenu2(): 
    rev2=0
    while rev2!=3: 
        print(Fore.WHITE+'====================================================================')
        print(Fore.CYAN +'The Reader\'s Favourites are:') 
        print(Fore.WHITE+'====================================================================')
        print(Fore.MAGENTA +' 1. SAPIENS : A Brief History of Humankind by Yuval Noah Harari')
        print(Fore.MAGENTA +' 2. India\'s Ancient Past by Ram Sharan Sharma' )
        print(Fore.MAGENTA +' 3. Go Back') 
        print(Fore.WHITE+'====================================================================')
        rev2=int(input('Choose a book to view their reviews :')) 
        if rev2==1:
            his1 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/Sapiens.jpg') 
            print(his1.format)
            print(his1.mode) 
            print(his1.size) 
            his1.show()
        elif rev2==2:
            his2 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/India_s ancient past.png') 
            print(his2.format)
            print(his2.mode) 
            print(his2.size) 
            his2.show()
        else:
            submenu3()

def subsubmenu3(): 
    rev3=0
    while rev3!=3: 
        print(Fore.WHITE+'=================================================================')
        print(Fore.CYAN +'The Reader\'s Favourites are:') 
        print(Fore.WHITE+'=================================================================')
        print(Fore.MAGENTA +' 1. A Diary of a Young Girl by Anne Frank') 
        print(Fore.MAGENTA +' 2. The Story of my Experiments with Truth by Mahatma Gandhi' )
        print(Fore.MAGENTA +' 3. Go Back') 
        print(Fore.WHITE+'=================================================================')
        rev3=int(input('Choose a book to view it\'s reviews :')) 
        if rev3==1:
            bio1 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/The diary of a young girl.jpg') 
            print(bio1.format)
            print(bio1.mode) 
            print(bio1.size) 
            bio1.show()
        elif rev3==2:
            bio2 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/The story of my experiments with truth.jpg') 
            print(bio2.format)
            print(bio2.mode) 
            print(bio2.size) 
            bio2.show()
        else:
            submenu3()

def subsubmenu4(): 
    rev4=0
    while rev4!=3:
        print(Fore.WHITE +'=======================================')
        print(Fore.CYAN +'The Reader\'s Favourites are:') 
        print(Fore.WHITE +'=======================================')
        print(Fore.MAGENTA +' 1. Defend or Die by Tom Marcus' ) 
        print(Fore.MAGENTA +' 2. The Darkest Evening by Ann Cleeves') 
        print(Fore.MAGENTA +' 3. Go Back')
        print(Fore.WHITE +'=======================================')
        rev4=int(input('Choose a book to view their reviews :')) 
        if rev4==1:
            thr1 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/Defend or die.jpeg') 
            print(thr1.format)
            print(thr1.mode) 
            print(thr1.size) 
            thr1.show()
        elif rev4==2:
            thr2 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/The darkest evening.jpeg')
            print(thr2.format)
            print(thr2.mode) 
            print(thr2.size)
            thr2.show()
        else:
            submenu3()

def subsubmenu5(): 
    rev5=0
    while rev5!=3: 
        print(Fore.WHITE+'==========================================================')
        print(Fore.CYAN +'The Reader\'s Favourites are:') 
        print(Fore.WHITE+'==========================================================')
        print(Fore.MAGENTA +' 1. Charlie and the Chocolate Factory by Ronald Dahl')
        print(Fore.MAGENTA +' 2. The Jungle Book by Rudyard Kipling' ) 
        print(Fore.MAGENTA +' 3. Go Back')
        print(Fore.WHITE+'==========================================================')
        rev5=int(input('Choose a book to view their reviews :')) 
        if rev5==1:
            chi1 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/Charlie and the chocolate factory.jpg') 
            print(chi1.format)
            print(chi1.mode) 
            print(chi1.size) 
            chi1.show()
        elif rev5==2:
            chi2 = Image.open('C:/Users/lenovo/OneDrive/Desktop/DT-PROJECT/Images/The jungle book.jpg') 
            print(chi2.format)
            print(chi2.mode) 
            print(chi2.size) 
            chi2.show()
        else:
            submenu3()

def linegraph(): 
    x=['January','February','March','April','May','June'] 
    y1=[1254,4587,6213,11000,2154,1023] 
    y2=[4584,3254,1023,5561,7412,3689] 
    y3=[1478,5663,7012,4532,2200,3210] 
    y4=[5466,7023,8020,5046,12504,3625] 
    y5=[4587,1020,3301,6201,8520,4612]
    plt.plot(x,y1,linestyle="dashed",marker='o',markeredgecolor='c',label='No vels')
    plt.plot(x,y2,linestyle='-- ',marker='o',markeredgecolor='y',label='History')
    plt.plot(x,y3,linestyle=':',marker='o',markeredgecolor='r',label='Biograp hies')
    plt.plot(x,y4,linestyle='- ',marker='o',markeredgecolor='b',label='Thrillers')
    plt.plot(x,y5,linestyle='dashdot',marker='o',markeredgecolor='g',label='C hildren\'s books')
    plt.legend() 
    plt.title('Sales')
    
def piechart():
    Col=[24654,25524,24095,30434,28241]
    Section=['Novels','History','Biography','Thrillers','Children'] 
    col=['cyan','gold','red','blue','green'] 
    plt.pie(Col,labels=Section,colors=col)
    plt.title('Total Sales of Six Months') 
    plt.show()