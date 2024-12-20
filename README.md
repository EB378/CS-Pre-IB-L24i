# CS-Pre-IB-L24i
Pre-IB Computer Science Course, L24i, 2024-2025, Basics of CS

* Pre-IB computer science project
** Overview
   - The project allows you to increase your final grade by a maximum
     of 3 grades (maximum level 3 in grading levels below)
   - Your program must process text data in a meaningful way, but you
     should not strive for a real-world application.
   - Grading is based on
     - specification
     - correctness and exception handling
     - code clarity
     - resource management.
   - An example is provided for you below, but your program need not
     be as complicated. The example below is relatively complicated,
     because it
     - is capable of reading input from multiple sources: command
       line, data file and keyboard (user)
     - defines a class and uses it to store and analyze data
     - contains a nested loop (loop within a loop) to process the
       data
     - uses ~null~ values for object variables to indicate that an
       object has been processed already.

** Project deadline
   The dealine of the project is <2024-02-02 Fri 23:59>.

** Project submission
   - Your submission consists of
     1. one *PDF file* containing documentation
        1. your target grade level (1, 2 or 3)
        2. specification
        3. test case with typical input
        4. explanation of how exceptions and special cases are handled
           (levels 2 and 3)
        5. explanation of resource handling (level 3)
     2. one or more ~.java~-files containing the code
     3. possibly one or more text data files needed for the test case.
   - Submission is made via email by providing either
     - one ~.zip~-archive containing all files as an attachment to the
       email, or
     - a link to a GitHub repository containing all files.
   - It is strongly suggested that you use documentation structure
     similar to the example below, as this will make both your and my
     life a lot easier.
   
** Grading levels
*** Criteria for level 1
**** Specification
     - There is a sensible description of what the program does.
     - The program reads input from the user and/or from a text data
       file and performs a meaningful operation.
     - Format of input is explained clearly.
     - The input contains multiple items of data (multiple numbers, or
       multiple lines of text, or similar).
     - At least some of the data is read from the user or from a file
       using a loop (~while~, ~for~).
       - Note: There are /many/ ways to do this. Read multiple lines
         from a file. Repeat the same operation multiple times for the
         user. Read multiple lines from user input.
**** Correctness and exception handling
     - The program works correctly in one documented test case with
       typical input.
     - If any text data files are required to test this, they are
       supplied.
**** Code clarity
     - Code is indented correctly.
     - There is no unnecessary whitespace (no extra empty lines or
       extra spaces).
     - Identifiers (names of variables, constants and functions) are
       meaningful in the context of the program.
*** Additional criteria for level 2
**** Correctness and exception handling
     - At least one exception is caught and reported correctly.  This
       is also documented.
**** Code clarity
     - Constants are identified and named.
     - All non-trivial parts of the code are
       commented. \ldquo{}Non-trivial\rdquo is defined by assuming
       that the reader is a fellow student.
*** Additional criteria for level 3
**** Correctness and exception handling *or* wow-factor
     One of the following:
     - The correct working of the program has been documented in all
       possible special cases (except for the computer running out of
       memory). That is, your program will not throw an exception
       (unless your computer runs out of memory).
     - Your program does something considerably more complex and/or
       sophisticated that would be required. (In this case, it is
       much more difficult to document correct working in all
       special cases.)
**** Resource management
     - At least one resource is closed when no longer needed, even in
       the case of an exception. This is also documented.
**** Code clarity
     - The flow of the program is split into meaningful functions
       called by ~main()~.
     - The role of defined functions is explained in comments.
     - If useful, classes are defined for program-specific data types.
** Example project
*** Documentation
**** Target assessment level
     Target assessment level of this work is 3.
**** Specification
***** What does the program do?
      The program
      1. reads data about persons from a file
      2. prints all persons in groups with namesakes (same first
         names) on consecutive lines.
      The user supplies the name of the input file either as a program
      argument or, if none is given, from keyboard.

***** Data format
       The input data text file consists of lines, each line
       containing
       #+begin_center
       =lastname firstname address=
       #+end_center
       Both ~lastname~ and ~firstname~ are single words, while
       ~address~ is all the remaining text on the line.
**** Correctness and exception handling
***** Typical test case
      File [[file:persons.txt]] contains data from 6 persons with 3 groups
      of namesakes. The number of persons in these groups is 3
      (Michael), 2 (Jane) and 1. When the program (file
      [[file:Main.java]]) is run with
      #+name: run-application
      #+begin_src sh :exports both :cache no :results output verbatim
      java Main.java persons.txt
      #+end_src

      the output is correct, with each group of namesakes printed on
      consecutive lines:

      #+RESULTS: run-application
      : Cash Michael Las Vegas, US
      : Knight Michael Moving truck
      : Burnham Michael The final frontier
      : McGyver Agnus Phoenix, Foundation
      : Doe Jane Aberdeen, Scotland
      : Tarzan Jane Greystoke, UK

