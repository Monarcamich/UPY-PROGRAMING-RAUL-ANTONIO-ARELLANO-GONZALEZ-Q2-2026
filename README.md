# UPY-PROGRAMING-RAUL-ANTONIO-ARELLANO-GONZALEZ-Q2-2026

  ---
  CW07

  Project description

  This program calculates the verification digit (dígito verificador) of a Chilean RUT (Rol Único Tributario) using the módulo 11 algorithm. The user inputs the RUT number without dashes or
  verification digit, and the program:

  1. Reverses the digit order of the input RUT.
  2. Multiplies each digit by a cycling sequence of multipliers [2, 3, 4, 5, 6, 7].
  3. Sums all the products and computes sum % 11.
  4. Subtracts that result from 11 to obtain the verification digit.
  5. Special cases: if the result is 11, the digit is 0; if the result is 10, the digit is K.
  6. Prints the calculated verification digit and the full RUT in the format rol-digito_verificador.

  Example:
  - Input: 201012341
  - Output: El dígito verificador calculado es: K / Rol completo: 201012341-K

  How to run the program

  1. Open a terminal and navigate to the CW07 directory:
  cd "CW07"
  2. Run the script with Python 3:
  python3 cw07.py
  3. When prompted, enter the RUT number without dashes or verification digit (e.g., 201012341).
  4. The program will print the calculated verification digit and the complete RUT.

  ---
  Classwork 08 — Numerical Integration

  Project description

  This program approximates the definite integral of six different functions over predefined intervals and compares the result to the exact value. The user picks a function, picks a mode, and the program returns the numerical approximation together with the absolute and relative errors. The supported numerical methods are:

  - LRM — Left Riemann (rectangles aligned to the left endpoint of each subinterval).
  - RRM — Right Riemann (rectangles aligned to the right endpoint).
  - MPM — Midpoint (rectangles evaluated at the midpoint of each subinterval).
  - TRAP — Trapezoidal rule.

  Available functions (with their interval and exact integral):

  1. x² + 2x − 3   on [1, 4]            → 27.00
  2. 3x³ − x² + 5  on [0, 2]            → 21.33
  3. sin(x)        on [0, π]            → 2.00
  4. cos(x) + 1    on [0, π/2]          → 2.5708
  5. exp(x)        on [0, 2]            → 6.3891
  6. ln(x)         on [1, 3]            → 1.2958

  Available modes:

  1. Default — runs the integral with n = 100 subintervals using the Midpoint method (MPM).
  2. Custom — the user sets both the number of subintervals n and the method (LRM / RRM / MPM / TRAP).
  3. Auto-adjust — the user sets a relative error tolerance; the program starts at n = 10 and doubles n each iteration until the relative error falls below the tolerance (or until n > 1,000,000).

  Example output (Default mode, function 3):
  - Function: math.sin(x)
  - Interval: [0, 3.141592653589793]
  - Method: MPM
  - Subintervals (n): 100
  - Approximation: 1.99983550
  - Exact value:   2.00000000
  - Absolute error: 0.00016450
  - Relative error: 0.000082 (0.0082%)

  How to run the program

  1. Open a terminal and navigate to the Classwork-08-Numerical-Integration directory:
  cd "Classwork-08-Numerical-Integration"
  2. Run the script with Python 3:
  python3 numerical_integration.py
  3. When prompted, choose a function (1-6) and a mode (1/2/3). If you pick mode 2 or 3, you will be asked for the number of subintervals, the method, and/or the tolerance.
  4. The program will print the chosen function, interval, method, number of subintervals, the numerical approximation, the exact value, the absolute error, and the relative error.

  A pseudocode description of the algorithm is available in `PPP.txt`, and a flowchart of the full process is available in `Flowchart.png`.

  ---
  CW09 — Spanish Verb Conjugator

  Project description

  This program conjugates Spanish verbs in the present tense. The user inputs a verb ending in -ar, -er, or -ir, and the program:

  1. Extracts the stem by removing the last two characters from the verb.
  2. Identifies the verb type (-ar, -er, or -ir) based on the ending.
  3. Applies the appropriate conjugation endings for each pronoun.
  4. Displays the conjugated verb for each of the eight Spanish pronouns: yo, tú, él/ella, nosotros, vosotros, ellos/ellas.

  Example:
  - Input: hablar
  - Output: yo hablo / tú hablas / él habla / ella habla / nosotros hablamos / vosotros habláis / ellos hablan / ellas hablan

  How to run the program

  1. Open a terminal and navigate to the CW09 directory:
  cd "CW09"
  2. Run the script with Python 3:
  python3 "Spanish verb conjugator.py"
  3. When prompted, enter a Spanish verb ending in -ar, -er, or -ir (e.g., hablar, comer, escribir).
  4. The program will print the conjugated verb for each pronoun.

  A pseudocode description of the program is available in `PPP.txt`, and a flowchart of the conjugation process is available in `Flowchart.png`.

  ---

  CW10 — School Management System

  Project description

  This program manages students, professors, and coordinators in a school system with role-based access. The system uses dictionaries to store users, subjects, and grades, and provides different functionality based on the logged-in user's role:

  - **Student**: View their report card with grades for all 7 subjects, see which subjects are approved (grade ≥ 8.0), and which subjects are pending.

  - **Professor**: View the list of students, select a student and subject to update their grade, and confirm the grade change.

  - **Coordinator**: View the complete list of professors, all subjects, and all students with their grades for each subject.

  Available users (username / password / role):

  - Students: jperez, dromo, mjuarez, mlopez, euc, cbalam (password: 1234)
  - Professor: jpedrozo (password: 1234)
  - Coordinator: dgamboa (password: 1234)

  Subjects offered:
  1. Discrete Mathematics
  2. Programming
  3. English II
  4. Differential Calculus
  5. Probability and Statistics
  6. Computer and Server Architecture
  7. Socio-Emotional Skills and Conflict Management

  Example output (Student role):
  - Report Card: Juan Pérez
  - Discrete Mathematics: 8.5
  - Programming: 9.2
  - English II: 9.0
  - Differential Calculus: 7.8
  - Probability and Statistics: 8.3
  - Computer and Server Architecture: 6.8
  - Socio-Emotional Skills and Conflict Management: 9.5
  - Approved subjects: {Discrete Mathematics, Programming, English II, Probability and Statistics, Socio-Emotional Skills and Conflict Management}
  - Pending subjects: {Differential Calculus, Computer and Server Architecture}

  How to run the program

  1. Open a terminal and navigate to the Classwork-10-School-management-system directory:
  cd "Classwork-10-School-management-system"
  2. Run the script with Python 3:
  python3 school_management_system.py
  3. When prompted, enter your username and password.
  4. The program will display different options based on your role (student, professor, or coordinator).

  A pseudocode description of the program is available in `PPP.txt`, and a flowchart of the process is available in `Flowcchart.png`.

  ---

  Classwork 11 — The Mandelbrot Set

  Project description

  This program generates and visualizes the Mandelbrot set by computing the iteration count for each pixel in a 2D grid. The Mandelbrot set is the set of complex numbers c for which the sequence z(n+1) = z(n)² + c, starting from z(0) = 0, does not diverge to infinity (i.e., |z| remains bounded).

  The program:
  1. Reads configuration parameters (width, height, coordinate bounds, max iterations) from a config.txt file.
  2. Maps each pixel to a complex number c using the formula:
     - real = real_min + (column / width) × (real_max - real_min)
     - imag = imag_min + (row / height) × (imag_max - imag_min)
  3. For each pixel, iterates z = z² + c until |z| ≥ 2 or max_iter is reached.
  4. Records the number of iterations for each pixel in a CSV file.

  Configuration parameters (config.txt):
  - ancho: width of the image in pixels
  - alto: height of the image in pixels
  - real_min, real_max: real axis range (default: -2.0 to 1.0)
  - imag_min, imag_max: imaginary axis range (default: -1.5 to 1.5)
  - max_iter: maximum iterations per pixel (default: 100)

  Example output (mandelbrot.csv):
  - row,column,iterations
  - 0,0,100
  - 0,1,98
  - 1,0,95
  - ...

  How to run the program

  1. Open a terminal and navigate to the Classwork-11-The-Mandelbrot-Set directory:
  cd "Classwork-11-The-Mandelbrot-Set"
  2. (Optional) Edit config.txt to adjust image size, coordinate bounds, or iterations.
  3. Run the script with Python 3:
  python3 mandelbrot_set_math.py
  4. The program will generate a mandelbrot.csv file with iteration counts for each pixel.

  A pseudocode description of the program is available in `PPP.txt`, and a sample output is available in `mandelbrot.csv`.

