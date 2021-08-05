def Task(m):
   if m == 7:
      return("It's time to wake up")
      
   elif m==8:
      return('Meditate')

   elif m==9:
      return("Breakfast Time")
   
   elif m==10:
      return('Have medicine Acetaminophen & check your temperature')
   
   elif m==11:

      return('Study or Work from home')
   elif m==12:

      return('Use your Nebuliser')
   elif m==13:

      return('FaceTime a family member or a friend')
   elif m==14:

      return('Have lunch')
   elif m==15:

      return('Take a nap')
   elif m==16:

       return("Please walk for atleast 60 minutes")
   elif m==18:

      return('Have medicine Remdesivir & check your temperature')
   elif m==19:

       return('Dinner time')
   elif m==20:

       return("Do the dishes please")
   elif m==21:

       return("Watch a movie/show")
   elif m==22:

       return("Check your blood oxygen levels using your oximeter")
   elif m==23:

       return("Time to go to bed. Good Night, sweet dreams!")


   else:

      return("It's Time to sleep")

def addNodes(G, nodes):
        for i in range(len(nodes)):
            if nodes[i] not in G:
                G[nodes[i]]=[]
        return G

def addEdges(G, edges, directed = False):
    for edge in edges:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])


def dijkstra(initial,final):
    graph= {'DHA':{'Ziauddin': 6, 'Expo': 6, 'JPMC': 3},
            'Clifton': {'JPMC': 5, 'Khaliqdina': 6},
            'Saddar': {'Expo': 6, 'JPMC': 10, 'Ziauddin': 2},
            'JPMC': {'DHA': 2, 'Saddar': 10, 'Nazimabad': 8},
            "Expo": {'DHA': 6, 'Nazimabad': 9},
            'Nazimabad': {'JPMC': 8, 'Expo': 9, 'Ziauddin': 10},
            'Ziauddin': {'Saddar': 2, 'Nazimabad': 10},
            'Gulshan': {'Expo':3, 'Ziauddin':6, 'JPMC':4},
            'Khaliqdina':{'Clifton':6,'Saddar':2}}
    infinity = 9999
    temp = {}
    Nodes = graph
  
    minimum_distance = {}
    path = []

    for node in Nodes:
        minimum_distance[node] = infinity
    minimum_distance[initial] = 0
 
    while Nodes:
        minNode = None
        for node in Nodes:
            if minNode is None:
                     minNode = node
            elif minimum_distance[node] < minimum_distance[minNode]:
                     minNode = node
        paths = graph[minNode].items()
        for childNode, weight in paths:
            if weight + minimum_distance[minNode] < minimum_distance[childNode]:
                  minimum_distance[childNode] = weight + minimum_distance[minNode]
                  temp[childNode] = minNode

        Nodes.pop(minNode)
 
    currentNode = final
    while currentNode != initial:
        try:
            path.insert(0,currentNode)
            currentNode = temp[currentNode]

        except KeyError:
            return('Path not reachable, try another location.')
            break

    path.insert(0,initial)


    if minimum_distance[final] != infinity:
        ans = minimum_distance[final]
        clock = ans*3
        f =  'Shortest distance is '+ str(minimum_distance[final]) + ' km. '
        j = " Enter these locations in google maps to reach your destination in about " + str(clock) + 'minutes'
        for i in range(len(path)):
            j += path[i]
            j += " ==> "
        j = j[0:(len(j)-1)]
        klex = f + j
        return klex
      
def delivery_sort(anon):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(anon) - 1):
            if anon[i] > anon[i + 1]:
                anon[i], anon[i + 1] = anon[i + 1], anon[i]
                swapped = True
    return anon

def push(lst, item):
  x = lst.append(item)
  return x

def pop(lst, item):
  y = lst.pop()
  return y
