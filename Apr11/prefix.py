def starts_with(prefix, books):
    
        bookswithPrefix =[]

        for book in books:
            if book.startswith(prefix):
                bookswithPrefix.append(book)

        return bookswithPrefix

print(starts_with("Harry Potter", ["Harry Potter 1", "Harry Potter 2", "Harry Potter 3", "Star Wars"]))