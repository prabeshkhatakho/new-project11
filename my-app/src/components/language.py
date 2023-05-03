import os
from pathlib import Path


file_path = "newfile.js"


if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' already exists and has been deleted.")
js_code = """import React from 'react'

function language() {
  return (
    <div>
      <h1>types of programming language</h1>
      <p>There are numerous programming languages available for various purposes, each with its own syntax, features, and use cases. Here are some common types of programming languages:
        Procedural programming languages: These languages are used for writing procedures or routines that are executed in a linear fashion, following a sequence of steps. Examples include C, Pascal, and Fortran.
        Object-oriented programming (OOP) languages: These languages are based on the concept of objects, which are instances of classes that encapsulate data and behavior. Examples include Java, C++, and Python.
        Functional programming languages: These languages treat computation as the evaluation of mathematical functions and avoid changing state and mutable data. Examples include Haskell, Lisp, and ML.
        Scripting languages: These languages are used for automating tasks, such as web scripting, system administration, and data manipulation. Examples include Python, Perl, and Ruby.
        Markup languages: These languages are used for describing the structure and presentation of documents, such as HTML for web pages and XML for data representation.
        Query languages: These languages are used for querying databases and retrieving data, such as SQL (Structured Query Language) for relational databases.
        Domain-specific languages (DSLs): These languages are designed for specific tasks or industries, such as MATLAB for scientific computing, R for data analysis, and LaTeX for document typesetting.
        Scripting languages for automation and configuration: These languages are used for automating tasks and configuring systems, such as Bash for shell scripting and PowerShell for Windows automation.
        Markup languages for styling and layout: These languages are used for defining the presentation and layout of documents, such as CSS (Cascading Style Sheets) for web styling and XSL (eXtensible Stylesheet Language) for XML document transformation.
        Query languages for data manipulation: These languages are used for querying and manipulating data, such as GraphQL for APIs and XQuery for XML documents.
        These are just some of the many types of programming languages available. Each type has its own strengths, weaknesses, and use cases, and the choice of language depends on the specific requirements of a particular project or task.</p>
        <br></br>
        <h1>what is oop??</h1>
        <p>OOP stands for Object-Oriented Programming. It is a programming paradigm that uses the concept of "objects" to represent and manipulate data and behaviors in a software system. In OOP, objects are instances of classes, which are blueprints or templates that define the structure, properties, and methods (functions) of objects.
            The key principles of OOP are:
            Encapsulation: The process of hiding internal details of an object and exposing only what is necessary. It allows for better organization of code and reduces complexity by grouping related data and behaviors into objects.
            Inheritance: The ability of a class to inherit properties and methods from a parent class. It promotes code reuse and allows for the creation of hierarchical relationships between classes.
            Polymorphism: The ability to use objects of different classes interchangeably, as long as they implement the same interface or have the same method signatures. It promotes flexibility and extensibility in code.
            Abstraction: The process of simplifying complex systems by creating abstract classes or interfaces that define common properties and behaviors. It allows for the creation of reusable code components and promotes code modularity.
            OOP provides several advantages, including modularity, reusability, maintainability, and scalability. It is widely used in many popular programming languages such as Java, C++, Python, and C#. By using OOP principles, developers can create well-structured, organized, and efficient code for complex software systems.</p>
        <br></br>
        <h1>what is functional programming language??</h1>
        <p>Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. A functional programming language is a programming language that supports and encourages functional programming concepts and techniques. Some key characteristics of functional programming languages include:
            Immutability: In functional programming, data is typically immutable, meaning it cannot be changed once it is created. Instead of modifying data, functional programs create new data structures with updated values, which promotes immutability and reduces the risk of unintended side effects.
            Higher-order functions: Functional programming languages often support higher-order functions, which are functions that can take other functions as arguments or return them as results. Higher-order functions enable powerful abstractions and allow for more concise and modular code.
            Pure functions: Pure functions are functions that produce the same output for the same input and have no side effects. Functional programming languages often emphasize the use of pure functions, which makes code easier to reason about and test.
            First-class functions: First-class functions means that functions can be treated as first-class citizens, which means they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions. First-class functions provide flexibility and expressiveness in functional programming.
            Recursion: Recursion is a common technique used in functional programming to solve problems by defining functions that call themselves. Functional programming languages often provide support for recursion and make it an important part of the programming paradigm.
            Focus on expressions rather than statements: Functional programming languages often favor the use of expressions, which are pieces of code that produce a value, rather than statements, which are instructions that perform an action. Expressions allow for more concise and declarative code.
            Examples of functional programming languages include Haskell, Lisp, ML, Scala, and Clojure. However, it's worth noting that many modern programming languages, such as JavaScript, Python, and Ruby, also incorporate functional programming concepts and allow for a mixed programming paradigm that combines both functional and imperative styles.</p>
    </div>
  )
}

export default language

"""

file = Path(file_path)
file.write_text(js_code)

print(f"File '{file_path}' has been created with the JavaScript code.")