---

Classwork 12 — The Mandelbrot Set (Visualization)

Project description

This program generates a visual representation (PNG image) of the Mandelbrot set using the iteration data computed in Classwork 11. It reads the iteration counts from a CSV file and maps each pixel to a grayscale brightness value based on how many iterations were needed to determine whether the point belongs to the set.

The program:

1. Reads configuration parameters (width, height, max_iter) from a config.txt file.
2. Reads iteration data from mandelbrot.csv (generated by Classwork 11).
3. Maps each pixel to a brightness value:
   - If iterations == max_iter: the point is inside the set → brightness = 40 (black)
   - Otherwise: brightness = (iterations / max_iter) × 255 (grayscale gradient)
4. Creates a grayscale image using PIL (Pillow) and saves it as mandelbrot.png.

Configuration parameters (config.txt):

- ancho: width of the image in pixels
- alto: height of the image in pixels
- max_iter: maximum iterations per pixel (must match the value used in Classwork 11)

Example output (mandelbrot.png):

- A grayscale image where black regions represent points inside the Mandelbrot set and lighter regions represent points outside the set.
- The image shows the characteristic "cardioid" shape and "bulbs" of the Mandelbrot set.

How to run the program

1. Open a terminal and navigate to the Classwork-12-The-Mandelbrot-Set directory:
   cd "Classwork-12-The-Mandelbrot-Set"
