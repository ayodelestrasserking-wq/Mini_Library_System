"""
Unit Tests for Mini Library Management System
Tests the core functionality using assert statements.
"""

from operations import *

def test_add_book():
    """Test adding a book successfully."""
    # Clear existing books for clean test
    global books
    books.clear()
    
    # Test successful book addition
    result = add_book("978-1234567890", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 5)
    assert result == True, "Book should be added successfully"
    assert "978-1234567890" in books, "Book should be in the books dictionary"
    assert books["978-1234567890"]["title"] == "The Great Gatsby", "Book title should match"
    assert books["978-1234567890"]["available_copies"] == 5, "Available copies should equal total copies"
    
    print("✓ Test 1 passed: Add book successfully")

def test_add_duplicate_book():
    """Test adding a book with duplicate ISBN."""
    # Clear existing books for clean test
    global books
    books.clear()
    
    # Add first book
    add_book("978-1234567890", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 5)
    
    # Try to add duplicate ISBN
    result = add_book("978-1234567890", "Another Book", "Another Author", "Sci-Fi", 3)
    assert result == False, "Duplicate ISBN should not be allowed"
    assert len(books) == 1, "Only one book should exist"
    
    print("✓ Test 2 passed: Prevent duplicate ISBN")

def test_borrow_when_no_copies_left():
    """Test borrowing when no copies are available."""
    # Clear existing data for clean test
    global books, members
    books.clear()
    members.clear()
    
    # Add a book with only 1 copy
    add_book("978-1234567890", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1)
    
    # Add a member
    add_member("M001", "John Doe", "john@example.com")
    
    # Borrow the only copy
    borrow_book("M001", "978-1234567890")
    
    # Try to borrow again (should fail)
    result = borrow_book("M001", "978-1234567890")
    assert result == False, "Should not be able to borrow when no copies left"
    assert books["978-1234567890"]["available_copies"] == 0, "Available copies should be 0"
    
    print("✓ Test 3 passed: Cannot borrow when no copies left")

def test_member_borrow_limit():
    """Test that members cannot borrow more than 3 books."""
    # Clear existing data for clean test
    global books, members
    books.clear()
    members.clear()
    
    # Add 4 books
    add_book("978-1", "Book 1", "Author 1", "Fiction", 1)
    add_book("978-2", "Book 2", "Author 2", "Sci-Fi", 1)
    add_book("978-3", "Book 3", "Author 3", "Mystery", 1)
    add_book("978-4", "Book 4", "Author 4", "Romance", 1)
    
    # Add a member
    add_member("M001", "John Doe", "john@example.com")
    
    # Borrow 3 books (should succeed)
    assert borrow_book("M001", "978-1") == True, "First borrow should succeed"
    assert borrow_book("M001", "978-2") == True, "Second borrow should succeed"
    assert borrow_book("M001", "978-3") == True, "Third borrow should succeed"
    
    # Try to borrow 4th book (should fail)
    result = borrow_book("M001", "978-4")
    assert result == False, "Should not be able to borrow more than 3 books"
    
    # Check member has exactly 3 books
    member = next(m for m in members if m["member_id"] == "M001")
    assert len(member["borrowed_books"]) == 3, "Member should have exactly 3 borrowed books"
    
    print("✓ Test 4 passed: Member borrow limit enforced")

def test_delete_book_with_borrowed_copies():
    """Test that books with borrowed copies cannot be deleted."""
    # Clear existing data for clean test
    global books, members
    books.clear()
    members.clear()
    
    # Add a book and member
    add_book("978-1234567890", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 2)
    add_member("M001", "John Doe", "john@example.com")
    
    # Borrow a copy
    borrow_book("M001", "978-1234567890")
    
    # Try to delete the book (should fail)
    result = delete_book("978-1234567890")
    assert result == False, "Should not be able to delete book with borrowed copies"
    assert "978-1234567890" in books, "Book should still exist"
    
    print("✓ Test 5 passed: Cannot delete book with borrowed copies")

def test_search_books():
    """Test searching for books by title and author."""
    # Clear existing books for clean test
    global books
    books.clear()
    
    # Add test books
    add_book("978-1", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1)
    add_book("978-2", "To Kill a Mockingbird", "Harper Lee", "Fiction", 1)
    add_book("978-3", "1984", "George Orwell", "Sci-Fi", 1)
    
    # Search by title
    results = search_books("Gatsby", "title")
    assert len(results) == 1, "Should find one book with 'Gatsby' in title"
    assert results[0][0] == "978-1", "Should find the correct ISBN"
    
    # Search by author
    results = search_books("Orwell", "author")
    assert len(results) == 1, "Should find one book by Orwell"
    assert results[0][0] == "978-3", "Should find the correct ISBN"
    
    print("✓ Test 6 passed: Search books functionality")

def test_return_book():
    """Test returning a borrowed book."""
    # Clear existing data for clean test
    global books, members
    books.clear()
    members.clear()
    
    # Add book and member
    add_book("978-1234567890", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1)
    add_member("M001", "John Doe", "john@example.com")
    
    # Borrow the book
    borrow_book("M001", "978-1234567890")
    assert books["978-1234567890"]["available_copies"] == 0, "Available copies should be 0 after borrow"
    
    # Return the book
    result = return_book("M001", "978-1234567890")
    assert result == True, "Return should succeed"
    assert books["978-1234567890"]["available_copies"] == 1, "Available copies should be 1 after return"
    
    # Check member no longer has the book
    member = next(m for m in members if m["member_id"] == "M001")
    assert "978-1234567890" not in member["borrowed_books"], "Member should not have the book after return"
    
    print("✓ Test 7 passed: Return book functionality")

def run_all_tests():
    """Run all unit tests."""
    print("Running Unit Tests for Mini Library Management System")
    print("=" * 50)
    
    try:
        test_add_book()
        test_add_duplicate_book()
        test_borrow_when_no_copies_left()
        test_member_borrow_limit()
        test_delete_book_with_borrowed_copies()
        test_search_books()
        test_return_book()
        
        print("=" * 50)
        print("✓ All tests passed successfully!")
        
    except AssertionError as e:
        print(f"✗ Test failed: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    run_all_tests()
