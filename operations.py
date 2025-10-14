"""
Mini Library Management System
A simple library management system using Python data structures.
"""

# Data Structures
# Books: Dictionary where key is ISBN, value is book details
books = {}

# Members: List of dictionaries containing member information
members = []

# Genres: Tuple of valid genres
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance", "Biography", "History", "Science")

def add_book(isbn, title, author, genre, total_copies):
    """
    Add a book to the system.
    
    Args:
        isbn (str): Unique ISBN identifier
        title (str): Book title
        author (str): Book author
        genre (str): Book genre (must be in GENRES tuple)
        total_copies (int): Number of copies available
    
    Returns:
        bool: True if book added successfully, False otherwise
    """
    # Validate ISBN uniqueness
    if isbn in books:
        print(f"Error: Book with ISBN {isbn} already exists.")
        return False
    
    # Validate genre
    if genre not in GENRES:
        print(f"Error: Invalid genre '{genre}'. Valid genres are: {', '.join(GENRES)}")
        return False
    
    # Validate total_copies
    if total_copies <= 0:
        print("Error: Total copies must be greater than 0.")
        return False
    
    # Add book to dictionary
    books[isbn] = {
        'title': title,
        'author': author,
        'genre': genre,
        'total_copies': total_copies,
        'available_copies': total_copies
    }
    
    print(f"Book '{title}' by {author} added successfully.")
    return True

def add_member(member_id, name, email):
    """
    Add a member to the system.
    
    Args:
        member_id (str): Unique member identifier
        name (str): Member's full name
        email (str): Member's email address
    
    Returns:
        bool: True if member added successfully, False otherwise
    """
    # Validate member ID uniqueness
    for member in members:
        if member['member_id'] == member_id:
            print(f"Error: Member with ID {member_id} already exists.")
            return False
    
    # Validate email format (basic validation)
    if '@' not in email or '.' not in email.split('@')[1]:
        print("Error: Invalid email format.")
        return False
    
    # Add member to list
    new_member = {
        'member_id': member_id,
        'name': name,
        'email': email,
        'borrowed_books': []
    }
    members.append(new_member)
    
    print(f"Member '{name}' added successfully.")
    return True

def search_books(search_term, search_by="title"):
    """
    Search for books by title or author.
    
    Args:
        search_term (str): Term to search for
        search_by (str): Search criteria - "title" or "author"
    
    Returns:
        list: List of matching books
    """
    if search_by not in ["title", "author"]:
        print("Error: search_by must be 'title' or 'author'.")
        return []
    
    matching_books = []
    search_term_lower = search_term.lower()
    
    for isbn, book in books.items():
        if search_by == "title" and search_term_lower in book['title'].lower():
            matching_books.append((isbn, book))
        elif search_by == "author" and search_term_lower in book['author'].lower():
            matching_books.append((isbn, book))
    
    return matching_books

def update_book(isbn, **kwargs):
    """
    Update book details.
    
    Args:
        isbn (str): ISBN of the book to update
        **kwargs: Fields to update (title, author, genre, total_copies)
    
    Returns:
        bool: True if updated successfully, False otherwise
    """
    if isbn not in books:
        print(f"Error: Book with ISBN {isbn} not found.")
        return False
    
    # Validate genre if provided
    if 'genre' in kwargs and kwargs['genre'] not in GENRES:
        print(f"Error: Invalid genre '{kwargs['genre']}'. Valid genres are: {', '.join(GENRES)}")
        return False
    
    # Validate total_copies if provided
    if 'total_copies' in kwargs and kwargs['total_copies'] <= 0:
        print("Error: Total copies must be greater than 0.")
        return False
    
    # Update fields
    for field, value in kwargs.items():
        if field in ['title', 'author', 'genre']:
            books[isbn][field] = value
        elif field == 'total_copies':
            books[isbn]['total_copies'] = value
            # Adjust available copies if needed
            borrowed_count = books[isbn]['total_copies'] - books[isbn]['available_copies']
            books[isbn]['available_copies'] = max(0, value - borrowed_count)
    
    print(f"Book with ISBN {isbn} updated successfully.")
    return True

def update_member(member_id, **kwargs):
    """
    Update member details.
    
    Args:
        member_id (str): Member ID to update
        **kwargs: Fields to update (name, email)
    
    Returns:
        bool: True if updated successfully, False otherwise
    """
    member_found = False
    
    for member in members:
        if member['member_id'] == member_id:
            member_found = True
            
            # Validate email if provided
            if 'email' in kwargs:
                if '@' not in kwargs['email'] or '.' not in kwargs['email'].split('@')[1]:
                    print("Error: Invalid email format.")
                    return False
            
            # Update fields
            for field, value in kwargs.items():
                if field in ['name', 'email']:
                    member[field] = value
            
            print(f"Member with ID {member_id} updated successfully.")
            return True
    
    if not member_found:
        print(f"Error: Member with ID {member_id} not found.")
        return False