def Delivery(day):
  if day == "Tuesday":
       All_med = ["COVID testing kits", "Face masks" , "Acetaminophen", "Remedesmir", "Sanitizer" ,'Oxygen Tank']

       sortedmed = delivery_sort(All_med)
       supplies = []
       supplies.append(sortedmed[0])
       supplies.append(sortedmed[1])
       supplies.append(sortedmed[2])
       supplies.append(sortedmed[4])
       supplies.append(sortedmed[5])
       night_med = []
       night_med.append(sortedmed[2])
       night_med.append(sortedmed[3])

       f = str('Keep the Quarantine Supplies ' + str(supplies)+' on the kitchen table and keep the medicines ' + str(night_med)+ 'on bedside')
       return f
  elif day == 'Friday':
     return 'COVID-19 testing day, Please do an anterior nasal swab and send it to the testing lab'
   
  elif day == 'Sunday':
    groceries = ["Cream-bread", "Roasted-Almonds" , "Caremel", "Raw-vegetables", "Canned-mushrooms"]
    sortedg = delivery_sort(groceries)
    refrigerator = []
    cupboard = []
    push(refrigerator, sortedg[0])
    push(refrigerator, sortedg[1])
    push(refrigerator, sortedg[2])
    push(cupboard, sortedg[3])
    push(cupboard, sortedg[4])
    cupboard = str(cupboard)
    refrigerator = str(refrigerator)
    return('Put groceries ' + (cupboard) +  ' in cabinet and '+ (refrigerator)+ ' in fridge')

from tkinter import *
import tkinter.messagebox
import sys

root = Tk()

root.title("COVID 19 (Health App)")


root.geometry("1000x500") 
root.configure(bg= '#E9967A')
            
label_name = Label(text = 'Enter Your Name Below' ,bg= '#E9967A',fg = "black", font= 10)
label_name.pack()

e = Entry(root, width=50,bg = "#E9967A" , fg = "white" )
e.pack()


label_Time = Label(text = 'Enter Current Time In Hours (Quarantine Mode)',bg= '#E9967A',fg = "black", font =10)
label_Time.pack()

c = Entry(root, width=50,bg = "#E9967A" , fg = "white")
c.pack()

label_day = Label(text = 'Enter Day Below (Quarantine Mode)',bg= '#E9967A',fg = "black", font = 10)
label_day.pack()

s = Entry(root, width=50,bg = "#E9967A" , fg = "white")
s.pack()

label_location = Label(text = 'Enter Initial And Final Locations Below ',bg= '#E9967A',fg = "black", font = 10)
label_location.pack()

p = Entry(root, width=50,bg = "#E9967A" , fg = "white")
p.pack()


def Myclick_():
   hello = "Hello " + e.get()
   my_label = Label(root, text=hello, borderwidth=2, relief="groove", bg = "peach puff", fg = "blue",font = 50)
   my_label.pack()

   Time = int(c.get())
   F = Task(Time)
   my_2nd_label = Label(root, text=F,borderwidth=2, relief="groove", bg = "peach puff", fg = "black",font = 50)
   my_2nd_label.pack()


   w = s.get()
   zx = Delivery(w)

   my_label_3 = Label(root, text=zx,borderwidth=2, relief="groove", bg = "peach puff", fg = "black",font = 50)
   my_label_3.pack()

   baba = p.get()
   R = baba.split(" ")
   firstR = R[0]
   secondR = R[1] 
   taher = dijkstra(firstR,secondR)

   my_label_4 = Label(root, text = taher, borderwidth=2, relief="groove", bg = "peach puff", fg = "black",font = 50)
   my_label_4.pack()
      
myButton = Button(root, text="CLICK HERE TO CONTINUE",bg = "#E9967A", fg = "white",command = Myclick_)
myButton.pack()

def resetAll():
    root.destroy()
clearall = Button(root, text= 'CLICK HERE TO QUIT/RESTART', fg = "white" , bg = "#E9967A", command=resetAll).pack(pady=10)
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

root.mainloop()
