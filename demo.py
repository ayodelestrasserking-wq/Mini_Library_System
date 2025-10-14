"""
Demo Script for Mini Library Management System
Demonstrates the usage of all core functionalities.
"""

from operations import *

def demo():
    """Demonstrate the library management system functionality."""
    print("=" * 60)
    print("MINI LIBRARY MANAGEMENT SYSTEM - DEMO")
    print("=" * 60)
    
    # Clear any existing data
    global books, members
    books.clear()
    members.clear()
    
    print("\n1. ADDING BOOKS")
    print("-" * 20)
    add_book("0001", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 3)
    add_book("0002", "1984", "George Orwell", "Sci-Fi", 2)
    add_book("0003", "To Kill a Mockingbird", "Harper Lee", "Fiction", 4)
    add_book("0004", "The Catcher in the Rye", "J.D. Salinger", "Fiction", 1)
    
    print("\n2. ADDING MEMBERS")
    print("-" * 20)
    add_member("M001", "Alice Johnson", "alice.johnson@email.com")
    add_member("M002", "Bob Smith", "bob.smith@email.com")
    add_member("M003", "Carol Davis", "carol.davis@email.com")
    
    print("\n3. DISPLAYING BOOKS")
    print("-" * 20)
    display_books()
    
    print("\n4. DISPLAYING MEMBERS")
    print("-" * 20)
    display_members()
    
    print("\n5. SEARCHING BOOKS")
    print("-" * 20)
    print("Searching for books with 'Gatsby' in title:")
    results = search_books("Gatsby", "title")
    for isbn, book in results:
        print(f"  Found: {book['title']} by {book['author']} (ISBN: {isbn})")
    
    print("\nSearching for books by 'Orwell':")
    results = search_books("Orwell", "author")
    for isbn, book in results:
        print(f"  Found: {book['title']} by {book['author']} (ISBN: {isbn})")
    
    print("\n6. BORROWING BOOKS")
    print("-" * 20)
    print("Alice borrows The Great Gatsby:")
    borrow_book("M001", "0001")
    
    print("\nBob borrows 1984:")
    borrow_book("M002", "0002")
    
    print("\nAlice borrows To Kill a Mockingbird:")
    borrow_book("M001", "0003")
    
    print("\nCarol borrows The Catcher in the Rye:")
    borrow_book("M003", "0004")
    
    print("\n7. DISPLAYING CURRENT STATE")
    print("-" * 20)
    display_books()
    display_members()
    
    print("\n8. TESTING BORROW LIMITS")
    print("-" * 20)
    print("Alice tries to borrow another book (should succeed - only has 2 books):")
    add_book("0005", "Test Book 1", "Test Author 1", "Mystery", 1)
    borrow_book("M001", "0005")
    
    print("\nAlice tries to borrow one more book (should fail - already has 3 books):")
    add_book("0006", "Test Book 2", "Test Author 2", "Mystery", 1)
    borrow_book("M001", "0006")
    
    print("\n9. TESTING NO COPIES AVAILABLE")
    print("-" * 20)
    print("Bob tries to borrow The Catcher in the Rye (should fail - no copies left):")
    borrow_book("M002", "0004")
    
    print("\n10. RETURNING BOOKS")
    print("-" * 20)
    print("Alice returns The Great Gatsby:")
    return_book("M001", "0001")
    
    print("\nBob returns 1984:")
    return_book("M002", "0002")
    
    print("\n11. DISPLAYING STATE AFTER RETURNS")
    print("-" * 20)
    display_books()
    display_members()
    
    print("\n12. UPDATING BOOK AND MEMBER INFORMATION")
    print("-" * 20)
    print("Updating book information:")
    update_book("0001", title="The Great Gatsby (Updated Edition)", total_copies=5)
    
    print("\nUpdating member information:")
    update_member("M001", name="Alice Johnson-Smith", email="alice.smith@email.com")
    
    print("\n13. TESTING DELETE OPERATIONS")
    print("-" * 20)
    print("Trying to delete a book with borrowed copies (should fail):")
    delete_book("0003")
    
    print("\nTrying to delete a member with borrowed books (should fail):")
    delete_member("M001")
    
    print("\nAlice returns all her books:")
    return_book("M001", "0003")
    return_book("M001", "0005")
    
    print("\nNow trying to delete the member (should succeed):")
    delete_member("M001")
    
    print("\nTrying to delete a book with no borrowed copies (should succeed):")
    delete_book("0006")
    
    print("\n14. FINAL STATE")
    print("-" * 20)
    display_books()
    display_members()
    
    print("\n15. ERROR HANDLING DEMONSTRATIONS")
    print("-" * 20)
    print("Trying to add book with invalid genre:")
    add_book("0007", "Invalid Genre Book", "Author", "InvalidGenre", 1)
    
    print("\nTrying to add member with invalid email:")
    add_member("M004", "Invalid Email", "invalid-email")
    
    print("\nTrying to borrow non-existent book:")
    borrow_book("M002", "9999")
    
    print("\nTrying to return book that wasn't borrowed:")
    return_book("M002", "0001")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    demo()