2. Ensure mandelbrot.csv (from Classwork 11) and config.txt are in the same directory.
3. Run the script with Python 3:
   python3 mandelbrot_set_vis.py
4. The program will generate a mandelbrot.png image with the visualization.

A pseudocode description of the program is available in `PPP.txt`, and the visualization output is available in `mandelbrot.png`.

---

Classwork 13 — Error Handling (Re-implementation of CW07, CW08, CW09)

Project description

This classwork re-implements the three previous programs (CW07 Chilean RUT verifier, CW08 numerical integrator, and CW09 Spanish verb conjugator) adding custom exceptions and `try/except` blocks so the programs recover gracefully from invalid user input instead of crashing.

The three scripts are:

- **CW07.py** — Chilean RUT verification digit calculator. Uses a custom `DigitoApocrifoError` exception and a `try/except` around the `rol.split("-")` call so a RUT without the dash prompts "Rol no valido" instead of raising a `ValueError`. After the algorithm runs, it compares the calculated digit with the user-supplied digit and raises `DigitoApocrifoError` if they differ.

- **CW08.py** — Numerical integration of a user-defined function on a user-defined interval. Defines a custom `IntegrationError` exception. The input block wraps the endpoint parsing in `try/except ValueError, NameError` and re-raises them as `IntegrationError("Endpoints must be numbers (or use 'pi').")`. It then supports LRM, RRM, MPM (rectangle methods) and TM (trapezoid) on the function and interval provided by the user.

- **CW09.py** — Spanish verb conjugator. Defines a custom `VerbError` exception. The input loop keeps asking until the user types a verb ending in -ar, -er, or -ir; if it doesn't, the program prints "Invalid verb" and re-prompts. Conjugation logic and output are identical to CW09.

How to run the program

1. Open a terminal and navigate to the Classwork-13-Error-Handling directory:
   cd "Classwork-13-Error-Handling"
2. Run any of the three scripts with Python 3, for example:
   python3 CW07.py
   python3 CW08.py
   python3 CW09.py
3. Follow the on-screen prompts. Each script will re-prompt on invalid input instead of terminating with an unhandled exception.

---

Classwork 14 — Error Handling (Re-implementation of CW10, CW11, CW12)

Project description

This classwork re-implements the three more complex previous programs (CW10 school management system, CW11 Mandelbrot iteration, CW12 Mandelbrot visualization) replacing the raw `open()` / `read()` / `split()` sequences with safer versions that handle missing files and malformed configuration lines.

The three scripts are:

- **school_management_system.py** — Same role-based school system as CW10 (student, professor, coordinator). Adds a validation block so the username/password loop keeps re-prompting until valid credentials are entered, and validates that the chosen student, subject, and grade can be parsed before mutating the grades dictionary.

- **mandelbrot_set_math.py** — Same Mandelbrot iteration as CW11, but the config-parsing block uses a `try/except` to skip blank lines and comment lines starting with `#`, and to handle lines that do not contain a valid `key=value` pair. This prevents the program from crashing on a stray blank line in `config.txt`.

- **mandelbrot_set_vis.py** — Same Mandelbrot visualization as CW12, also guarded against malformed lines in `config.txt` and against `mandelbrot.csv` rows whose column count does not match the expected `fila,columna,iteraciones` format.

How to run the program

1. Open a terminal and navigate to the Classwork-14-Error-Handling directory:
   cd "Classwork-14-Error-Handling"
2. For the Mandelbrot scripts, place a `config.txt` in the same directory (see CW11/CW12 for the expected keys) and, for the visualization, the `mandelbrot.csv` produced by the math script.
3. Run the script you want with Python 3, for example:
   python3 school_management_system.py
   python3 mandelbrot_set_math.py
   python3 mandelbrot_set_vis.py
4. The program will print a confirmation message when it finishes; malformed config lines or CSV rows are skipped instead of aborting the run.

---

Classwork 15 — Sorting Algorithms Visualization (Bubble, Insertion, Selection)

Project description