def delete_book(isbn):
    """
    Delete a book from the system.
    
    Args:
        isbn (str): ISBN of the book to delete
    
    Returns:
        bool: True if deleted successfully, False otherwise
    """
    if isbn not in books:
        print(f"Error: Book with ISBN {isbn} not found.")
        return False
    
    # Check if book is currently borrowed
    if books[isbn]['available_copies'] < books[isbn]['total_copies']:
        print(f"Error: Cannot delete book '{books[isbn]['title']}' - it has borrowed copies.")
        return False
    
    # Remove book
    book_title = books[isbn]['title']
    del books[isbn]
    print(f"Book '{book_title}' deleted successfully.")
    return True

def delete_member(member_id):
    """
    Delete a member from the system.
    
    Args:
        member_id (str): Member ID to delete
    
    Returns:
        bool: True if deleted successfully, False otherwise
    """
    member_found = False
    
    for i, member in enumerate(members):
        if member['member_id'] == member_id:
            member_found = True
            
            # Check if member has borrowed books
            if member['borrowed_books']:
                print(f"Error: Cannot delete member '{member['name']}' - they have borrowed books.")
                return False
            
            # Remove member
            member_name = member['name']
            del members[i]
            print(f"Member '{member_name}' deleted successfully.")
            return True
    
    if not member_found:
        print(f"Error: Member with ID {member_id} not found.")
        return False

def borrow_book(member_id, isbn):
    """
    Allow a member to borrow a book.
    
    Args:
        member_id (str): Member ID
        isbn (str): ISBN of the book to borrow
    
    Returns:
        bool: True if borrowed successfully, False otherwise
    """
    # Find member
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break
    
    if not member:
        print(f"Error: Member with ID {member_id} not found.")
        return False
    
    # Check if book exists
    if isbn not in books:
        print(f"Error: Book with ISBN {isbn} not found.")
        return False
    
    # Check if member already has 3 books borrowed
    if len(member['borrowed_books']) >= 3:
        print(f"Error: Member '{member['name']}' has already borrowed the maximum of 3 books.")
        return False
    
    # Check if book is available
    if books[isbn]['available_copies'] <= 0:
        print(f"Error: No copies of '{books[isbn]['title']}' are available.")
        return False
    
    # Check if member already borrowed this book
    if isbn in member['borrowed_books']:
        print(f"Error: Member '{member['name']}' has already borrowed '{books[isbn]['title']}'.")
        return False
    
    # Borrow the book
    member['borrowed_books'].append(isbn)
    books[isbn]['available_copies'] -= 1
    
    print(f"Member '{member['name']}' successfully borrowed '{books[isbn]['title']}'.")
    return True

def return_book(member_id, isbn):
    """
    Allow a member to return a borrowed book.
    
    Args:
        member_id (str): Member ID
        isbn (str): ISBN of the book to return
    
    Returns:
        bool: True if returned successfully, False otherwise
    """
    # Find member
    member = None
    for m in members:
        if m['member_id'] == member_id:
            member = m
            break
    
    if not member:
        print(f"Error: Member with ID {member_id} not found.")
        return False
    
    # Check if book exists
    if isbn not in books:
        print(f"Error: Book with ISBN {isbn} not found.")
        return False
    
    # Check if member has borrowed this book
    if isbn not in member['borrowed_books']:
        print(f"Error: Member '{member['name']}' has not borrowed '{books[isbn]['title']}'.")
        return False
    
    # Return the book
    member['borrowed_books'].remove(isbn)
    books[isbn]['available_copies'] += 1
    
    print(f"Member '{member['name']}' successfully returned '{books[isbn]['title']}'.")
    return True

def display_books():
    """Display all books in the system."""
    if not books:
        print("No books in the system.")
        return
    
    print("\n=== ALL BOOKS ===")
    for isbn, book in books.items():
        print(f"ISBN: {isbn}")
        print(f"  Title: {book['title']}")
        print(f"  Author: {book['author']}")
        print(f"  Genre: {book['genre']}")
        print(f"  Available: {book['available_copies']}/{book['total_copies']}")
        print()

def display_members():
    """Display all members in the system."""
    if not members:
        print("No members in the system.")
        return
    
    print("\n=== ALL MEMBERS ===")
    for member in members:
        print(f"ID: {member['member_id']}")
        print(f"  Name: {member['name']}")
        print(f"  Email: {member['email']}")
        print(f"  Borrowed Books: {len(member['borrowed_books'])}")
        if member['borrowed_books']:
            print("    Books:")
            for isbn in member['borrowed_books']:
                if isbn in books:
                    print(f"      - {books[isbn]['title']} (ISBN: {isbn})")
        print()

def get_genres():
    """Return the tuple of valid genres."""
    return GENRES
