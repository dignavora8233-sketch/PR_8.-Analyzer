import numpy as np

class DataAnalytics:

    def __init__(self):
        self.array = None

    # Private Method
    def __check_array(self):
        if self.array is None:
            print("First create an array.")
            return False
        return True

    # Class Method
    @classmethod
    def default_array(cls):
        obj = cls()
        obj.array = np.array([10, 20, 30, 40, 50])
        return obj

    # Static Method
    @staticmethod
    def show_title(title):
        print("\n" + "=" * 40)
        print(title)
        print("=" * 40)

    # Create Array
    def create_array(self):

        self.show_title("CREATE NUMPY ARRAY")

        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                values = input("Enter elements: ").split()

                if len(values) == 0:
                    print("Please enter elements.")
                    return

                self.array = np.array([int(x) for x in values])

            elif choice == "2":

                rows = int(input("Enter rows: "))
                cols = int(input("Enter columns: "))

                if rows <= 0 or cols <= 0:
                    print("Rows and columns must be positive.")
                    return

                values = input("Enter elements: ").split()

                if len(values) != rows * cols:
                    print("Incorrect number of elements.")
                    print("Required elements:", rows * cols)
                    return

                self.array = np.array([int(x) for x in values]).reshape(rows, cols)

            elif choice == "3":

                layers = int(input("Enter layers: "))
                rows = int(input("Enter rows: "))
                cols = int(input("Enter columns: "))

                if layers <= 0 or rows <= 0 or cols <= 0:
                    print("Dimensions must be positive.")
                    return

                values = input("Enter elements: ").split()

                required = layers * rows * cols

                if len(values) != required:
                    print("Incorrect number of elements.")
                    print("Required elements:", required)
                    return

                self.array = np.array([int(x) for x in values]).reshape(layers, rows, cols)

            else:
                print("Invalid choice.")
                return

            print("\nArray created successfully:")
            print(self.array)

        except ValueError:
            print("Please enter integer values only.")

    # Indexing and Slicing
    def indexing_slicing(self):

        if not self.__check_array():
            return

        self.show_title("INDEXING AND SLICING")

        print("Array:")
        print(self.array)

        try:

            if self.array.ndim == 1:

                index = int(input("Enter index: "))
                print("Element:", self.array[index])

                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))

                print("Sliced Array:")
                print(self.array[start:end])

            elif self.array.ndim == 2:

                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))

                print("Element:", self.array[row, col])

                start_row = int(input("Enter start row: "))
                end_row = int(input("Enter end row: "))

                start_col = int(input("Enter start column: "))
                end_col = int(input("Enter end column: "))

                print("Sliced Array:")
                print(self.array[ start_row:end_row ,start_co l:end_col] )

            elif self.array.ndim == 3:

                layer = int(input("Enter layer index: "))
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))

                print( "Element:", self.array[layer, row, col] )

                print("Sliced Array:")
                print(self.array[layer])

        except (ValueError, IndexError):
            print("Invalid index.")

    # Mathematical Operations
    def mathematical_operations(self):

        if not self.__check_array():
            return

        self.show_title("MATHEMATICAL OPERATIONS")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = input("Enter your choice: ")

        try:

            if choice in ["1", "2", "3", "4"]:

                values = input("Enter second array elements: ").split()

                second = np.array([int(x) for x in values])

                if second.size != self.array.size:
                    print( "Both arrays must have same number of elements." )
                    return

                second = second.reshape(self.array.shape)

                if choice == "1":
                    print("\nResult:")
                    print(self.array + second)

                elif choice == "2":
                    print("\nResult:")
                    print(self.array - second)

                elif choice == "3":
                    print("\nResult:")
                    print(self.array * second)

                elif choice == "4":

                    if np.any(second == 0):
                        print("Division by zero is not allowed.")
                        return

                    print("\nResult:")
                    print(self.array / second)

            elif choice == "5":

                if self.array.ndim != 1:
                    print("Dot product requires 1D arrays.")
                    return

                values = input("Enter second array elements: " ).split()

                second = np.array([int(x) for x in values])

                if second.size != self.array.size:
                    print("Both arrays must have same size.")
                    return

                print("\nDot Product:")
                print(np.dot(self.array, second))

            elif choice == "6":

                if self.array.ndim != 2:
                    print( "Matrix multiplication requires a 2D array." )
                    return

                rows = int(input("Enter second matrix rows: "))

                cols = int( input("Enter second matrix columns: ") )

                values = input( "Enter second matrix elements: " ).split()

                if len(values) != rows * cols:
                    print("Incorrect number of elements.")
                    return

                second = np.array([int(x) for x in values] ).reshape(rows, cols)

                if self.array.shape[1] != second.shape[0]:
                    print( "Matrix dimensions are not compatible." )
                    return

                print("\nMatrix Multiplication:")
                print(np.matmul(self.array, second))

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter integer values.")

    # Combine and Split
    def combine_split(self):

        if not self.__check_array():
            return

        self.show_title("COMBINE OR SPLIT ARRAYS")

        print("1. Combine Arrays")
        print("2. Split Array")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                values = input("Enter another array elements:" ).split()

                second = np.array([int(x) for x in values])

                if second.size != self.array.size:
                    print("Both arrays must have same number of elements." )
                    return

                second = second.reshape(self.array.shape)

                if self.array.ndim == 1:
                    result = np.concatenate((self.array, second))
                else:
                    result = np.concatenate( (self.array, second), axis=0)

                print("\nCombined Array:")
                print(result)

            elif choice == "2":

                parts = int(input("Enter number of parts: "))

                if parts <= 0:
                    print("Parts must be greater than 0.")
                    return

                result = np.array_split(self.array,parts)
                  

                print("\nSplit Arrays:")

                for i, part in enumerate(result, 1):
                    print("Part", i)
                    print(part)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input.")

    # Search, Sort and Filter
    def search_sort_filter(self):

        if not self.__check_array():
            return

        self.show_title("SEARCH, SORT AND FILTER")

        print("1. Search")
        print("2. Sort")
        print("3. Filter")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                value = int(input("Enter value: "))

                if np.any(self.array == value):
                    print("Value found.")
                else:
                    print("Value not found.")

            elif choice == "2":

                print("1. Ascending")
                print("2. Descending")

                sort_choice = input("Enter your choice: " )

                values = self.array.flatten()

                if sort_choice == "1":

                    print("\nAscending Order:")
                    print(np.sort(values))

                elif sort_choice == "2":

                    print("\nDescending Order:")
                    print(np.sort(values)[::-1])

                else:
                    print("Invalid choice.")

            elif choice == "3":

                print("1. Greater than")
                print("2. Less than")
                print("3. Equal to")

                condition = input("Enter condition: ")

                value = int(input("Enter value: "))

                values = self.array.flatten()

                if condition == "1":
                    result = values[values > value]

                elif condition == "2":
                    result = values[values < value]

                elif condition == "3":
                    result = values[values == value]

                else:
                    print("Invalid condition.")
                    return

                print("\nFiltered values:")
                print(result)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter integer values.")

    # Statistics
    def statistics(self):

        if not self.__check_array():
            return

        self.show_title("AGGREGATES AND STATISTICS")

        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Minimum")
        print("5. Maximum")
        print("6. Standard Deviation")
        print("7. Variance")
        print("8. Percentile")
        print("9. Correlation Coefficient")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                print("Sum:", np.sum(self.array))

            elif choice == "2":
                print("Mean:", np.mean(self.array))

            elif choice == "3":
                print("Median:", np.median(self.array))

            elif choice == "4":
                print("Minimum:", np.min(self.array))

            elif choice == "5":
                print("Maximum:", np.max(self.array))

            elif choice == "6":
                print( "Standard Deviation:", np.std(self.array) )

            elif choice == "7":
                print( "Variance:", np.var(self.array) )

            elif choice == "8":

                percentile = float( input("Enter percentile (0-100): ") )

                if percentile < 0 or percentile > 100:
                    print( "Percentile must be between 0 and 100." )
                    return

                print( "Percentile:", np.percentile( self.array,  percentile ) )

            elif choice == "9":

                values = input(  "Enter second array elements: " ).split()

                second = np.array( [int(x) for x in values]  )

                first = self.array.flatten()

                if first.size != second.size:
                    print(  "Both arrays must have same size."  )
                    return

                correlation = np.corrcoef(first,  second )[0, 1]

                print( "Correlation Coefficient:", correlation )

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid values.")