This program generates 10 random integers between 0 and 100, sorts them using one of three classic O(n²) sorting algorithms, and animates the sort on screen using `stddraw` (a Python port of `stdlib`/`stddraw`). Each value in the array is drawn as a vertical bar whose height equals the value, and the pair of indices being compared (or the position of the key / the current minimum) is highlighted in red on every step.

The supported algorithms are:

- **Bubble Sort** (`bubble_sort` / `bubble_sort_animated`) — Repeatedly sweeps the array and swaps adjacent elements that are out of order. After each full sweep, the largest unsorted element is guaranteed to be at the end of the array.

- **Insertion Sort** (`insertion_sort` / `insertion_sort_animated`) — Iterates from left to right, taking each element as a "key" and shifting the larger preceding elements one position to the right to make room for it.

- **Selection Sort** (`selection_sort` / `selection_sort_animated`) — Iterates from left to right, finds the minimum of the unsorted suffix, and swaps it into the next position of the sorted prefix.

The non-animated `bubble_sort`, `insertion_sort`, and `selection_sort` functions sort in place without drawing; the `*_animated` variants wrap them with calls to `draw_bars` so each comparison and swap is visible on the canvas. The red highlight is drawn on the pair being compared (bubble), the key being inserted (insertion), or the current minimum and the element being compared (selection).

How to run the program

1. Open a terminal and navigate to the Classwork-15-bubblesort-sorting-Algorithms directory:
   cd "Classwork-15-bubblesort-sorting-Algorithms"
2. Run the script with Python 3:
   python3 boubble-algortithim.py
3. The console will print `Before sorting: [...]` and then a window will open showing the sorting animation in real time. When the animation finishes, the console prints `After sorting: [...]` and the window remains open.
4. To try a different algorithm, open the script and comment/uncomment the `bubble_sort_animated`, `insertion_sort_animated`, or `selection_sort_animated` call near the bottom of the file.

A pseudocode description of the program is available in `PPP.txt`, and a flowchart of the process is available in `FLOWCHART.png`. The helper modules `stddraw.py` and `color.py` must stay in the same directory as the main script.

---

Classwork 16 — Recursive Functions

Project description

This program demonstrates classic recursive algorithms and a recursive JSON-flattening utility. Each function is built around a base case that stops the recursion and a recursive case that reduces the problem until the base case is reached. The implemented functions are:

- **recursive(n)** — Counts down from n-1 to 0, printing each value along the way, and returns the string `"Done"` when n ≤ 0.

- **fibonacci(n)** — Returns the n-th Fibonacci number. Base case: n == 0 or n == 1. Recursive case: `fibonacci(n-1) + fibonacci(n-2)`.

- **factorial(n)** — Returns n!. Base case: n == 0 or n == 1 → returns 1. Recursive case: `n * factorial(n-1)`.

- **multiplicacion_recursive(n, m)** — Multiplies n by m using recursion. Base case: m == 0 → returns 0. Recursive case: `n + multiplicacion_recursive(n, m-1)`.

- **division_entera_recursiva(dividendo, divisor)** — Integer division using recursion. Base case: `dividendo - divisor < 0` → returns 0. Recursive case: `division_entera_recursiva(dividendo - divisor, divisor) + 1`.

- **potencia_recursiva(base, exponente)** — Computes base^exponente using recursion. Base case: exponente == 0 → returns 1. Recursive case: `base * potencia_recursiva(base, exponente - 1)`.

- **serie_collatz(n)** — Prints the Collatz sequence starting at n. If n == 1, prints `1` and returns `"END!"`. If n is even, prints `n//2` and recurses on `n//2`. Otherwise prints `3n+1` and recurses on `3n+1`.

- **aplanar_json(diccionario, clave_padre, separador)** — Flattens a nested JSON-like dict into a single-level dict whose keys are dotted paths (default separator `.`). Supports nested dicts (recurses with the accumulated key as `clave_padre`) and lists (each element gets an index suffix, e.g. `g.0.h`). Non-collection values are stored as-is.

The `__main__` block feeds a sample nested JSON to `aplanar_json` and runs each numeric/sequence function with a fixed input so the recursion can be observed in the console.

How to run the program

1. Open a terminal and navigate to the Classwork-16-Recursive-Functions directory:
   cd "Classwork-16-Recursive-Functions"
2. Run the script with Python 3:
   python3 recursive_functions.py
3. The program will print, in order: `recursive(5)`, `fibonacci(10)`, `factorial(5)`, `multiplicacion_recursive(3, 4)`, `division_entera_recursiva(17, 5)`, `potencia_recursiva(2, 5)`, the Collatz series starting at 6, and the flattened version of the sample JSON.

A pseudocode description of the program is available in `recursive_functions_ppp.txt`.