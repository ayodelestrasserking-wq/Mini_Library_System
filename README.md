# Mini_library
A simple library management system built in Python using lists, dictionaries, and tuples. This system supports adding, searching, updating, deleting, borrowing, and returning books, as well as managing library members.

## Features

- *Book Management*: Add, search, update, and delete books
- *Member Management*: Add, update, and delete library members
- *Borrowing System*: Members can borrow up to 3 books at a time
- *Return System*: Members can return borrowed books
- *Data Validation*: Ensures data integrity with proper validation
- *Search Functionality*: Search books by title or author

## Data Structures Used

- *Books*: Stored in a dictionary where ISBN is the key and book details are the value
- *Members*: Stored as a list of dictionaries containing member information
- *Genres*: Defined as a tuple of valid genres (Fiction, Non-Fiction, Sci-Fi, Mystery, Romance, Biography, History, Science)

## Files

- operations.py - Contains all the core functions and data structures
- demo.py - Demonstration script showing system usage
- tests.py - Unit tests using assert statements
- README.md - This file with instructions## How to Run

### Prerequisites
- Python 3.6 or higher

### Running the Demo
To see the system in action, run the demo script:

bash
python demo.py


This will demonstrate all the features including:
- Adding books and members
- Borrowing and returning books
- Searching functionality
- Update and delete operations
- Error handling

### Running the Tests
To run the unit tests:

bash
python tests.py


This will run 7 comprehensive tests covering:
- Adding books successfully
- Preventing duplicate ISBNs
- Borrowing when no copies are available
- Member borrow limits (max 3 books)
- Deleting books with borrowed copies
- Search functionality
- Return book functionality

### Using the System Programmatically
You can import and use the functions in your own code:

python
from operations import *

# Add a book
add_book("978-1234567890", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 5)

# Add a member
add_member("M001", "John Doe", "john@example.com")
## Available Functions

### Book Operations
- add_book(isbn, title, author, genre, total_copies) - Add a new book
- search_books(search_term, search_by) - Search books by title or author
- update_book(isbn, **kwargs) - Update book details
- delete_book(isbn) - Delete a book (only if no copies are borrowed)

### Member Operations
- add_member(member_id, name, email) - Add a new member
- update_member(member_id, **kwargs) - Update member details
- delete_member(member_id) - Delete a member (only if no books are borrowed)

### Borrowing Operations
- borrow_book(member_id, isbn) - Borrow a book
- return_book(member_id, isbn) - Return a borrowed book

### Display Functions
- display_books() - Show all books in the system
- display_members() - Show all members in the system

## Validation Rules

- *ISBNs must be unique* - Cannot add duplicate ISBNs
- *Member IDs must be unique* - Cannot add duplicate member IDs
- *Genres must be valid* - Must be one of the predefined genres
- *Email validation* - Basic email format validation
- *Borrow limits* - Members can borrow maximum 3 books
- *Availability check* - Cannot borrow books with no available copies
- *Delete restrictions* - Cannot delete books with borrowed copies or members with borrowed books

## Error Handling
he system includes comprehensive error handling for:
- Duplicate ISBNs and member IDs
- Invalid genres and email formats
- Borrowing limits and availability
- Delete restrictions
- Non-existent books and members

All functions return True on success and False on failure, with descriptive error messages printed to the console.

## Testing

The system includes 7 comprehensive unit tests that verify:
1. Successful book addition
2. Prevention of duplicate ISBNs
3. Borrowing restrictions when no copies available
4. Member borrow limits (max 3 books)
5. Delete restrictions for books with borrowed copies
6. Search functionality for books
7. Return book functionality

Run python tests.py to execute all tests and verify the system works correctly.


