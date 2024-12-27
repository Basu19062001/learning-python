class Library:

  __noOfBooks = 0
  __listOfBook = []
  
  def __init__(self, bookName):
    self.__bookName = bookName
    self.updateListOfBook(bookName)
  
  
  @property
  def bookName(self):
    return self.__bookName
  @bookName.setter
  def bookName(self, bookName):
    self.__bookName = bookName
    self.updateListOfBook(bookName)
    
    
  def updateListOfBook(self, bookName):
    self.__listOfBook.append(bookName)
    self.__noOfBooks += 1
  
  def getNoOfBooks(self):
    return self.__noOfBooks

  def isBookAvailable(self, bookName):
    if bookName in self.__listOfBook:
      print("Book is available")
    else:
      print("Book is not available")
  
  def returnBook(self, bookName):
    if bookName in self.__listOfBook:
      return self.__listOfBook.remove(bookName)
    else:
      print("Book is not available")
      
  
  def displayListOfBook(self):
    for book in self.__listOfBook:
      print(book)
      
      
library = Library("Python")
library.bookName = "Java"
library.bookName = "C++"
library.bookName = "C"
library.bookName = "Datastructures"
library.bookName = "Algorithm"
library.bookName = "DataStructures & Algorithms"
library.bookName = "Database"
library.bookName = "SQL"
library.bookName = "MySQL"
library.bookName = "MongoDB"

library.displayListOfBook()
print(library.getNoOfBooks())
print(library.bookName)
library.isBookAvailable("Java")
library.isBookAvailable("Python")
library.isBookAvailable("Math")
print(library.returnBook("Python"))
library.displayListOfBook()
library.returnBook("Java")
library.displayListOfBook()
library.returnBook("Java")