***** Exception handling (levels 2 and 3)
      The following are all the possible exceptions / special cases
      and the way they are handled.
      - More than one program argument: only the first one is used as
        name of data file.
      - Reading user-supplied data file name fails: exception is
        caught and printed to user, program exits.
      - Opening data file for reading fails: exception is caught and
        printed to user, program exits.
      - Reading data from data file fails: exception caught and
        printed, program exits.
      - Number of persons exceeds program constant: reported to user,
        program exits.

***** Resource management (level 3)
      The following resources are opened with ~try~-with-resources
      -statements and are therefore closed automatically when the
      program no longer needs them, even in the case of an exception.
      - ~Scanner~ for system input when reading user-supplied file
        name.
      - ~Scanner~ when reading data file.

*** Program code (provided here just for ease of reading, would be a separate file in your submission)
    #+begin_src java :exports code :tangle Main.java
      import java.io.File;
      import java.util.Scanner;

      public class Main
      {
        public static void main (String[] args)
        {
          // maximum number of persons this program can handle
          final int MAX_NUM_PERSONS = 1000;

          // get name of data file
          String filename;
          if (args.length >= 1)
            filename = args [0];
          else
            filename = queryFilename ();

          // read persons into an array
          Person[] persons = new Person [MAX_NUM_PERSONS];
          int numPersons = readPersons (filename, persons);

          // list namesakes
          printNamesakes (persons, numPersons);
        }

        // query the user for the name of data file; return value is the
        // name of the file
        static String queryFilename ()
        {
          String filename;
          try (Scanner scanner = new Scanner (System.in))
          {
            System.out.print ("give data file name: ");
            filename = scanner.next ();
          }
          catch (Exception e)
          {
            System.out.println ("unable to read data file name, exception: " + e);
            filename = "";
            System.exit (-1);
          }

          return filename;
        }

        // read persons from data file with given file name into the
        // supplied array; return value is the number of persons in the data
        // file
        static int readPersons (String filename, Person[] persons)
        {
          int numPersons = 0;

          // open file and create a scanner for it
          try (Scanner scanner = new Scanner (new File (filename)))
          {
            try
            {
              // read while there are lines in the file
              while (scanner.hasNextLine ())
              {
                // report error and exit if program limit exceeded
                if (numPersons > persons.length)
                {
                  System.out.println ("exceeded maximum number of persons " + persons.length);
                  System.exit (-1);
                }

                // each line has last name, first name, address
                String lastname = scanner.next ();
                String firstname = scanner.next ();
                String address = scanner.nextLine (); // address is the rest of the line

                persons [numPersons] = new Person (lastname, firstname, address);
                numPersons = numPersons + 1;
              }
            }
            catch (Exception e)
            {
              System.out.println ("unable to read person data, exception " + e);
              System.exit (-1);
            }
          }
          catch (Exception e)
          {
            System.out.println ("unable to open file " + filename + " for reading, exception : " + e);
            System.exit (-1);
          }

          return numPersons;
        }

        // print the persons as groups of namesakes
        static void printNamesakes (Person[] persons, int numPersons)
        {
          // go through the persons
          for (int personInd = 0; personInd < numPersons; personInd = personInd + 1)
          {
            Person person = persons [personInd];

            // if the person has not been printed yet, print the person and
            // the possible namesakes
            if (person != null)
            {
              System.out.println (person);

              // go through namesake candidates, starting from the next
              // person
              for (int candInd = personInd + 1; candInd < numPersons; candInd = candInd + 1)
              {
                Person candidate = persons [candInd];
                if (candidate != null && person.isNamesake (candidate))
                {
                  System.out.println (candidate);
                  persons [candInd] = null; // set to null, since the person has been printed
                }
              }
            }
          } 
        }
      }


      // class containing information of person and helpful methods
      class Person
      {
        public Person (String lastname, String firstname, String address)
        {
          this.lastname = lastname;
          this.firstname = firstname;
          this.address = address;
        }

        // method for testing whether another person is a namesake
        public boolean isNamesake (Person person)
        {
          return firstname.equals (person.firstname);
        }

        public String toString ()
        {
          // note that address always contains a space at its beginning, so
          // none needs to be added between firstname and address
          return lastname + " " + firstname + address;
        }

        public String firstname, lastname, address; // member variables
      }

    #+end_src