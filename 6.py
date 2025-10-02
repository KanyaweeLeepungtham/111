books = []

def add_book(books, isbn, title, author, copies):
    for book in books:
        if book['isbn'] == isbn:
            print("❌ Error: duplicate ISBN")
            return
    
    books.append({
        'isbn': isbn,
        'title': title,
        'author': author,
        'total_copies': copies
    })
def search_books(books, keyword):
    results = []
    for book in books:
        if (keyword.lower() in book['title'].lower()) or (keyword.lower() in book['author'].lower()):
            results.append(book)
    return results
books = []

# Add these 7 books
add_book(books, '001', 'Python Crash Course', 'Eric Matthes', 3)
add_book(books, '002', 'Clean Code', 'Robert Martin', 2)
add_book(books, '003', 'The Pragmatic Programmer', 'Hunt & Thomas', 2)
add_book(books, '004', 'Design Patterns', 'Gang of Four', 1)
add_book(books, '005', 'Introduction to Algorithms', 'Cormen et al.', 2)
add_book(books, '006', 'Code Complete', 'Steve McConnell', 3)
add_book(books, '007', 'Refactoring', 'Martin Fowler', 2)

found = search_books(books, "code")
for b in found:
        print(f"- Isbn:{b['isbn']}, Title: {b['title']}, Author: {b['author']}, Copies: {b['total_copies']}")
found = search_books(books, "eric")
for b in found:
    print(f"- Isbn:{b['isbn']}, Title: {b['title']}, Author: {b['author']}, Copies: {b['total_copies']}")