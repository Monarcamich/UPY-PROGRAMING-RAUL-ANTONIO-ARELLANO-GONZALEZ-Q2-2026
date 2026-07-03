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

  1. Open a terminal and navigate to the Classwork-10-School-management-system.py directory:
  cd "Classwork-10-School-management-system.py"
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