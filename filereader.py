# pip install pandas
import pandas, os, time

# import sys
# print(sys.builtin_module_names)

fruits = ["pear","apple","watermelon","banana","blueberries","cranberries","cherries","elderberries","lemon","orange","grape","pineapple","sugar-apple"]
# fruits = open("fruits.txt")
# print(fruits.read())
# fruits.close() #you can not interact with this file until open it again

#open("file.txt", "w") -- create a file or overwrite an existent
#args -- 
# "r" (default - read the file)
# "w" (overwrite file or create one)
# "x" (create file and open for edit // does not overwrite if already exists)
# "a" (open for writing - append text to file)
# "char+" (you can read and edit) -- example line 35


with open("fruits.txt", "w") as fruits_file:
     fruits_file.write("\n".join(fruits))
# with open("bear.txt", "w") as bear:
#      bear.write("Lorem ipsum dolor sit amet consectetur, adipisicing elit. Alias, rerum. Doloremque provident itaque corporis quae exercitationem nesciunt voluptatem laboriosam possimus sed hic. Earum ipsum odio laborum molestiae, iste facere vitae.")
# with open("bear.txt") as bear:
#      print(bear.read()[:90])


#to print many times
# fruits_content = fruits.read()
# print(content) 
# print(content)

def char_occurences(char, file_path):
     with open(file_path) as file:
          return file.read().count(char)
     
# print(char_occurences("a", "fruits.txt"))
     
with open("fruits.txt", "a+") as fruits_file:
     fruits_file.write("\ngreen-apple") # after the write, the cursor goes to the end of file, if you print, it wont return nothing
     fruits_file.seek(0) # cursor will go to the beginning of file, so you can read it entirely
     # print(fruits_file.read())

# with open("data.txt", "a+") as datatxt:
#      content_to_append = ""
#      for i in range(2):
#           datatxt.seek(0)
#           content_to_append += "\n" + datatxt.read()
#      datatxt.write(content_to_append)
        
# if not os.path.exists("data.txt"): open("data.txt", "w").write("0.2,1.4\n0.3,1\n0.9,2.6")

while True:
     if os.path.exists("stars.csv"):
          stars = pandas.read_csv("stars.csv")
          # print(stars.mean()) # all colunms
          print(stars.mean()["Burger King"])
     else:
          open("stars.csv", "w").write("McDonald's,Burger King,Bob's\n4,5,3\n5,4.5,3.5\n5,5,3\n3.5,5,4\n4,4,4")
     time.sleep(10)
          