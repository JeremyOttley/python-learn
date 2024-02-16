## TODO oaisbn python -> streamlit
import re
import pyperclip


# Function to convert ISBN to the desired format
def convertISBN(isbn):

	# Remove non-numeric characters from ISBN
	isbnNumbers = re.sub("[^0-9]", "", isbn, count=0, flags=0)

	# Take the last 4 digits
	# Convert to uppercase and prepend 'A'
	return 'A' + isbnNumbers[8:12] + 'E'


def main():

    # Prompt the user for input
    isbn = input("Enter ISBN: ")

    # Call the function to convert ISBN to the desired format
    result = convertISBN(isbn)

    # Output the result to the console
    print(result)
    
    # Copy the result to the clipboard
    pyperclip.copy(result)


if __name__ == "__main__":

    main()

